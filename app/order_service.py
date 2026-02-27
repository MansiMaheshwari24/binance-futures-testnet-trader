import logging
from .binance_client import BinanceFuturesClient

class OrderService:

    def __init__(self):
        self.client = BinanceFuturesClient()
        self.logger = logging.getLogger()

    def create_order(self, symbol, side, order_type, quantity, price=None):

        try:
            self.logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

            response = self.client.place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )

            self.logger.info(f"Order response: {response}")
            return response

        except Exception as e:
            self.logger.error(f"Order failed: {str(e)}")
            raise