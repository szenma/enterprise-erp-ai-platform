from fastapi import APIRouter
from src.connectors.erpnext import ERPNextConnector

router = APIRouter()

@router.get("/invoices")
async def get_invoices():
    connector = ERPNextConnector("url", "key")
    return connector.get_invoices()