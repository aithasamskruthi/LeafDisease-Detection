# disease_knowledge.py
# Full PlantVillage 38-class disease knowledge base

CLASS_NAMES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]

DISEASE_INFO = {

    # ── APPLE ───────────────────────────────────────────────────────────────
    "Apple___Apple_scab": {
        "description": "Apple scab is a fungal disease caused by Venturia inaequalis. It appears as dark, olive-green to brown lesions on leaves and fruits, leading to defoliation and reduced fruit quality.",
        "treatment_steps": [
            "Remove and destroy all fallen infected leaves to reduce fungal spore load.",
            "Apply fungicides containing captan, myclobutanil, or mancozeb at bud break and repeat every 7–10 days during wet weather.",
            "Prune trees to improve air circulation within the canopy.",
            "Avoid overhead irrigation; use drip irrigation to keep foliage dry.",
            "Apply protective sprays before rain events during the primary infection period (spring).",
        ],
        "prevention": "Plant scab-resistant apple varieties. Rake and compost fallen leaves in autumn. Apply dormant sprays of lime sulfur before bud break each year.",
    },
    "Apple___Black_rot": {
        "description": "Black rot is caused by the fungus Botryosphaeria obtusa. It causes circular, brown to black lesions on leaves (frog-eye leaf spot) and shriveled, mummified black fruits.",
        "treatment_steps": [
            "Prune and remove all dead or diseased wood, cankers, and mummified fruits.",
            "Spray copper-based fungicides or thiophanate-methyl from pink stage through cover sprays.",
            "Destroy infected plant debris; do not leave prunings on the ground.",
            "Ensure proper tree nutrition — stressed trees are more susceptible.",
            "Apply fungicide sprays every 10–14 days during the growing season.",
        ],
        "prevention": "Maintain good orchard sanitation. Remove mummified fruits before winter. Avoid wounding trees during pruning when weather is wet.",
    },
    "Apple___Cedar_apple_rust": {
        "description": "Cedar-apple rust is caused by Gymnosporangium juniperi-virginianae, a fungus that requires both apple/crabapple and cedar/juniper trees to complete its life cycle. It produces bright orange spots on apple leaves.",
        "treatment_steps": [
            "Remove nearby juniper or cedar trees that act as alternate hosts, if feasible.",
            "Apply fungicides (myclobutanil, propiconazole, or triadimefon) starting at pink stage and repeat through petal fall.",
            "Remove and destroy infected apple leaves showing orange pustules.",
            "Spray at 7–10 day intervals during wet spring weather.",
            "Monitor and remove gelatinous orange galls on juniper trees in early spring.",
        ],
        "prevention": "Plant rust-resistant apple varieties. Avoid planting apples near eastern red cedars or juniper. Apply preventive fungicides every spring.",
    },
    "Apple___healthy": {
        "description": "The apple leaf appears healthy with no visible signs of disease or pest damage.",
        "treatment_steps": [
            "Continue regular monitoring of the orchard for early signs of disease.",
            "Maintain balanced fertilization based on soil and leaf tissue tests.",
            "Practice good sanitation: remove fallen leaves and fruits promptly.",
            "Ensure adequate irrigation without overwatering.",
            "Apply preventive fungicide program as a seasonal routine.",
        ],
        "prevention": "Keep the orchard clean and well-ventilated. Perform annual pruning to maintain canopy structure. Scout regularly for pests and diseases.",
    },

    # ── BLUEBERRY ────────────────────────────────────────────────────────────
    "Blueberry___healthy": {
        "description": "The blueberry leaf is healthy with no visible disease symptoms.",
        "treatment_steps": [
            "Maintain soil pH between 4.5 and 5.5 for optimal blueberry growth.",
            "Apply mulch around the base to retain moisture and suppress weeds.",
            "Monitor for fungal diseases like mummyberry during wet seasons.",
            "Fertilize with ammonium sulfate for acidic soil nutrition.",
            "Prune old canes after harvest to promote new growth.",
        ],
        "prevention": "Plant disease-resistant varieties. Ensure excellent drainage. Avoid overhead irrigation to reduce foliar disease risk.",
    },

    # ── CHERRY ───────────────────────────────────────────────────────────────
    "Cherry_(including_sour)___Powdery_mildew": {
        "description": "Powdery mildew on cherry is caused by Podosphaera clandestina. It appears as white powdery coatings on young leaves, shoots, and buds, causing leaf distortion and reduced fruit set.",
        "treatment_steps": [
            "Apply sulfur-based fungicides or potassium bicarbonate at first signs of infection.",
            "Use systemic fungicides (myclobutanil, trifloxystrobin) for severe infections.",
            "Remove and destroy heavily infected shoots and leaves.",
            "Improve air circulation by pruning dense canopy growth.",
            "Avoid excess nitrogen fertilization, which promotes susceptible succulent growth.",
        ],
        "prevention": "Plant resistant cherry varieties. Space trees adequately for good air movement. Apply preventive fungicide at bud swell in spring.",
    },
    "Cherry_(including_sour)___healthy": {
        "description": "The cherry leaf appears healthy with no signs of fungal, bacterial, or viral disease.",
        "treatment_steps": [
            "Continue regular scouting for brown rot, leaf spot, and powdery mildew.",
            "Maintain proper irrigation and avoid waterlogging.",
            "Thin fruits if heavily loaded to reduce disease pressure.",
            "Apply balanced fertilizer based on soil test results.",
            "Prune annually to maintain open canopy structure.",
        ],
        "prevention": "Practice good orchard hygiene. Remove mummified fruits. Apply protective fungicide spray program during bloom and post-harvest.",
    },

    # ── CORN ─────────────────────────────────────────────────────────────────
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "description": "Gray leaf spot is caused by Cercospora zeae-maydis. It produces rectangular, gray to tan lesions bounded by leaf veins, which can coalesce and kill large areas of the leaf under high humidity.",
        "treatment_steps": [
            "Apply foliar fungicides (strobilurins like azoxystrobin or triazoles like propiconazole) at tasseling stage.",
            "Plant hybrid corn varieties with genetic resistance to gray leaf spot.",
            "Rotate crops — avoid corn-after-corn in the same field.",
            "Till crop residue after harvest to reduce overwintering inoculum.",
            "Monitor fields weekly from V6 stage onwards during warm, humid conditions.",
        ],
        "prevention": "Use resistant hybrids. Practice 2-year crop rotation with non-host crops. Avoid dense planting that reduces air circulation.",
    },
    "Corn_(maize)___Common_rust_": {
        "description": "Common rust is caused by Puccinia sorghi. It produces small, oval, powdery, brick-red pustules on both surfaces of leaves, reducing photosynthesis and yield under severe infection.",
        "treatment_steps": [
            "Apply fungicides (triazoles, strobilurins) at first signs of rust pustules before tasseling.",
            "Use rust-resistant corn hybrids in rust-prone areas.",
            "Scout fields regularly from the V6 growth stage onwards.",
            "Apply a second fungicide application 14–21 days after first if rust is spreading rapidly.",
            "Avoid late-season planting when conditions favor rust development.",
        ],
        "prevention": "Plant resistant hybrids. Scout early each season. Fungicide application is most effective as a preventive measure before heavy infection.",
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "description": "Northern leaf blight is caused by Exserohilum turcicum. It produces long, cigar-shaped, grayish-green to tan lesions (5–15 cm) on leaves, which may girdle the leaf and cause premature death.",
        "treatment_steps": [
            "Apply fungicides (azoxystrobin, propiconazole) from tasseling through early silking stage.",
            "Plant resistant hybrid varieties with Ht genes.",
            "Rotate crops with non-host species (soybean, small grains) for at least one season.",
            "Incorporate infected crop debris by tillage after harvest.",
            "Scout fields during V6–VT stages; treat when lesions appear on 50% of plants.",
        ],
        "prevention": "Use resistant hybrids as primary management strategy. Crop rotation reduces soilborne inoculum. Avoid overhead irrigation.",
    },
    "Corn_(maize)___healthy": {
        "description": "The corn leaf is healthy with no visible signs of fungal, bacterial, or viral infection.",
        "treatment_steps": [
            "Monitor for common rust, gray leaf spot, and northern leaf blight weekly.",
            "Ensure adequate nitrogen fertilization to maintain plant vigor.",
            "Maintain proper plant population to avoid overcrowding.",
            "Scout for insect pests (corn earworm, aphids) alongside disease monitoring.",
            "Irrigate consistently to prevent moisture stress that can increase disease susceptibility.",
        ],
        "prevention": "Rotate crops annually. Use treated, certified seed. Apply preventive fungicide at tasseling in high-risk areas.",
    },

    # ── GRAPE ────────────────────────────────────────────────────────────────
    "Grape___Black_rot": {
        "description": "Grape black rot is caused by Guignardia bidwellii. It causes circular brown lesions with dark borders on leaves, and shriveled, hard, black mummified berries that remain on the cluster.",
        "treatment_steps": [
            "Apply fungicides (myclobutanil, mancozeb, captan) starting at budbreak and continue every 10–14 days through véraison.",
            "Remove and destroy all mummified berries and infected plant material.",
            "Prune vines to open the canopy and improve air circulation.",
            "Apply sprays preventively before rain events during bloom and fruit set.",
            "Train vines on a trellis system to keep fruit off the ground.",
        ],
        "prevention": "Remove all mummies before bud break. Plant resistant varieties. Maintain a strict spray program from bud break through fruit ripening.",
    },
    "Grape___Esca_(Black_Measles)": {
        "description": "Esca (Black Measles) is a complex vascular disease caused by several wood-rotting fungi. It causes interveinal leaf scorch (tiger-stripe pattern) and dark spots on berries, leading to vine decline.",
        "treatment_steps": [
            "There is no effective curative treatment — focus on cultural management.",
            "Prune infected wood well below visible discoloration into healthy tissue.",
            "Protect pruning wounds immediately with wound sealants or Trichoderma-based biological fungicides.",
            "Remove and destroy severely infected vines to prevent spread.",
            "Avoid pruning during wet conditions to reduce fungal entry through wounds.",
        ],
        "prevention": "Prune during dry weather. Apply wound protectants after every pruning cut. Avoid mechanical damage to vines. Use certified disease-free planting material.",
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "description": "Grape leaf blight (Isariopsis leaf spot) is caused by Isariopsis clavispora (Coniella diplodiella). It produces angular, dark-brown spots on leaves leading to early defoliation.",
        "treatment_steps": [
            "Apply copper-based fungicides or mancozeb at first sign of symptoms.",
            "Remove and dispose of infected leaves and fallen debris.",
            "Improve air circulation through canopy management and shoot positioning.",
            "Apply fungicide sprays every 10–14 days during wet weather.",
            "Avoid overhead irrigation; use drip systems to keep foliage dry.",
        ],
        "prevention": "Maintain good vineyard sanitation. Remove infected leaves during the season. Train vines to ensure good light penetration and air movement.",
    },
    "Grape___healthy": {
        "description": "The grape leaf appears healthy with no signs of fungal, bacterial, or viral disease.",
        "treatment_steps": [
            "Continue regular scouting for downy mildew, powdery mildew, and black rot.",
            "Maintain proper trellising and canopy management throughout the season.",
            "Apply preventive copper or sulfur sprays at key phenological stages.",
            "Monitor for phylloxera and other root and foliar pests.",
            "Ensure balanced nutrition; excess nitrogen promotes disease susceptibility.",
        ],
        "prevention": "Follow an integrated pest management (IPM) program. Maintain open canopy. Use resistant rootstocks where available.",
    },

    # ── ORANGE ───────────────────────────────────────────────────────────────
    "Orange___Haunglongbing_(Citrus_greening)": {
        "description": "Huanglongbing (HLB) or Citrus greening is a devastating bacterial disease caused by Candidatus Liberibacter asiaticus, spread by the Asian citrus psyllid. It causes yellow mottling of leaves (blotchy mottle), small misshapen fruits, and eventual tree death.",
        "treatment_steps": [
            "There is currently no cure. Immediately remove and destroy infected trees to prevent spread.",
            "Control Asian citrus psyllid (vector) with systemic insecticides (imidacloprid) applied to soil or foliar sprays.",
            "Apply nutritional spray programs (foliar micronutrients) to extend the productive life of mildly infected trees.",
            "Monitor psyllid populations with yellow sticky traps throughout the grove.",
            "Report suspected HLB to local agricultural authorities immediately.",
        ],
        "prevention": "Use certified HLB-free nursery stock. Install psyllid monitoring traps. Apply systemic insecticides preventively. Quarantine plant material from affected areas.",
    },

    # ── PEACH ────────────────────────────────────────────────────────────────
    "Peach___Bacterial_spot": {
        "description": "Bacterial spot of peach is caused by Xanthomonas arboricola pv. pruni. It causes water-soaked lesions on leaves that turn brown and fall out (shot-hole appearance), and raised, scab-like spots on fruit.",
        "treatment_steps": [
            "Apply copper-based bactericides (copper hydroxide, copper sulfate) from shuck split through cover sprays every 7–10 days.",
            "Use oxytetracycline sprays during bloom and early fruit development where permitted.",
            "Remove and destroy severely infected twigs and branches during dormant pruning.",
            "Avoid overhead irrigation; use drip or micro-sprinkler systems.",
            "Reduce tree stress through proper irrigation and balanced fertilization.",
        ],
        "prevention": "Plant resistant peach varieties. Avoid sites with frequent summer rains. Maintain good air circulation through annual pruning.",
    },
    "Peach___healthy": {
        "description": "The peach leaf appears healthy with no signs of bacterial or fungal disease.",
        "treatment_steps": [
            "Scout regularly for bacterial spot, leaf curl, and brown rot.",
            "Apply dormant copper spray before bud break each year.",
            "Maintain proper irrigation to prevent drought stress.",
            "Fertilize according to leaf and soil test recommendations.",
            "Thin fruits to reduce disease incidence and improve fruit size.",
        ],
        "prevention": "Plant resistant varieties. Maintain open tree structure for air circulation. Follow a preventive spray calendar each season.",
    },

    # ── PEPPER ───────────────────────────────────────────────────────────────
    "Pepper,_bell___Bacterial_spot": {
        "description": "Bacterial spot of pepper is caused by Xanthomonas vesicatoria. It causes small, water-soaked lesions on leaves that turn brown with yellow halos, leading to defoliation and scabby fruit spots.",
        "treatment_steps": [
            "Apply copper-based bactericides (copper hydroxide + mancozeb) every 5–7 days during wet weather.",
            "Remove and destroy infected plant debris and avoid working in wet fields.",
            "Use drip irrigation instead of overhead irrigation to minimize leaf wetness.",
            "Apply copper sprays starting at transplanting and continue preventively.",
            "Avoid excessive nitrogen fertilization that promotes lush, susceptible growth.",
        ],
        "prevention": "Use certified disease-free seed or transplants. Treat seed with hot water (52°C for 30 minutes) before planting. Rotate crops with non-solanaceous plants for 2–3 years.",
    },
    "Pepper,_bell___healthy": {
        "description": "The bell pepper leaf appears healthy with no visible disease symptoms.",
        "treatment_steps": [
            "Monitor regularly for bacterial spot, phytophthora blight, and anthracnose.",
            "Maintain consistent soil moisture with drip irrigation.",
            "Apply balanced fertilizer; avoid excess nitrogen.",
            "Scout for aphids and thrips that can vector viral diseases.",
            "Stake or cage plants to keep foliage off the ground.",
        ],
        "prevention": "Rotate crops every 2–3 years. Use resistant varieties. Maintain good field sanitation. Apply preventive copper sprays during the rainy season.",
    },

    # ── POTATO ───────────────────────────────────────────────────────────────
    "Potato___Early_blight": {
        "description": "Early blight is caused by Alternaria solani. It produces dark-brown, target-shaped (concentric ring) lesions on older leaves first, leading to yellowing, defoliation, and yield loss under severe infection.",
        "treatment_steps": [
            "Apply fungicides (chlorothalonil, mancozeb, azoxystrobin) at first appearance of symptoms.",
            "Begin fungicide program when plants are 15–20 cm tall and continue every 7–14 days.",
            "Remove and destroy infected lower leaves to slow disease spread.",
            "Avoid water stress through consistent irrigation — stressed plants are more susceptible.",
            "Apply potassium fertilizer to improve plant resistance to early blight.",
        ],
        "prevention": "Plant certified disease-free seed potatoes. Rotate crops with non-solanaceous plants for 2–3 years. Use resistant varieties. Avoid overhead irrigation.",
    },
    "Potato___Late_blight": {
        "description": "Late blight is caused by Phytophthora infestans — the pathogen responsible for the Irish Potato Famine. It produces water-soaked, oily-looking lesions on leaves with white sporulation on the underside, rapidly destroying entire fields under cool, wet conditions.",
        "treatment_steps": [
            "Apply fungicides (chlorothalonil, metalaxyl, cymoxanil, mancozeb) immediately at first sign of symptoms or when weather conditions are favorable.",
            "Spray preventively every 5–7 days during cool, wet weather (temperature 10–20°C with high humidity).",
            "Destroy infected plant material immediately; do not compost.",
            "Hill potato rows to protect tubers from infected foliage and soil splash.",
            "Harvest tubers as soon as vines die; do not store infected tubers.",
        ],
        "prevention": "Plant certified seed potatoes from clean stock. Use resistant varieties. Destroy volunteer potato plants and nightshade weeds. Monitor weather-based blight forecasting tools.",
    },
    "Potato___healthy": {
        "description": "The potato leaf appears healthy with no signs of early blight, late blight, or other common diseases.",
        "treatment_steps": [
            "Scout weekly for late blight symptoms, especially during cool and wet weather.",
            "Maintain optimal plant nutrition with balanced NPK fertilization.",
            "Hill rows at the appropriate growth stage to protect developing tubers.",
            "Apply preventive fungicide sprays when weather conditions favor blight development.",
            "Remove and destroy any volunteer potato plants that can harbor disease.",
        ],
        "prevention": "Use certified seed potatoes. Rotate with non-solanaceous crops every 3–4 years. Apply preventive fungicide program during the growing season.",
    },

    # ── RASPBERRY ────────────────────────────────────────────────────────────
    "Raspberry___healthy": {
        "description": "The raspberry leaf appears healthy with no visible signs of fungal or viral disease.",
        "treatment_steps": [
            "Scout regularly for spur blight, cane blight, and anthracnose.",
            "Prune out old, fruited floricanes after harvest.",
            "Maintain proper trellis structure for good air circulation.",
            "Apply copper or lime sulfur sprays during dormancy.",
            "Monitor for raspberry mosaic virus spread by aphids.",
        ],
        "prevention": "Plant certified virus-free stock. Remove old canes promptly after fruiting. Apply preventive fungicide program in spring.",
    },

    # ── SOYBEAN ──────────────────────────────────────────────────────────────
    "Soybean___healthy": {
        "description": "The soybean leaf appears healthy with no disease symptoms.",
        "treatment_steps": [
            "Scout fields regularly for sudden death syndrome, frogeye leaf spot, and SCN.",
            "Maintain proper row spacing for good air circulation.",
            "Apply seed inoculant with Bradyrhizobium for nitrogen fixation.",
            "Monitor for soybean aphids and bean leaf beetles that vector viruses.",
            "Apply foliar fungicide at R3 growth stage in high-yield environments.",
        ],
        "prevention": "Plant certified seed with seed treatments. Use resistant varieties. Rotate with corn or wheat. Maintain soil health with proper lime and phosphorus management.",
    },

    # ── SQUASH ───────────────────────────────────────────────────────────────
    "Squash___Powdery_mildew": {
        "description": "Powdery mildew on squash is caused by Podosphaera xanthii and Erysiphe cichoracearum. It appears as white powdery patches on leaf surfaces, eventually covering entire leaves and causing premature aging.",
        "treatment_steps": [
            "Apply potassium bicarbonate, neem oil, or sulfur-based fungicides at first sign of white powdery patches.",
            "Use systemic fungicides (myclobutanil, trifloxystrobin) for severe infections.",
            "Remove heavily infected leaves to reduce spore load.",
            "Avoid overhead irrigation; keep foliage dry.",
            "Spray every 7–10 days, alternating fungicide modes of action to prevent resistance.",
        ],
        "prevention": "Plant resistant squash varieties. Space plants adequately for air circulation. Avoid excessive nitrogen fertilization. Plant in full sun locations.",
    },

    # ── STRAWBERRY ───────────────────────────────────────────────────────────
    "Strawberry___Leaf_scorch": {
        "description": "Strawberry leaf scorch is caused by Diplocarpon earlianum. It produces small, irregular, purple to dark-brown spots on leaves that coalesce, causing the leaf to look scorched or burned.",
        "treatment_steps": [
            "Apply fungicides (captan, thiram, or myclobutanil) at the first sign of symptoms.",
            "Remove and destroy infected leaves immediately.",
            "Renovate bed after harvest by mowing foliage and applying fungicide.",
            "Avoid overhead irrigation; use drip irrigation to reduce leaf wetness.",
            "Apply fungicide every 7–10 days during wet weather.",
        ],
        "prevention": "Plant certified disease-free transplants. Use resistant varieties. Renovate strawberry beds annually. Ensure good drainage and air circulation.",
    },
    "Strawberry___healthy": {
        "description": "The strawberry leaf appears healthy with no signs of leaf scorch, gray mold, or other common diseases.",
        "treatment_steps": [
            "Monitor regularly for botrytis gray mold, especially during fruiting in wet weather.",
            "Remove dead leaves and old runners to improve air circulation.",
            "Apply preventive fungicide program from bloom through harvest.",
            "Fertilize according to soil test — balanced nutrition reduces susceptibility.",
            "Replace beds every 2–3 years to reduce disease buildup.",
        ],
        "prevention": "Plant certified stock. Maintain proper bed renovation. Avoid excessive nitrogen. Apply mulch to prevent soil splash onto foliage.",
    },

    # ── TOMATO ───────────────────────────────────────────────────────────────
    "Tomato___Bacterial_spot": {
        "description": "Bacterial spot of tomato is caused by Xanthomonas vesicatoria. It causes small, water-soaked, dark lesions on leaves with yellow halos, and raised, scabby spots on fruits that reduce market value.",
        "treatment_steps": [
            "Apply copper-based bactericides (copper hydroxide) mixed with mancozeb every 5–7 days.",
            "Begin sprays at transplanting and continue preventively through the season.",
            "Remove infected plant parts and avoid working in wet fields.",
            "Use drip irrigation to minimize leaf wetness duration.",
            "Avoid wounding plants during field operations.",
        ],
        "prevention": "Use certified disease-free seed. Treat seed with hot water (52°C for 25 minutes). Rotate crops with non-solanaceous plants for 2–3 years. Plant resistant varieties.",
    },
    "Tomato___Early_blight": {
        "description": "Early blight on tomato is caused by Alternaria solani. It produces dark, concentric-ringed 'bull's-eye' lesions on older lower leaves, causing yellowing, defoliation, and reduced fruit production.",
        "treatment_steps": [
            "Apply fungicides (chlorothalonil, mancozeb, azoxystrobin) at first symptom appearance.",
            "Remove infected lower leaves when first lesions appear.",
            "Maintain adequate plant nutrition — potassium-deficient plants are more susceptible.",
            "Apply organic mulch to prevent soil-splash onto lower leaves.",
            "Spray every 7–10 days during wet, warm conditions.",
        ],
        "prevention": "Use resistant varieties. Rotate crops with non-solanaceous plants. Avoid overhead irrigation. Stake or cage tomatoes to keep foliage off the ground.",
    },
    "Tomato___Late_blight": {
        "description": "Late blight on tomato is caused by Phytophthora infestans. It produces large, water-soaked lesions on leaves and stems with a white fuzzy mold on undersides, rapidly killing entire plants in cool, wet conditions.",
        "treatment_steps": [
            "Apply fungicides (chlorothalonil, cymoxanil + mancozeb, or fluopicolide) immediately upon detection.",
            "Spray every 5–7 days during wet, cool weather conditions.",
            "Remove and bag all infected plant material — do not compost.",
            "Destroy heavily infected crops immediately to protect neighboring fields.",
            "Never save seed from infected plants.",
        ],
        "prevention": "Use certified, disease-free transplants. Avoid planting near potatoes. Apply preventive fungicide program during cool, wet seasons. Monitor local late blight forecasting networks.",
    },
    "Tomato___Leaf_Mold": {
        "description": "Tomato leaf mold is caused by Passalora fulva (formerly Cladosporium fulvum). It produces pale-green to yellow patches on upper leaf surfaces with olive-green to grayish-brown velvety mold on lower surfaces, thriving in humid greenhouse conditions.",
        "treatment_steps": [
            "Improve ventilation immediately by opening vents and reducing plant spacing.",
            "Apply fungicides (chlorothalonil, mancozeb, or difenoconazole) every 7–10 days.",
            "Remove and destroy infected leaves.",
            "Reduce relative humidity below 85% by improving airflow in greenhouses.",
            "Avoid wetting foliage during irrigation; use drip irrigation.",
        ],
        "prevention": "Use resistant varieties with Cf resistance genes. Maintain greenhouse humidity below 85%. Space plants for good air circulation. Avoid overcrowding.",
    },
    "Tomato___Septoria_leaf_spot": {
        "description": "Septoria leaf spot is caused by Septoria lycopersici. It produces numerous small, circular spots with gray-white centers and dark borders on lower leaves, causing rapid defoliation from the bottom up.",
        "treatment_steps": [
            "Apply fungicides (chlorothalonil, mancozeb, copper-based products) at first sign of symptoms.",
            "Remove and destroy infected lower leaves.",
            "Mulch around plants to prevent soil splash.",
            "Avoid overhead irrigation; use drip irrigation.",
            "Spray every 7–10 days, especially during warm, wet weather.",
        ],
        "prevention": "Use certified, disease-free seed and transplants. Rotate crops. Stake tomatoes to improve air circulation. Avoid touching plants when foliage is wet.",
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "description": "Two-spotted spider mites (Tetranychus urticae) cause stippled, bronzed, or yellowed leaves with fine webbing on undersides. Severe infestations cause leaf drop and plant death, especially in hot, dry conditions.",
        "treatment_steps": [
            "Apply miticides (abamectin, bifenazate, or spiromesifen) — rotate modes of action to prevent resistance.",
            "Apply insecticidal soap or neem oil for organic management.",
            "Use a strong stream of water to knock mites off foliage.",
            "Release predatory mites (Phytoseiulus persimilis) for biological control.",
            "Avoid broad-spectrum insecticides that kill natural predators of spider mites.",
        ],
        "prevention": "Maintain adequate soil moisture — drought-stressed plants attract spider mites. Monitor the underside of leaves weekly. Avoid dusty conditions around plants.",
    },
    "Tomato___Target_Spot": {
        "description": "Target spot is caused by Corynespora cassiicola. It produces circular lesions with concentric rings (target pattern) on leaves, stems, and fruits, leading to premature defoliation under high humidity.",
        "treatment_steps": [
            "Apply fungicides (azoxystrobin, difenoconazole, or chlorothalonil) at first appearance of lesions.",
            "Remove infected leaves and crop debris.",
            "Improve canopy ventilation through proper spacing and pruning.",
            "Apply sprays every 7–14 days during wet conditions.",
            "Avoid overhead irrigation.",
        ],
        "prevention": "Use resistant varieties where available. Rotate crops with non-solanaceous plants. Practice good field sanitation.",
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "description": "Tomato Yellow Leaf Curl Virus (TYLCV) is a begomovirus transmitted by silverleaf whitefly (Bemisia tabaci). It causes severe yellowing and curling of young leaves, stunted growth, and complete yield failure if infection occurs early.",
        "treatment_steps": [
            "There is no cure. Remove and destroy infected plants immediately to prevent spread.",
            "Control whitefly vector with insecticides (imidacloprid, thiamethoxam) applied to soil or foliar.",
            "Use yellow sticky traps to monitor and reduce whitefly populations.",
            "Install reflective mulch to deter whitefly landings.",
            "Use insect-proof nets in greenhouse production.",
        ],
        "prevention": "Plant TYLCV-resistant varieties. Control whitefly populations before planting. Remove weeds that host whiteflies. Use certified virus-free transplants.",
    },
    "Tomato___Tomato_mosaic_virus": {
        "description": "Tomato Mosaic Virus (ToMV) causes a mosaic pattern of light and dark green on leaves, leaf distortion, stunted growth, and internal fruit browning. It is mechanically transmitted through infected hands, tools, and plant debris.",
        "treatment_steps": [
            "There is no cure. Remove and destroy infected plants.",
            "Disinfect all tools, stakes, and equipment with 10% bleach solution.",
            "Wash hands thoroughly with soap before and after handling plants.",
            "Do not use tobacco products while handling tomato plants — tobacco can carry TMV.",
            "Control aphids that can spread virus mechanically.",
        ],
        "prevention": "Use certified virus-free seed and transplants. Plant resistant varieties (Tm2 gene). Practice strict hygiene during all field operations. Avoid replanting in infected soil without crop rotation.",
    },
    "Tomato___healthy": {
        "description": "The tomato leaf appears healthy with no signs of fungal, bacterial, or viral disease.",
        "treatment_steps": [
            "Scout weekly for early blight, late blight, bacterial spot, and whiteflies.",
            "Maintain consistent irrigation — avoid drought stress that increases disease susceptibility.",
            "Apply balanced fertilizer; avoid excess nitrogen that promotes lush, susceptible growth.",
            "Stake or cage plants to keep foliage and fruits off the ground.",
            "Apply preventive fungicide program during warm, wet weather.",
        ],
        "prevention": "Rotate crops every 2–3 years. Use certified transplants. Mulch to prevent soil splash. Scout fields twice weekly during the peak growing season.",
    },

    # ── DEFAULT FALLBACK ─────────────────────────────────────────────────────
    "__default__": {
        "description": "A disease or condition has been detected on this leaf. Further analysis may be required. Please consult a local agricultural extension officer with the image for precise identification.",
        "treatment_steps": [
            "Isolate the affected plant to prevent potential spread to healthy plants.",
            "Remove and destroy visibly infected leaves or plant parts.",
            "Improve air circulation around plants by spacing them properly.",
            "Avoid overhead watering to reduce leaf wetness.",
            "Consult a local agricultural extension service or plant pathologist for precise diagnosis.",
        ],
        "prevention": "Maintain good field sanitation. Use certified disease-free planting material. Practice crop rotation. Monitor plants regularly for early symptoms.",
    },
}
