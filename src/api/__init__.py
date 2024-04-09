from flask import Blueprint
from .routes import get_stock

api_blueprint = Blueprint('api', __name__)

api_blueprint.add_url_rule('/api/stock/<string:ticker>', view_func=get_stock, methods=['GET'])
