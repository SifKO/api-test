"""
Initialiaze application
"""
import logging
from flask import Flask
from config import Config


logger = logging.getLogger()
# FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s' 
FORMAT = '%(levelname)s : %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

app = Flask(__name__)
app.config.from_object(Config)

from green_api import routes