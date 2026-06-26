import pandas as pd
from prophet import Prophet
import numpy as np

def forecast_cashflow(days=30):
    """Advanced Cashflow Forecasting with Prophet"""
    # Generate sample historical data
    dates = pd.date_range(end=pd.Timestamp.today(), periods=365)
    df = pd.DataFrame({
        'ds': dates,
        'y': np.random.normal(120000, 20000, 365).cumsum()
    })

    model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
    model.fit(df)

    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(days)