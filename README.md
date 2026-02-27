# Binance Futures Testnet Trader (USDT-M)

A CLI-based Python application to place Market and Limit orders on Binance Futures Testnet.

## Features

- Market & Limit Orders
- BUY / SELL support
- Structured architecture
- Logging to file
- Proper error handling
- Environment variable config

## Setup

1. Clone repository
2. Create virtual environment 

    python -m venv (venv-foldername)
    venv\Scripts\activate 

3. Install dependencies

pip install -r requirements.txt

4. Create .env file 

    BINANCE_API_KEY=your_api_key_here
    BINANCE_SECRET_KEY=your_secret_key_here
    BASE_URL=https://testnet.binancefuture.com
    
5. Add your Binance Futures Testnet API keys


## Run Examples

### Market Order

python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

### Limit Order

python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 63000

## Logs

Logs are stored in:
logs/trading.log

## Assumptions

- User has active Binance Futures Testnet account
- API key has Futures trading enabled
- Testnet base URL used