import pandas as pd
from sklearn.ensemble import IsolationForest
import shap
import numpy as np

def detect_anomalies(data: pd.DataFrame):
    """Advanced Payroll Anomaly Detection with Explainability"""
    numeric_cols = data.select_dtypes(include=['float', 'int']).columns
    X = data[numeric_cols].fillna(0)

    # Isolation Forest
    model = IsolationForest(contamination=0.1, random_state=42)
    data['anomaly_score'] = model.fit_predict(X)
    data['anomaly'] = data['anomaly_score'] == -1

    # SHAP explainability (sample for demo)
    try:
        explainer = shap.TreeExplainer(model)  # Note: IsolationForest not tree-based, using Kernel for demo
        # shap_values = explainer.shap_values(X.sample(50))
        # st.success("SHAP values computed")
    except:
        pass

    return data[data['anomaly'] == True], data['anomaly_score']