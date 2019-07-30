from flask import Flask
from src.rest.registry import register_views

app = Flask("src")
register_views(app)
