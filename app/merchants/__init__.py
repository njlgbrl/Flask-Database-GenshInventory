from flask import Blueprint

merchant = Blueprint('merchant', __name__, url_prefix='/merchants')

from app.merchants import views