from fastapi import FastAPI
from src.core.config import settings
from src.api.v1 import erp, agents, ml

app = FastAPI(title="ERP-AI Platform", version="1.0.0")

app.include_router(erp.router, prefix="/api/v1/erp", tags=["ERP"])
app.include_router(agents.router, prefix="/api/v1/agents", tags=["Agents"])
app.include_router(ml.router, prefix="/api/v1/ml", tags=["ML"])

@app.get("/")
async def root():
    return {"message": "Welcome to ERP-AI Platform"}