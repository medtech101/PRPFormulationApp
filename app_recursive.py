
import streamlit as st
import datetime
import pandas as pd

# Set page configuration
st.set_page_config(page_title="AI-Guided PRP Therapy Assistant", layout="wide", page_icon="🧠")

# Initialize session history
if "history" not in st.session_state:
    st.session_state.history = []

# Title
st.title("🧠 AI-Guided PRP Formulation Assistant")
st.markdown("This tool simulates an adaptive AI system that suggests and improves topical PRP formulations based on brain scan insights and pain response.")

# Layout: Two columns
left, right = st.columns(2)

# File Upload Section
with left:
    st.header("📄 Upload fMRI File")
    uploaded_file = st.file_uploader("Upload simulated fMRI scan (PDF/image)", type=["pdf", "png", "jpg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded fMRI Scan Preview", use_column_width=True)

# Pain Score Input
with right:
    st.header("📊 Enter Initial Pain Score (VAS)")
    pain_score = st.slider("Pain Score (0 = no pain, 10 = worst pain)", 0, 10, 6)

st.markdown("---")

# Generate AI Recommendation
if st.button("🔍 Generate Personalized Recommendation"):
    pattern = "ACC-dominant (Cognitive-Affective Pain)"
    formula = [
        "PRP (4x concentration)",
        "CBD 2%",
        "Curcumin 1%",
        "Lidocaine 2.5%",
        "HA + DMSO base"
    ]
    rationale = [
        "Reduces neuroinflammation via CB2 modulation",
        "Blocks TRPV1 and inflammatory transcription factors",
        "Short-term neural desensitization via sodium channel block",
        "Hydrogel base improves tissue retention and penetration"
    ]

    st.success("AI analysis complete.")
    st.subheader("🧠 AI Interpretation")
    st.markdown(f"**Detected Pattern:** {pattern}")

    st.subheader("💊 Suggested Topical PRP Formulation")
    for ing, reason in zip(formula, rationale):
        st.markdown(f"- **{ing}** — {reason}")

    st.markdown("---")
    st.subheader("🔁 Outcome Tracking (Simulated Recursion)")

    post_score = st.slider("Follow-up Pain Score", 0, 10, 3)
    st.caption("Enter pain score after 1 week of treatment")

    if post_score >= pain_score:
        feedback = "🔄 AI Suggests Adjustment: Increase Curcumin to 2%, consider NMDA modulator (e.g., Ketamine microdose)"
    elif (pain_score - post_score) >= 4:
        feedback = "✅ High improvement. Current formulation effective. Recommend continuing."
    else:
        feedback = "↔️ Moderate improvement. Maintain formula and reassess in 1 week."

    notes = st.text_area("📝 Clinician Notes")

    if st.button("💾 Log Case and Feedback"):
        st.success("Case logged successfully!")
        case_data = {
            "Date": str(datetime.date.today()),
            "Pre-Score": pain_score,
            "Post-Score": post_score,
            "Pattern": pattern,
            "Formula": ", ".join(formula),
            "Feedback": feedback,
            "Notes": notes
        }
        st.session_state.history.append(case_data)

# History
if st.session_state.history:
    st.markdown("---")
    st.header("📈 Treatment History Log")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df)
