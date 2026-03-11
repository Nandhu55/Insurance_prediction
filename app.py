import streamlit as st
from src.prediction import Insurance_Prediction

# Page config
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

body {
background: linear-gradient(135deg,#0f172a,#020617);
}

.title {
text-align:center;
font-size:42px;
font-weight:700;
background: linear-gradient(90deg,#4facfe,#00f2fe);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
text-align:center;
color:#9ca3af;
font-size:18px;
margin-bottom:30px;
}

.card{
background: rgba(255,255,255,0.05);
padding:30px;
border-radius:15px;
backdrop-filter: blur(10px);
border:1px solid rgba(255,255,255,0.1);
}

.result{
padding:25px;
border-radius:12px;
text-align:center;
font-size:22px;
font-weight:600;
background: linear-gradient(90deg,#4facfe,#00f2fe);
color:white;
margin-top:20px;
}

button[kind="primary"]{
background: linear-gradient(90deg,#6366f1,#06b6d4);
border:none;
border-radius:10px;
height:3em;
font-size:16px;
font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">💰 Insurance Cost Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning based premium estimator</div>', unsafe_allow_html=True)

# Card container
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📋 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Age", min_value=1, max_value=100)
    Annual_Income_LPA = st.number_input("Annual Income (LPA)")

with col2:
    Policy_Term_Years = st.number_input("Policy Term (Years)")
    Sum_Assured_Lakhs = st.number_input("Sum Assured (Lakhs)")

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# Prediction Button
if st.button("🔍 Predict Insurance Cost", use_container_width=True):

    model = Insurance_Prediction()

    result = model.prediction(
        Age,
        Annual_Income_LPA,
        Policy_Term_Years,
        Sum_Assured_Lakhs
    )

    st.markdown(
        f'<div class="result">Estimated Insurance Cost: {result}</div>',
        unsafe_allow_html=True
    )

st.write("")
st.caption("⚡ Built with Streamlit & Machine Learning")