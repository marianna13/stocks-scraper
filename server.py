import json
from flask import Flask
from flask import request
from fin_info import get_info
from scraper import get_stock_data
import time
start_time = time.time()

app = Flask(__name__)
@app.route('/', methods=['POST'])
def index():
    request_json = request.get_json()
    tickers = request_json.get('tickers')
    infos = get_data(tickers)
    return json.dumps({"data": infos})

@app.route('/get_stocks', methods=['GET'])
def get_stocks():
    tickers = ['MSFT', 'AAPL', 'TSLA', 'F', 'FB']
    infos = get_data(tickers)
    return json.dumps({"data": infos})
print("--- %s seconds ---" % (time.time() - start_time))


def get_data(tickers):
    infos = [get_info(ticker) for ticker in tickers]
    return infos

app.run(host='0.0.0.0', port=5000)