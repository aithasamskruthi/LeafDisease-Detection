import streamlit as st
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import numpy as np
import json
import os
import time
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile
import base64

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LeafDoc AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CSS Styling ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main { background-color: #0d1117; }

h1, h2, h3 { font-family: 'Syne', sans-serif !important; }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #4ade80 0%, #22d3ee 50%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin-bottom: 0.3rem;
}

.hero-sub {
    color: #6b7280;
    font-size: 1.05rem;
    font-weight: 300;
    letter-spacing: 0.05em;
}

.card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: border-color 0.2s;
}

.card:hover { border-color: #4ade80; }

.disease-badge {
    display: inline-block;
    background: linear-gradient(135deg, #4ade8022, #22d3ee22);
    border: 1px solid #4ade8055;
    color: #4ade80;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.4rem;
    padding: 0.5rem 1.2rem;
    border-radius: 50px;
    margin-bottom: 0.5rem;
}

.severity-low    { color: #4ade80; border-color: #4ade8055; background: #4ade8011; }
.severity-medium { color: #fbbf24; border-color: #fbbf2455; background: #fbbf2411; }
.severity-high   { color: #f87171; border-color: #f8717155; background: #f8717111; }

.step-card {
    background: #0d1117;
    border: 1px solid #21262d;
    border-left: 3px solid #4ade80;
    border-radius: 8px;
    padding: 0.8rem 1rem;
    margin: 0.4rem 0;
    color: #e6edf3;
    font-size: 0.92rem;
}

.confidence-bar-bg {
    background: #21262d;
    border-radius: 100px;
    height: 8px;
    width: 100%;
    margin-top: 6px;
}

.confidence-bar {
    background: linear-gradient(90deg, #4ade80, #22d3ee);
    border-radius: 100px;
    height: 8px;
}

.label-text {
    color: #8b949e;
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.2rem;
}

.value-text {
    color: #e6edf3;
    font-size: 1rem;
    font-weight: 500;
}

.upload-hint {
    color: #6b7280;
    font-size: 0.85rem;
    text-align: center;
    padding: 1rem;
}

.sidebar-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #4ade80;
    margin-bottom: 0.5rem;
}

.stButton > button {
    background: linear-gradient(135deg, #4ade80, #22d3ee) !important;
    color: #0d1117 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.5rem 2rem !important;
    font-size: 0.95rem !important;
    transition: opacity 0.2s !important;
}

.stButton > button:hover { opacity: 0.85 !important; }

/* Dark overrides */
[data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #21262d; }
.stSelectbox label, .stSlider label, .stFileUploader label { color: #8b949e !important; }
</style>
""", unsafe_allow_html=True)

# ─── Load Disease Knowledge Base ─────────────────────────────────────────────
from disease_knowledge import DISEASE_INFO, CLASS_NAMES

# ─── Load Model ──────────────────────────────────────────────────────────────
@st.cache_resource
def load_model(num_classes):
    model = models.efficientnet_b0(weights=None)
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    model_path = "leaf_disease_model.pth"
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path, map_location="cpu"))
        model.eval()
        return model, True
    return model, False

# ─── Image Preprocessing ─────────────────────────────────────────────────────
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

def predict(model, image: Image.Image):
    img_t = transform(image).unsqueeze(0)
    with torch.no_grad():
        logits = model(img_t)
        probs  = torch.softmax(logits, dim=1)[0]
    top3_probs, top3_idx = torch.topk(probs, 3)
    return top3_probs.numpy(), [CLASS_NAMES[i] for i in top3_idx.numpy()]

def get_severity(confidence: float, disease_name: str) -> str:
    if "healthy" in disease_name.lower():
        return "Healthy"
    if confidence > 0.80:
        return "High"
    elif confidence > 0.55:
        return "Medium"
    return "Low"

# ─── Translation ─────────────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def translate_text(text: str, dest_lang: str) -> str:
    if dest_lang == "en":
        return text
    try:
        translated = GoogleTranslator(source="en", target=dest_lang).translate(text)
        return translated if translated else text
    except Exception:
        return text

# ─── TTS ─────────────────────────────────────────────────────────────────────
def text_to_speech(text: str, lang: str) -> str:
    tts = gTTS(text=text, lang=lang, slow=False)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        return f.name

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
    <audio controls autoplay style="width:100%; margin-top:0.5rem; border-radius:8px;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

# ─── Language Options ─────────────────────────────────────────────────────────
LANGUAGES = {
    "English":    "en",
    "Hindi (हिन्दी)":  "hi",
    "Telugu (తెలుగు)": "te",
    "Tamil (தமிழ்)":   "ta",
    "Kannada (ಕನ್ನಡ)": "kn",
    "Bengali (বাংলা)":  "bn",
    "Marathi (मराठी)":  "mr",
    "Gujarati (ગુજરાતી)": "gu",
    "French":     "fr",
    "Spanish":    "es",
    "German":     "de",
    "Arabic":     "ar",
    "Chinese":    "zh-cn",
    "Japanese":   "ja",
}

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">🌿 LeafDoc AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="label-text">Settings</div>', unsafe_allow_html=True)
    st.markdown("---")

    selected_lang = st.selectbox(
        "🌐 Output Language",
        list(LANGUAGES.keys()),
        index=0
    )
    lang_code = LANGUAGES[selected_lang]

    enable_voice = st.toggle("🔊 Voice Readout", value=True)

    st.markdown("---")
    st.markdown('<div class="label-text">About</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="color:#6b7280; font-size:0.8rem; line-height:1.6;">
    LeafDoc AI detects plant leaf diseases using deep learning (EfficientNet-B0),
    estimates severity, and provides multilingual treatment guidance with voice output.
    <br><br>
    <b style="color:#4ade80;">Supported Plants:</b><br>
    Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="label-text">Model Info</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="color:#6b7280; font-size:0.8rem; line-height:1.6;">
    Architecture: EfficientNet-B0<br>
    Dataset: PlantVillage (38 classes)<br>
    Input: 224×224 RGB
    </div>
    """, unsafe_allow_html=True)

# ─── Main Layout ──────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">LeafDoc AI 🌿</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Plant Disease Detection · Severity Analysis · Multilingual Treatment · Voice Guidance</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Load model
model, model_loaded = load_model(len(CLASS_NAMES))

if not model_loaded:
    st.warning("""
    ⚠️ **No trained model found** (`leaf_disease_model.pth`).
    
    Running in **demo mode** — predictions will be random.
    
    → Run `python train_model.py` to train the model first (see README).
    """)

col_upload, col_results = st.columns([1, 1.4], gap="large")

with col_upload:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 📤 Upload Leaf Image")
    uploaded_file = st.file_uploader(
        "Choose a leaf image",
        type=["jpg", "jpeg", "png", "webp"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, width=400, caption="Uploaded Leaf")
    else:
        st.markdown('<div class="upload-hint">📷 Upload a clear photo of a plant leaf<br>JPG, PNG or WEBP · Max 200MB</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file:
        analyze_btn = st.button("🔍 Analyze Leaf", use_container_width=True)
    else:
        analyze_btn = False

with col_results:
    if uploaded_file and analyze_btn:
        with st.spinner("Analyzing leaf..."):
            # Demo mode: use random if model not loaded
            if not model_loaded:
                import random
                top_classes = random.sample(CLASS_NAMES, 3)
                raw_probs   = sorted([random.random() for _ in range(3)], reverse=True)
                s = sum(raw_probs)
                top_probs   = [p/s for p in raw_probs]
            else:
                top_probs, top_classes = predict(model, image)

            disease_name = top_classes[0]
            confidence   = float(top_probs[0])
            severity     = get_severity(confidence, disease_name)
            info         = DISEASE_INFO.get(disease_name, DISEASE_INFO["__default__"])

        # Translate
        with st.spinner(f"Translating to {selected_lang}..."):
            t_disease     = translate_text(disease_name.replace("_", " ").title(), lang_code)
            t_description = translate_text(info["description"], lang_code)
            t_steps       = [translate_text(s, lang_code) for s in info["treatment_steps"]]
            t_prevention  = translate_text(info["prevention"], lang_code)
            t_severity    = translate_text(severity, lang_code)

        # ── Disease Card ──
        sev_class = {
            "Healthy": "severity-low",
            "Low":     "severity-low",
            "Medium":  "severity-medium",
            "High":    "severity-high"
        }.get(severity, "severity-medium")

        st.markdown(f"""
        <div class="card">
            <div class="label-text">Detected Disease</div>
            <div class="disease-badge {sev_class}">{t_disease}</div>
            <br>
            <div style="display:flex; gap:2rem; margin-bottom:0.8rem;">
                <div>
                    <div class="label-text">Severity</div>
                    <div class="value-text {sev_class}" style="font-weight:700;">{t_severity}</div>
                </div>
                <div>
                    <div class="label-text">Confidence</div>
                    <div class="value-text">{confidence*100:.1f}%</div>
                    <div class="confidence-bar-bg">
                        <div class="confidence-bar" style="width:{confidence*100:.1f}%"></div>
                    </div>
                </div>
            </div>
            <div class="label-text">Description</div>
            <div style="color:#c9d1d9; font-size:0.9rem; line-height:1.6;">{t_description}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Top-3 Predictions ──
        with st.expander("📊 Top-3 Predictions"):
            for prob, cls in zip(top_probs, top_classes):
                st.markdown(f"""
                <div style="margin-bottom:0.5rem;">
                    <div style="display:flex; justify-content:space-between; color:#c9d1d9; font-size:0.88rem;">
                        <span>{cls.replace('_',' ').title()}</span>
                        <span>{prob*100:.1f}%</span>
                    </div>
                    <div class="confidence-bar-bg">
                        <div class="confidence-bar" style="width:{prob*100:.1f}%"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # ── Treatment Steps ──
        st.markdown(f"""
        <div class="card">
            <div class="label-text">Treatment Steps</div>
            <div style="margin-top:0.5rem;">
        """, unsafe_allow_html=True)
        for i, step in enumerate(t_steps, 1):
            st.markdown(f'<div class="step-card">{"🔢"} <b>Step {i}:</b> {step}</div>', unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

        # ── Prevention ──
        st.markdown(f"""
        <div class="card">
            <div class="label-text">🛡️ Prevention</div>
            <div style="color:#c9d1d9; font-size:0.9rem; line-height:1.6; margin-top:0.3rem;">{t_prevention}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Voice Readout ──
        if enable_voice:
            with st.spinner("Generating voice readout..."):
                voice_text = (
                    f"{t_disease}. {t_description}. "
                    f"Severity: {t_severity}. "
                    "Treatment steps: " +
                    ". ".join([f"Step {i+1}: {s}" for i, s in enumerate(t_steps)]) +
                    f". Prevention: {t_prevention}"
                )
                try:
                    audio_file = text_to_speech(voice_text, lang_code)
                    st.markdown("#### 🔊 Voice Readout")
                    autoplay_audio(audio_file)
                    os.unlink(audio_file)
                except Exception as e:
                    st.info(f"Voice unavailable for {selected_lang}: {e}")

    elif not uploaded_file:
        st.markdown("""
        <div class="card" style="text-align:center; padding:3rem 1rem;">
            <div style="font-size:4rem;">🌱</div>
            <div style="color:#4ade80; font-family:'Syne',sans-serif; font-size:1.2rem; font-weight:700; margin:0.5rem 0;">Upload a leaf image</div>
            <div style="color:#6b7280; font-size:0.88rem;">
                Take a clear photo of the affected leaf<br>
                and click Analyze to get instant diagnosis.
            </div>
        </div>
        """, unsafe_allow_html=True)
