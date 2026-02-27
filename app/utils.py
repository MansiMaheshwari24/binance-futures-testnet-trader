import hmac
import hashlib
import logging
from urllib.parse import urlencode

def generate_signature(secret_key: str, params: dict) -> str:
    query_string = urlencode(params)
    return hmac.new(
        secret_key.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()

def setup_logger():
    logging.basicConfig(
        filename="logs/trading.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger()