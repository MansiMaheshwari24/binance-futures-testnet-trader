import argparse
import logging
from app.utils import setup_logger
from app.order_service import OrderService

def validate_input(args):
    if args.side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

    if args.type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

    if args.type.upper() == "LIMIT" and not args.price:
        raise ValueError("Price is required for LIMIT orders.")

def main():

    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Order Placement")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args)

        print("\n===== Order Request Summary =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")
        print("=================================\n")

        service = OrderService()
        response = service.create_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("✅ Order Placed Successfully")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

    except Exception as e:
        print("❌ Order Failed:", str(e))

if __name__ == "__main__":
    main()