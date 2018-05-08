from flask import Flask
from configs import Config
from app import routes

app = Flask(__name__)
app.config.from_object(Config)
