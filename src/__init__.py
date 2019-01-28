from flask import Flask

app = Flask("src")

from src.rest import register_routes

register_routes(app)
