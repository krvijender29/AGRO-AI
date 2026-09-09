# 🌱 AgroAI: Smart Crop Health & Sustainable Farming Advisor
### *AI-Powered Diagnostics & Eco-Advisory for UN SDG 2 (Zero Hunger) & SDG 13 (Climate Action)*

[![1M1B Initiative](https://img.shields.io/badge/1M1B-AI%20for%20Sustainability-green)](https://www.1m1b.org/)
[![SDG 2](https://img.shields.io/badge/UN%20SDG-2%20Zero%20Hunger-orange)](https://sdgs.un.org/goals/goal2)
[![SDG 13](https://img.shields.io/badge/UN%20SDG-13%20Climate%20Action-blue)](https://sdgs.un.org/goals/goal13)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agro-ai-krvijender29.streamlit.app/)

> 🌐 **Live Web Application**: [https://agro-ai-krvijender29.streamlit.app/](https://agro-ai-krvijender29.streamlit.app/)

---

## 📌 Project Overview
Plant diseases cost the global agricultural economy over ** billion annually**, with smallholder farmers bearing the brunt through 20% to 40% harvest losses. In addition, misdiagnosis frequently leads to excessive prophylactic spraying of synthetic chemical pesticides, degrading soil microbial health, polluting groundwater, and accelerating greenhouse gas emissions.

**AgroAI** is an edge-ready, interactive web application that bridges AI computer vision with sustainable agronomic science. By simply uploading or photographing a crop leaf, farmers receive:
1. **Instant Disease Diagnosis & Severity Scoring**: Identifies pathogens (blights, rusts, bacterial spots, or healthy foliage).
2. **Organic Bio-Remedy Protocols**: Prescribes non-chemical, biologically sound alternatives (e.g. *Bacillus subtilis*, neem bio-deterrents, Trichoderma).
3. **Chemical Reduction Footprint**: Quantitative guidance on curbing synthetic fungicide and pesticide dependency.
4. **Soil & Irrigation Care**: Agronomic guidelines to eliminate fungal spore propagation.

---

## 🇺🇳 Alignment with UN Sustainable Development Goals
- **SDG 2: Zero Hunger (Target 2.4)**: Promotes resilient agricultural practices and sustainable food production systems by preventing catastrophic crop failure.
- **SDG 12: Responsible Consumption and Production (Target 12.4)**: Significantly cuts down toxic chemical pesticide usage, lowering agrochemical residue on crops and in food supplies.
- **SDG 13: Climate Action (Target 13.1)**: Curtails the high carbon footprint linked to chemical pesticide synthesis and transportation.
- **SDG 15: Life on Land (Target 15.3)**: Preserves soil microbial biodiversity and combats agricultural land degradation.

---

## 🏗️ System Architecture
`
[ Leaf Image Input ] ---> (Upload / Sample Selector)
        │
        ▼
[ Computer Vision Diagnostic Engine ]
   ├── Chromaticity & Chlorophyll Analysis
   ├── Necrotic Lesion Ratio Calculation
   └── Feature Mapping & Probability Distribution
        │
        ▼
[ Sustainable Knowledge Base Engine ]
   ├── Eco-Friendly Bio-Remedies
   ├── Irrigation & Moisture Guidance
   └── Chemical Footprint Reduction Strategy
        │
        ▼
[ Interactive Streamlit Dashboard + Exportable Diagnostic Report ]
`

---

## 🚀 Quickstart Guide

### Prerequisites
- Python 3.9+ installed on your system.

### 1. Clone or Navigate to the Repository
`ash
git clone https://github.com/your-username/agro-ai-sustainability.git
cd agro-ai-sustainability
`

### 2. Install Dependencies
`ash
pip install -r requirements.txt
`

### 3. Run the Web Application
`ash
streamlit run app.py
`
Open your browser at http://localhost:8501.

---

## 🧪 Testing with Built-in Samples
No crop leaves on hand? The app includes pre-loaded sample leaves accessible via the **"Select Demo Sample Leaf"** selector:
- Tomato - Early Blight (Infected)
- Tomato - Healthy Foliage
- Potato - Late Blight (Critical)
- Corn - Common Rust
- Bell Pepper - Bacterial Spot

---

## 👥 Author & Acknowledgements
- Developed as the **Capstone Project** for the **1M1B (One Million for One Billion) AI for Sustainability Program**.
- Guided by the UN SDG framework and sustainable agricultural methodologies.
