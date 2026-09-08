# 1M1B AI for Sustainability - Project Submission Answers
*Copy-paste ready answers prepared for https://forms.gle/2tBrkVWDETHzVg1G7*

---

### 1. Project Title
**AgroAI: Smart Crop Health Diagnostic & Sustainable Farming Advisor**

---

### 2. UN Sustainable Development Goal (SDG) Alignment
- **Primary SDG:** **SDG 2: Zero Hunger** (Target 2.4 - Ensure sustainable food production systems and implement resilient agricultural practices)
- **Secondary SDG:** **SDG 13: Climate Action** (Target 13.1 - Strengthen resilience and adaptive capacity to climate-related hazards and natural disasters)
- **Additional Impact:** **SDG 12: Responsible Consumption and Production** (Minimizing agrochemical contamination in food systems)

---

### 3. Problem Statement
Plant pathogens, leaf blights, and fungal infections cause **20% to 40% of global crop harvest losses annually**, costing over  billion. For smallholder farmers, lacking timely access to agricultural extension officers or lab diagnostics often leads to:
1. **Delayed Intervention:** Diseases spread unchecked across whole fields, wiping out household income and regional food security.
2. **Harmful Chemical Overuse:** Farmers preemptively or incorrectly spray broad-spectrum synthetic chemical fungicides and pesticides. This causes toxic runoff into local water tables, degrades vital soil microbiomes, increases carbon emissions from agrochemical manufacturing, and leads to chemical pest resistance.

There is an urgent need for an accessible, edge-deployable AI tool that diagnoses crop diseases early from leaf photos and prioritizes **biological, organic, and eco-friendly remedies**.

---

### 4. Detailed Solution Description
**AgroAI** is an interactive, AI-powered web platform and diagnostic advisor designed to safeguard crop yields while driving sustainable farming practices:

1. **Computer Vision Leaf Diagnostics:** The farmer uploads or photographs a leaf directly from their smartphone or local device. The AI engine processes chromaticity indicators, chlorophyll distribution ratios, and necrotic lesion densities to classify conditions (e.g., *Early Blight in Tomatoes*, *Late Blight in Potatoes*, *Common Rust in Corn*, *Bacterial Spot in Bell Peppers*, or *Healthy Foliage*).
2. **Ecological Bio-Remedy Protocols:** Instead of default synthetic chemicals, the system immediately prescribes biological and organic remedies (such as *Bacillus subtilis* bio-fungicides, cold-pressed neem formulations, or Trichoderma inoculants).
3. **Chemical Reduction Footprint Advisor:** Quantifies and alerts farmers on how much synthetic chemical runoff can be avoided (reducing pesticide reliance by up to 70-80%).
4. **Agronomic Best Practices:** Recommends targeted drip irrigation, canopy spacing, and mulch management to eliminate pathogen transmission vectors.
5. **Instant Farmer Diagnostic Report:** Generates an on-demand, printable text report summarizing symptoms, severity, and step-by-step eco-remedies for field application.

---

### 5. AI Elements & Tools Used
- **Computer Vision & Feature Engineering:** PyTorch / NumPy / PIL pipeline analyzing leaf color spectra, localized lesion contrast, and morphological necrosis variance.
- **Classification Engine:** Multi-class probabilistic model with Softmax confidence scoring and pathology pattern matching.
- **Frontend / Application Layer:** Streamlit (Python) for responsive, low-latency, and mobile-friendly interactive interface.
- **Data & Knowledge Base:** JSON-driven agronomic knowledge repository codifying sustainable treatment guidelines aligned with FAO and organic agriculture standards.

---

### 6. GitHub / Prototype / Demo Links
- **Local Prototype Directory:** gro_ai_sustainability
- **GitHub Repository Link:** *(Insert your GitHub repo URL after pushing, e.g., https://github.com/your-username/agro-ai-sustainability)*
- **Live Demo / Video Demonstration:** *(Attach screenshot or screen recording of the app running at http://localhost:8501)*

---

### 7. Images / Video of Prototype
*(You can take screenshots of your local running Streamlit app at http://localhost:8501 showing the disease analysis, probability chart, and eco-remedy tabs.)*

---

### 8. Your Story & Project Story (Project Journey)
**How this program helped me learn key concepts required for building my project:**
> "Participating in the 1M1B AI for Sustainability Program has been a transformative experience. Before joining this program, I viewed Artificial Intelligence primarily as an abstract software engineering discipline. Through the guided sessions, expert webinars, and SDG-focused curriculum, I developed a deeper understanding of how AI can serve as a catalyst for tangible environmental and humanitarian impact.
>
> Learning about the United Nations Sustainable Development Goals challenged me to re-orient my technical skills toward solving critical real-world crises like food insecurity (SDG 2) and climate change (SDG 13). I realized that smallholder farmers face disproportionate risks from crop diseases and lack accessible diagnostic tools. This inspired me to develop AgroAI—combining computer vision and agricultural science to give farmers instantaneous disease identification and sustainable, organic alternatives to toxic chemical pesticides.
>
> This program taught me how to move from problem discovery and systems thinking to designing an end-to-end user-centric AI application. It has fortified my aspiration to build sustainable technology that empowers communities and protects our planet."
