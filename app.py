
import streamlit as st
import datetime

st.set_page_config(page_title="PRP Formulation Assistant", layout="centered")

st.title("🧠 AI-Guided PRP Formulation Assistant")

st.header("📄 Upload fMRI File")
uploaded_file = st.file_uploader("Choose a PDF or image file", type=["pdf", "png", "jpg"])

st.header("📊 Enter Pain Score (0–10)")
pain_score = st.slider("Pain Score", 0, 10, 5)

if st.button("Generate Recommendation"):
    st.success("Processing scan and score...")

    pattern = "ACC-dominant (Cognitive-Affective Pain)"
    formula = [
        "PRP (3–6x concentration)",
        "CBD 2%",
        "Curcumin 1%",
        "Lidocaine 2.5%",
        "HA + DMSO base"
    ]

    st.subheader("🧠 AI Interpretation")
    st.write(f"Detected pattern: **{pattern}**")

    st.subheader("💊 Suggested PRP Formulation")
    for item in formula:
        st.markdown(f"- {item}")

    st.header("🔁 Outcome Tracking")
    post_score = st.slider("Post-treatment Pain Score", 0, 10, 3)
    notes = st.text_area("Clinician Notes or Observations")

    if st.button("Log Case"):
        st.success("Case logged successfully!")
        st.write("📅 Date:", datetime.date.today())
        st.write("Initial Score:", pain_score)
        st.write("Post-treatment Score:", post_score)
        st.write("Notes:", notes)

        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append({
            "Date": str(datetime.date.today()),
            "Pattern": pattern,
            "Pre-Score": pain_score,
            "Post-Score": post_score,
            "Formula": formula,
            "Notes": notes
        })

if "history" in st.session_state:
    st.header("📈 Case History")
    st.dataframe(st.session_state.history)
