
import streamlit as st
import datetime
import pandas as pd

st.set_page_config(page_title="AI-Guided PRP Therapy Assistant", layout="wide", page_icon="🧠")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🧠 AI-Guided PRP Formulation Assistant")
st.markdown("This tool simulates an adaptive AI system that suggests and refines topical PRP formulations based on brain scan patterns and patient outcomes.")

# Columns for layout
left, right = st.columns(2)

# Upload Section
with left:
    st.header("📄 Upload fMRI File")
    uploaded_file = st.file_uploader("Upload simulated fMRI scan (PDF/image)", type=["pdf", "png", "jpg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded fMRI Scan Preview", use_column_width=True)

# Pain Score Entry
with right:
    st.header("📊 Initial Pain Score (VAS)")
    pain_score = st.slider("Select pain score before treatment", 0, 10, 6)

st.markdown("---")

# Simulated pattern detection
st.header("🔍 Simulated AI Pattern Detection")
pattern = st.selectbox("Choose detected pain pattern (for simulation):", [
    "ACC-dominant",
    "Thalamic-dominant",
    "Insular/S1-dominant",
    "Widespread/Glial-activated"
])

# Dynamic formulation mapping
formulations = {
    "ACC-dominant": [
        "PRP (4x concentration)",
        "CBD 2%",
        "Curcumin 1%",
        "Lidocaine 2.5%"
    ],
    "Thalamic-dominant": [
        "PRP (5x concentration)",
        "Ketamine (0.1%)",
        "Baclofen (1%)"
    ],
    "Insular/S1-dominant": [
        "PRP (6x concentration)",
        "Capsaicin (0.075%)",
        "Diclofenac (1%)"
    ],
    "Widespread/Glial-activated": [
        "PRP (3x concentration)",
        "Naltrexone (1%)",
        "Palmitoylethanolamide (PEA)",
        "HA base"
    ]
}

rationale_dict = {
    "CBD 2%": "Reduces neuroinflammation via CB2 modulation",
    "Curcumin 1%": "Blocks TRPV1 and inflammatory transcription factors",
    "Lidocaine 2.5%": "Short-term desensitization via sodium channel block",
    "Ketamine (0.1%)": "NMDA antagonism for neuropathic modulation",
    "Baclofen (1%)": "GABA-B agonist, reduces excitatory signaling",
    "Capsaicin (0.075%)": "TRPV1 overload to reduce nociceptor response",
    "Diclofenac (1%)": "COX inhibition for local anti-inflammatory effects",
    "Naltrexone (1%)": "Glial modulator, reduces cytokine reactivity",
    "Palmitoylethanolamide (PEA)": "Endogenous anti-inflammatory fatty acid amide",
    "HA base": "Enhances bioavailability and tissue retention",
    "PRP (3x concentration)": "Autologous growth factor concentrate",
    "PRP (4x concentration)": "Standard PRP for inflammation and healing",
    "PRP (5x concentration)": "Enhanced PRP for deeper modulation",
    "PRP (6x concentration)": "High-yield PRP for intensive cases"
}

# Display output
if st.button("💊 Generate Formulation"):
    selected_formula = formulations[pattern]

    st.subheader("🧠 AI Interpretation")
    st.write(f"Detected pattern: **{pattern}**")

    st.subheader("💡 Personalized PRP Formulation")
    for ingredient in selected_formula:
        st.markdown(f"- **{ingredient}** — {rationale_dict.get(ingredient, 'Custom component')}")

    # Outcome Section
    st.markdown("---")
    st.subheader("🔁 Outcome & Feedback Loop")

    post_score = st.slider("Follow-up Pain Score (1 week later)", 0, 10, 3)
    notes = st.text_area("Clinician Notes / Adjustments")

    # Feedback logic
    if post_score >= pain_score:
        feedback = "🔄 Suggest adjusting bioactives: increase anti-inflammatory agents or switch delivery base."
    elif (pain_score - post_score) >= 4:
        feedback = "✅ High improvement. Continue current formulation."
    else:
        feedback = "↔️ Moderate response. Consider dose titration or adjunct agent."

    if st.button("💾 Log Case"):
        st.success("Case logged successfully!")
        st.session_state.history.append({
            "Date": str(datetime.date.today()),
            "Pattern": pattern,
            "Pre-Score": pain_score,
            "Post-Score": post_score,
            "Formula": ", ".join(selected_formula),
            "Feedback": feedback,
            "Notes": notes
        })

# History Table
if st.session_state.history:
    st.markdown("---")
    st.header("📈 Treatment History")
    st.dataframe(pd.DataFrame(st.session_state.history))
