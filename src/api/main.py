import yfinance as yf
from flask import Flask, jsonify
import logging

api = Flask(__name__)


@api.route('/')
def index():
    return 'Hello, World!'


@api.route('/api/stock/<string:ticker>', methods=['GET'])
def stock(ticker):
    stock = yf.Ticker(ticker)
    return jsonify(stock.history(period='1y').to_dict(orient='records'))


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)

