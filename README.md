# 🌿 LeafDoc AI — Plant Disease Detection System

<p align="center">
  <img src="leafdoc.png" width="100%" alt="LeafDoc AI Application UI">
</p>

A complete AI-powered plant disease detection app built with:
- **EfficientNet-B0** (PyTorch) for image classification
- **PlantVillage dataset** — 38 disease classes across 14 plant species
- **Streamlit** for the web UI
- **googletrans** for multilingual output (14 languages)
- **gTTS** for voice readout of treatment steps

---

## 📁 Project Structure

```
leaf_disease_app/
├── app.py                  ← Main Streamlit application
├── disease_knowledge.py    ← Disease info, treatment steps, prevention tips
├── train_model.py          ← Model training script
├── requirements.txt        ← Python dependencies
├── README.md               ← This file
└── leaf_disease_model.pth  ← Saved model weights (after training)
```

---

## ⚙️ Step 1 — Set Up Environment

### Option A: Conda (Recommended for AIML students)
```bash
# Create a new conda environment
conda create -n leafdoc python=3.10 -y
conda activate leafdoc

# Navigate to project folder
cd leaf_disease_app

# Install dependencies
pip install -r requirements.txt
```

### Option B: venv
```bash
python -m venv leafdoc_env

# Windows
leafdoc_env\Scripts\activate
# Mac/Linux
source leafdoc_env/bin/activate

pip install -r requirements.txt
```

### GPU Support (Optional but faster training)
If you have an NVIDIA GPU:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

---

## 📦 Step 2 — Download the Dataset

### Option A: Kaggle (Recommended)
1. Go to: https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset
2. Download and extract it
3. You should get a folder called `New Plant Diseases Dataset(Augmented)` 
   containing `train` and `valid` subfolders

Use the `train` subfolder as your `--data_dir`:
```
New Plant Diseases Dataset(Augmented)/
└── train/
    ├── Apple___Apple_scab/
    │   ├── image1.JPG
    │   ├── image2.JPG
    │   └── ...
    ├── Apple___healthy/
    ├── Tomato___Late_blight/
    └── ... (38 total class folders)
```

### Option B: PlantVillage on GitHub
```bash
git clone https://github.com/spMohanty/PlantVillage-Dataset.git
# Use the 'color' subfolder
```

---

## 🧠 Step 3 — Train the Model

```bash
# Basic training (15 epochs, recommended)
python train_model.py --data_dir "path/to/train" --epochs 15 --batch_size 32

# If you have a GPU and more VRAM
python train_model.py --data_dir "path/to/train" --epochs 20 --batch_size 64

# If running on CPU only (slower, reduce batch size)
python train_model.py --data_dir "path/to/train" --epochs 10 --batch_size 16
```

### Expected Training Time
| Hardware | Time per Epoch | Total (15 epochs) |
|----------|---------------|-------------------|
| RTX 3060 | ~3–5 min      | ~1 hour           |
| RTX 4090 | ~1–2 min      | ~25 min           |
| CPU only | ~30–60 min    | ~10+ hours        |

### Expected Accuracy
EfficientNet-B0 on PlantVillage typically achieves:
- **Train Accuracy**: 97–99%
- **Validation Accuracy**: 95–98%

### Training Output
After training, you'll see:
```
✅ Training complete! Best Val Accuracy: 97.42%
   Model saved to: leaf_disease_model.pth
```

---

## 🚀 Step 4 — Run the App

```bash
# Make sure you're in the leaf_disease_app directory
cd leaf_disease_app

# Run Streamlit
streamlit run app.py
```

The app opens automatically at: **http://localhost:8501**

---

## 🌐 Features

| Feature | Details |
|---------|---------|
| Disease Detection | 38 classes across 14 plant species |
| Top-3 Predictions | With confidence bars |
| Severity Analysis | Low / Medium / High based on confidence |
| Treatment Steps | Numbered, crop-specific steps |
| Prevention Tips | Season-specific prevention advice |
| Languages | 14 languages including Telugu, Hindi, Tamil, Kannada |
| Voice Readout | Reads treatment steps aloud via gTTS |
| Demo Mode | Works without trained model (random predictions) |

---

## 🌿 Supported Plants & Diseases

| Plant | Diseases Detected |
|-------|------------------|
| Apple | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| Blueberry | Healthy |
| Cherry | Powdery Mildew, Healthy |
| Corn | Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy |
| Grape | Black Rot, Esca, Leaf Blight, Healthy |
| Orange | Huanglongbing (Citrus Greening) |
| Peach | Bacterial Spot, Healthy |
| Pepper | Bacterial Spot, Healthy |
| Potato | Early Blight, Late Blight, Healthy |
| Raspberry | Healthy |
| Soybean | Healthy |
| Squash | Powdery Mildew |
| Strawberry | Leaf Scorch, Healthy |
| Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, TYLCV, Mosaic Virus, Healthy |

---

## 🐛 Troubleshooting

### `ModuleNotFoundError: No module named 'googletrans'`
```bash
pip install googletrans==4.0.0-rc1
```

### Translation not working (HTTPSConnectionPool error)
```bash
# Uninstall and reinstall with specific version
pip uninstall googletrans httpx -y
pip install googletrans==4.0.0-rc1 httpx==0.13.3
```

### `FileNotFoundError` for model
Run the training script first:
```bash
python train_model.py --data_dir "path/to/your/dataset"
```
Or use Demo Mode — the app works without the model (shows random predictions).

### Voice not working for a language
Not all languages are supported by gTTS. Telugu (te), Hindi (hi), Tamil (ta), and most major Indian languages work. If it fails, the app shows a warning without crashing.

### CUDA out of memory
Reduce batch size:
```bash
python train_model.py --data_dir "..." --batch_size 16
```

---

## 🚢 Deploying to Streamlit Cloud (Free Hosting)

1. Push your project to GitHub:
```bash
git init
git add .
git commit -m "LeafDoc AI initial commit"
git remote add origin https://github.com/yourusername/leaf-disease-app.git
git push -u origin main
```

2. Go to **https://share.streamlit.io** and sign in with GitHub

3. Click **"New app"** → Select your repo → Set main file to `app.py`

4. Upload your `leaf_disease_model.pth` to the repo (if under 100MB)
   - If larger, use Git LFS: `git lfs track "*.pth"`

5. Click **Deploy** — your app gets a public URL instantly!

---

## 📖 Model Architecture

```
Input Image (224×224×3)
        ↓
EfficientNet-B0 Backbone (ImageNet pretrained)
   - MBConv blocks with squeeze-and-excitation
   - Progressive scaling of width, depth, resolution
        ↓
Global Average Pooling
        ↓
Dropout (0.2)
        ↓
Linear(1280 → 38)    ← Custom classification head
        ↓
Softmax
        ↓
38-class prediction + confidence scores
```

---

## 🎓 Learning Resources

These concepts from your AIML branch are used in this project:
- **Computer Vision**: CNN, transfer learning, EfficientNet architecture
- **Deep Learning**: Training loop, loss functions, optimizers, schedulers
- **Data Mining**: Data augmentation, train/val split, class distribution analysis
- **ML**: Model evaluation metrics (accuracy, top-k predictions)

---

*Built with ❤️ for 4th Year AIML students*
