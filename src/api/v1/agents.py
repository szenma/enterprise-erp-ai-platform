from fastapi import APIRouter
from src.agents.finance_agent import FinanceAgent

router = APIRouter()

@router.post("/finance/analyze")
async def analyze_finance(data: dict):
    agent = FinanceAgent()
    return agent.analyze_cashflow(data)