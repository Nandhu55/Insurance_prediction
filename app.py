import streamlit as st
from src.prediction import Insurance_Prediction

st.set_page_config(
    page_title="Insurance Cost Prediction",
    page_icon="💰",
    layout="centered"
)

# ---------- Custom Styling ----------
st.markdown("""
<style>

body{
background: linear-gradient(120deg,#020617,#0f172a);
}

.title{
text-align:center;
font-size:48px;
font-weight:700;
background: linear-gradient(90deg,#38bdf8,#22d3ee);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
text-align:center;
color:#9ca3af;
font-size:18px;
margin-bottom:40px;
}

.section{
background: rgba(255,255,255,0.04);
padding:30px;
border-radius:15px;
border:1px solid rgba(255,255,255,0.08);
}

.result{
padding:22px;
border-radius:12px;
text-align:center;
font-size:24px;
font-weight:600;
background: linear-gradient(90deg,#3b82f6,#06b6d4);
color:white;
margin-top:20px;
}

button[kind="primary"]{
background: linear-gradient(90deg,#6366f1,#22d3ee);
border:none;
border-radius:10px;
font-weight:600;
height:3em;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('💰 Insurance Cost Prediction', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning based premium estimator</div>', unsafe_allow_html=True)

# ---------- Input Section ----------
st.markdown('<div class="section">', unsafe_allow_html=True)

st.subheader("📋 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Age", min_value=1, max_value=100, value=21)
    Annual_Income_LPA = st.number_input("Annual Income (LPA)", value=1000000.0)

with col2:
    Policy_Term_Years = st.number_input("Policy Term (Years)", value=5)
    Sum_Assured_Lakhs = st.number_input("Sum Assured (Lakhs)", value=3.0)

st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# ---------- Prediction ----------
if st.button("🔍 Predict Insurance Cost", use_container_width=True):

    model = Insurance_Prediction()

    result = model.prediction(
        Age,
        Annual_Income_LPA,
        Policy_Term_Years,
        Sum_Assured_Lakhs
    )

    st.markdown(
        f'<div class="result">Estimated Insurance Cost: ₹ {round(result,2)}</div>',
        unsafe_allow_html=True
    )

st.write("")
st.caption("⚡ Built with Streamlit & Machine Learning")
