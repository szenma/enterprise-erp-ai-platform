import requests

class ERPNextConnector:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def get_invoices(self):
        # Implement ERPNext API calls
        return {"status": "connected", "data": "sample invoices"}