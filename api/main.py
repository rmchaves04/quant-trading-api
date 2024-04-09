from flask import Flask
import logging

api = Flask(__name__)


@api.route('/')
def index() :
    return 'Hello, World!'


if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=3000)

