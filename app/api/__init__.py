import os
import glob

from flask import Blueprint
from flask_cors import CORS

api = Blueprint('api', __name__)

# apply CORS to Blueprint
CORS(api)

# all controllers(api endpoints) for various collections of database
__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
