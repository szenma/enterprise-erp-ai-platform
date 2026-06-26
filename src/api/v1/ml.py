from fastapi import APIRouter
from src.ml.payroll_anomaly import detect_anomalies
import pandas as pd

router = APIRouter()

@router.post("/payroll/anomalies")
async def detect_payroll_anomalies(data: list):
    df = pd.DataFrame(data)
    return detect_anomalies(df).to_dict()