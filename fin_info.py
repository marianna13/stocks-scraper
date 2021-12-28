import yfinance as yf

def get_info(ticker):
    ticker_yahoo = yf.Ticker(ticker)
    return {
        "symbol": ticker_yahoo.info['symbol'],
        "shortName": ticker_yahoo.info['shortName'],
        "currentPrice": ticker_yahoo.info['currentPrice'],
        "prevClose": ticker_yahoo.info["previousClose"]
        }

