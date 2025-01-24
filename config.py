"""
Config of our flask app 
"""

import os


class Config:
    """
    class for config flask app, storing config variables
    """
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '111cc8c7d71403a3c6fb750670d95c7ec6'
