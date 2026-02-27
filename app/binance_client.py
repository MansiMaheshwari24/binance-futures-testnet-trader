import time
import requests
from .config import API_KEY, SECRET_KEY, BASE_URL
from .utils import generate_signature

class BinanceFuturesClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "X-MBX-APIKEY": API_KEY
        }

    def _post(self, endpoint: str, params: dict):
        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 5000

        signature = generate_signature(SECRET_KEY, params)
        params["signature"] = signature

        url = f"{self.base_url}{endpoint}"

        response = requests.post(url, headers=self.headers, params=params, timeout=10)
        response.raise_for_status()

        return response.json()

    def place_order(self, symbol, side, order_type, quantity, price=None):

        endpoint = "/fapi/v1/order"

        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }

        if order_type.upper() == "LIMIT":
            if not price:
                raise ValueError("Price required for LIMIT order.")
            params["price"] = price
            params["timeInForce"] = "GTC"

        return self._post(endpoint, params)