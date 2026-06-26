import streamlit as st
import pandas as pd
from src.ml.payroll_anomaly import detect_anomalies
from src.ml.cashflow_forecast import forecast_cashflow

st.set_page_config(page_title="ERP-AI Platform Demo", layout="wide")
st.title("🚀 ERP-AI Platform Demo")
st.markdown("### Intelligent ERP Automation with AI Agents & ML")

tab1, tab2, tab3 = st.tabs(["Payroll Anomaly Detection", "Cashflow Forecasting", "Vendor Scoring"])

with tab1:
    st.subheader("HR - Payroll Anomaly Detection")
    if st.button("Run Anomaly Detection"):
        df = pd.read_csv("data/sample_payroll.csv")
        anomalies, scores = detect_anomalies(df)
        st.dataframe(anomalies)
        st.success(f"Detected {len(anomalies)} anomalies!")

with tab2:
    st.subheader("Finance - Cashflow Forecasting")
    if st.button("Generate Forecast"):
        forecast = forecast_cashflow()
        st.line_chart(forecast)
        st.success("30-day cashflow forecast generated using Prophet!")

with tab3:
    st.subheader("Procurement - Vendor Scoring")
    st.info("Advanced XGBoost + SHAP scoring coming soon...")

st.sidebar.info("This demo showcases production AI capabilities for enterprise ERP.")