from flask import Flask
from flask_cors import CORS
import os

def init_app():
    app = Flask(__name__, 
                template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'))
    CORS(app)
    return app 