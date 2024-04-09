import yfinance as yf
from flask import jsonify


def get_stock(ticker):
    stock = yf.Ticker(ticker)
    return jsonify(stock.history(period='1y').to_dict(orient='records'))
