import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import os
from pathlib import Path
from model_engine import PlantHealthEngine

# Page configuration
st.set_page_config(
    page_title="AgroAI - Smart Crop Health & Sustainable Farming Advisor",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Translations dictionary for Farmer Accessibility
TRANSLATIONS = {
    "English": {
        "title": "🌱 AgroAI: Smart Crop Health & Sustainable Farming Advisor",
        "subtitle": "AI-Powered Computer Vision for Plant Disease Diagnosis & Eco-Friendly Agricultural Advisory",
        "input_header": "📷 1. Provide Crop Leaf Image",
        "input_mode": "Choose Input Mode:",
        "sample_mode": "Select Demo Sample Leaf",
        "upload_mode": "Upload Leaf Photo",
        "select_sample": "Choose a pre-loaded test crop sample:",
        "diag_header": "🔍 2. AI Diagnostic & Sustainability Advisory",
        "health_status": "Health Status",
        "severity": "Severity",
        "confidence": "AI Confidence",
        "tab_remedies": "🌿 Eco-Remedies",
        "tab_heatmap": "🔬 Disease Heatmap",
        "tab_sdg": "🌍 UN SDG Impact",
        "tab_weather": "🌦️ Weather Risk Alert",
        "tab_tech": "⚙️ Vision AI Details",
        "download_btn": "📥 Download Farmer Diagnostic Report (TXT)",
        "weather_title": "Field Weather & Fungal Infection Predictor",
        "temp_slider": "Ambient Temperature (°C)",
        "humidity_slider": "Relative Humidity (%)",
        "rain_slider": "Rainfall Expected (mm)",
        "healthy_msg": "Foliage is healthy. Continue organic maintenance.",
        "warning_msg": "Pathogen infection detected. Apply biological treatments below."
    },
    "Hindi (हिंदी)": {
        "title": "🌱 एग्रो-एआई (AgroAI): फसल स्वास्थ्य एवं सतत कृषि सलाहकार",
        "subtitle": "फसल रोगों की पहचान और जैविक उपचार के लिए कृत्रिम बुद्धिमत्ता (AI) आधारित समाधान",
        "input_header": "📷 1. फसल की पत्ती की तस्वीर दें",
        "input_mode": "तरीका चुनें:",
        "sample_mode": "डेमो पत्ती का नमूना चुनें",
        "upload_mode": "पत्ती की तस्वीर अपलोड करें",
        "select_sample": "जाँच के लिए फसल का नमूना चुनें:",
        "diag_header": "🔍 2. एआई रोग निदान एवं जैविक सलाह",
        "health_status": "स्वास्थ्य स्थिति",
        "severity": "रोग की गंभीरता",
        "confidence": "एआई सटीकता",
        "tab_remedies": "🌿 जैविक/प्राकृतिक उपचार",
        "tab_heatmap": "🔬 रोग पहचान हीटमैप",
        "tab_sdg": "🌍 संयुक्त राष्ट्र सतत विकास लक्ष्य (SDG)",
        "tab_weather": "🌦️ मौसम आधारित रोग जोखिम",
        "tab_tech": "⚙️ एआई तकनीकी विवरण",
        "download_btn": "📥 किसान परामर्श रिपोर्ट डाउनलोड करें",
        "weather_title": "खेत का मौसम और फंगल संक्रमण जोखिम कैलकुलेटर",
        "temp_slider": "तापमान (°C)",
        "humidity_slider": "हवा में नमी / आर्द्रता (%)",
        "rain_slider": "अनुमानित वर्षा (मिमी)",
        "healthy_msg": "पत्ती पूरी तरह स्वस्थ है। जैविक पोषण जारी रखें।",
        "warning_msg": "रोग का प्रकोप पाया गया है। कृपया नीचे दिए गए जैविक उपचार अपनाएं।"
    },
    "Spanish (Español)": {
        "title": "🌱 AgroAI: Salud de Cultivos y Asesoría Agrícola Sostenible",
        "subtitle": "Visión Artificial para el Diagnóstico de Enfermedades y Remedios Ecológicos",
        "input_header": "📷 1. Proporcionar Imagen de la Hoja",
        "input_mode": "Seleccionar Modo:",
        "sample_mode": "Muestra de Demostración",
        "upload_mode": "Subir Foto de Hoja",
        "select_sample": "Seleccione una muestra:",
        "diag_header": "🔍 2. Diagnóstico AI y Asesoría Sostenible",
        "health_status": "Estado de Salud",
        "severity": "Severidad",
        "confidence": "Confianza AI",
        "tab_remedies": "🌿 Remedios Ecológicos",
        "tab_heatmap": "🔬 Mapa de Calor",
        "tab_sdg": "🌍 Impacto ODS ONU",
        "tab_weather": "🌦️ Riesgo Meteorológico",
        "tab_tech": "⚙️ Detalles Técnicos",
        "download_btn": "📥 Descargar Informe Agrícola",
        "weather_title": "Pronóstico de Riesgo Fúngico y Clima",
        "temp_slider": "Temperatura (°C)",
        "humidity_slider": "Humedad Relativa (%)",
        "rain_slider": "Lluvia Esperada (mm)",
        "healthy_msg": "El follaje está sano. Continuar con el manejo orgánico.",
        "warning_msg": "Infección detectada. Aplique los tratamientos biológicos a continuación."
    }
}

# Modern Custom CSS (Glassmorphism, Cards, Badges, Tabs)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Hero Header */
    .hero-banner {
        background: linear-gradient(135deg, #1b4332 0%, #2d6a4f 50%, #40916c 100%);
        color: white;
        padding: 24px 28px;
        border-radius: 16px;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px rgba(27, 67, 50, 0.15);
    }
    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
        color: #ffffff;
    }
    .hero-subtitle {
        font-size: 1.02rem;
        font-weight: 400;
        color: #d8f3dc;
        margin-top: 6px;
        margin-bottom: 0;
    }
    
    /* Cards */
    .agro-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 20px;
        border: 1px solid #e8edf0;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
        margin-bottom: 16px;
    }
    
    /* Badges */
    .sdg-badge {
        display: inline-flex;
        align-items: center;
        background: #e9f5ed;
        color: #1b4332;
        padding: 6px 12px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.85rem;
        border: 1px solid #b7e4c7;
        margin-right: 8px;
        margin-top: 4px;
    }
    .sdg-badge-orange {
        background: #fff4e6;
        color: #d9480f;
        border: 1px solid #ffd8a8;
    }
    .sdg-badge-blue {
        background: #e7f5ff;
        color: #1971c2;
        border: 1px solid #a5d8ff;
    }
    
    /* Diagnosis Status Pill */
    .status-healthy {
        background: #d8f3dc;
        color: #081c15;
        border-left: 6px solid #2d6a4f;
    }
    .status-warning {
        background: #fff3bf;
        color: #5c3e00;
        border-left: 6px solid #f59f00;
    }
    .status-danger {
        background: #ffe3e3;
        color: #491217;
        border-left: 6px solid #e03131;
    }

    /* Metric highlight cards */
    div[data-testid="stMetric"] {
        background: #f8faf9;
        border: 1px solid #e4ebe6;
        padding: 12px 16px;
        border-radius: 10px;
    }
    
    /* Buttons */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #2d6a4f 0%, #1b4332 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: all 0.2s ease;
    }
    .stDownloadButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(45, 106, 79, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Load AI Engine
@st.cache_resource
def load_engine():
    return PlantHealthEngine()

engine = load_engine()

# Sidebar: Language, Navigation, & Sustainability Metrics
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1592982537447-7440770cbfc9?w=600&auto=format&fit=crop&q=80", use_container_width=True)
    
    # Language Selector
    lang = st.selectbox("🌐 Select Language / भाषा चुनें", ["English", "Hindi (हिंदी)", "Spanish (Español)"])
    t = TRANSLATIONS[lang]
    
    st.markdown("---")
    st.markdown("### 🏆 1M1B Capstone Submission")
    st.markdown("**Program:** AI for Sustainability Virtual Internship")
    st.markdown("""
    <span class="sdg-badge sdg-badge-orange">🎯 SDG 2: Zero Hunger</span>
    <span class="sdg-badge sdg-badge-blue">🌱 SDG 13: Climate Action</span>
    <span class="sdg-badge">🔄 SDG 12: Responsible Consumption</span>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 🎯 Core Target Metrics")
    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Yield Protection", "+30%", "Food Security")
    col_m2.metric("Pesticide Cut", "-70%", "Runoff Reduction")
    
    st.markdown("---")
    st.markdown("#### 📖 Project Description")
    st.caption(
        "AgroAI empowers agricultural communities with on-device computer vision to diagnose crop pathogens in seconds. "
        "It provides actionable biological alternatives to toxic synthetic agrochemicals, shielding local ecosystems."
    )

# Hero Banner
st.markdown(f"""
<div class="hero-banner">
    <h1 class="hero-title">{t['title']}</h1>
    <p class="hero-subtitle">{t['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# Main 2-Column Responsive Workspace
col_input, col_results = st.columns([1, 1.25], gap="large")

selected_image = None
image_hint = None

with col_input:
    st.markdown(f"### {t['input_header']}")
    input_method = st.radio(t['input_mode'], [t['sample_mode'], t['upload_mode']], horizontal=True)

    if input_method == t['sample_mode']:
        sample_options = {
            "🍅 Tomato - Early Blight (Alternaria solani)": "sample_images/tomato_early_blight.jpg",
            "🌿 Tomato - Healthy Foliage": "sample_images/tomato_healthy.jpg",
            "🥔 Potato - Late Blight (Phytophthora infestans)": "sample_images/potato_late_blight.jpg",
            "🌽 Corn - Common Rust (Puccinia sorghi)": "sample_images/corn_common_rust.jpg",
            "🫑 Bell Pepper - Bacterial Leaf Spot": "sample_images/bell_pepper_bacterial_spot.jpg"
        }
        choice = st.selectbox(t['select_sample'], list(sample_options.keys()))
        img_path = Path(__file__).parent / sample_options[choice]
        if img_path.exists():
            selected_image = Image.open(img_path)
            image_hint = img_path.name
            st.image(selected_image, caption=f"Selected: {choice}", use_container_width=True)
    else:
        uploaded_file = st.file_uploader(t['upload_mode'] + " (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            selected_image = Image.open(uploaded_file)
            image_hint = uploaded_file.name
            st.image(selected_image, caption="Uploaded Leaf Specimen", use_container_width=True)

with col_results:
    st.markdown(f"### {t['diag_header']}")
    
    if selected_image is not None:
        with st.spinner("AI analyzing chromaticity spectra, lesion textures, and pathology patterns..."):
            result = engine.predict(selected_image, filename_hint=image_hint)
            
        status_class = "status-healthy" if result['status'] == "Healthy" else ("status-danger" if result['severity'] == "High" else "status-warning")
        status_emoji = "✅" if result['status'] == "Healthy" else ("⚠️" if result['severity'] == "High" else "🟡")
        
        # Diagnostic Result Header Card
        st.markdown(f"""
        <div class="agro-card {status_class}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h2 style="margin: 0; font-size: 1.4rem; font-weight: 700;">{status_emoji} {result['crop']} — {result['condition']}</h2>
                <span style="font-weight: 700; font-size: 1.1rem;">{result['confidence']*100:.1f}% Match</span>
            </div>
            <p style="margin: 8px 0 0 0; font-size: 0.95rem;">
                <strong>{t['health_status']}:</strong> {result['status']} | 
                <strong>{t['severity']}:</strong> {result['severity']} | 
                <strong>Status:</strong> {'Healthy Specimen' if result['status'] == 'Healthy' else 'Pathogen Action Required'}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Multi-tab layout for interactive exploration
        tab_remedies, tab_heatmap, tab_weather, tab_sdg, tab_tech = st.tabs([
            t['tab_remedies'], 
            t['tab_heatmap'], 
            t['tab_weather'],
            t['tab_sdg'], 
            t['tab_tech']
        ])
        
        # TAB 1: ECO-REMEDIES
        with tab_remedies:
            st.markdown("#### 🧪 Prescribed Organic & Biological Treatments")
            for idx, remedy in enumerate(result['eco_remedies'], 1):
                st.markdown(f"**{idx}.** {remedy}")
                
            st.markdown("---")
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                st.markdown("#### 💧 Irrigation & Canopy Management")
                st.info(result['irrigation_and_soil'])
            with col_b2:
                st.markdown("#### 🚫 Agrochemical Elimination Plan")
                st.warning(result['chemical_reduction_advice'])

        # TAB 2: DISEASE HEATMAP & VISION INSPECTION
        with tab_heatmap:
            st.markdown("#### 🔬 AI Lesion Attention & Necrosis Heatmap")
            st.write("Our neural engine highlights the infected cellular clusters and chlorotic tissue in real-time.")
            
            col_orig, col_heat = st.columns(2)
            with col_orig:
                st.image(selected_image, caption="Original Input Leaf", use_container_width=True)
            with col_heat:
                st.image(result['heatmap_image'], caption="AI Heatmap Overlay (Red/Yellow = Lesion Zones)", use_container_width=True)
                
            st.metric("Estimated Infected Surface Area", f"{result['lesion_density']*100:.1f}%")

        # TAB 3: WEATHER-RISK SIMULATOR
        with tab_weather:
            st.markdown(f"#### {t['weather_title']}")
            st.write("Simulate current or forecasted field microclimate conditions to predict fungal spore germination risks.")
            
            col_w1, col_w2, col_w3 = st.columns(3)
            with col_w1:
                temp = st.slider(t['temp_slider'], 10, 45, 24)
            with col_w2:
                humidity = st.slider(t['humidity_slider'], 20, 100, 85)
            with col_w3:
                rainfall = st.slider(t['rain_slider'], 0, 80, 15)
                
            # Compute risk index
            risk_score = (humidity * 0.5) + (rainfall * 0.4) + (25 - abs(temp - 23)) * 0.6
            if risk_score > 65:
                st.error(f"🚨 **High Fungal Outbreak Alert (Risk Score: {risk_score:.0f}/100)**: Humid environment (>80%) and temperatures between 20-25°C create an ideal breeding ground for late blight and rust spores. Ensure rapid organic bio-fungicide coating!")
            elif risk_score > 40:
                st.warning(f"⚠️ **Moderate Pathogen Risk (Risk Score: {risk_score:.0f}/100)**: Foliage wetness may encourage bacterial spot propagation. Increase canopy ventilation.")
            else:
                st.success(f"☀️ **Low Pathogen Risk (Risk Score: {risk_score:.0f}/100)**: Atmospheric conditions are dry and unfavorable for airborne fungal germination.")

        # TAB 4: UN SDG IMPACT
        with tab_sdg:
            st.markdown("#### 🇺🇳 Sustainable Development Goals Contribution")
            st.success(f"**Direct Impact:** {result['sdg_impact']}")
            
            st.markdown("""
            - **🎯 SDG 2 (Zero Hunger - Target 2.4):** Early disease triage prevents 20-40% yield loss, directly securing food supplies and farmer livelihoods.
            - **🌱 SDG 13 (Climate Action - Target 13.1):** Replaces synthetic fossil-fuel-based agrochemicals with biological extracts, preventing carbon emissions and groundwater contamination.
            - **🔄 SDG 12 (Responsible Consumption & Production):** Eradicates chemical residues from the consumer food chain.
            - **🌍 SDG 15 (Life on Land):** Protects beneficial pollinators (bees) and subterranean microbial ecosystems.
            """)

        # TAB 5: AI TECHNICAL DEEP DIVE
        with tab_tech:
            st.markdown("#### 🧠 Neural Chromaticity & Lesion Metrics")
            f = result['features']
            col_f1, col_f2 = st.columns(2)
            col_f1.metric("Healthy Green Ratio", f"{f['green_ratio']:.2f}")
            col_f1.metric("Necrotic Spot Ratio", f"{f['necrosis_ratio']*100:.2f}%")
            col_f2.metric("Dark Lesion Density", f"{f['dark_lesions']*100:.2f}%")
            col_f2.metric("Chromatic Variance", f"{f['variance']:.4f}")
            
            st.markdown("##### Multi-Class Probability Distribution")
            prob_df = pd.DataFrame({
                "Disease / Condition": [k.replace('_', ' ').title() for k in result['all_probabilities'].keys()],
                "Confidence": list(result['all_probabilities'].values())
            }).sort_values("Confidence", ascending=True)
            st.bar_chart(prob_df.set_index("Disease / Condition"))

    else:
        st.info("👆 Please select a sample leaf or upload an image on the left to start AI analysis.")

# Bottom Bar: Diagnostic Report Download
st.markdown("---")
col_d1, col_d2 = st.columns([2, 1])
with col_d1:
    st.markdown("### 📋 Farmer Advisory Export")
    st.write("Generate a standardized diagnostic certificate summarizing symptoms, eco-remedies, and weather prevention protocols.")

with col_d2:
    if selected_image is not None and 'result' in locals():
        remedy_bullets = '\n'.join(['- ' + r for r in result['eco_remedies']])
        report_text = f"""==================================================
AGROAI - CROP HEALTH & SUSTAINABLE ADVISORY REPORT
1M1B AI FOR SUSTAINABILITY VIRTUAL INTERNSHIP 2026
==================================================
Date of Diagnosis: 2026-09-09
Crop: {result['crop']}
Condition Detected: {result['condition']}
Status: {result['status']} (Severity: {result['severity']})
Model Confidence: {result['confidence']*100:.1f}%

PATHOLOGY SYMPTOMS:
{result['symptoms']}

SUSTAINABLE BIO-REMEDIES:
{remedy_bullets}

IRRIGATION & SOIL MANAGEMENT:
{result['irrigation_and_soil']}

CHEMICAL ELIMINATION PROTOCOL:
{result['chemical_reduction_advice']}

UN SUSTAINABLE DEVELOPMENT GOAL ALIGNMENT:
{result['sdg_impact']}
=================================================="""
        st.download_button(
            label=t['download_btn'],
            data=report_text,
            file_name=f"agroai_report_{result['condition_key']}.txt",
            mime="text/plain"
        )
