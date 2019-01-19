from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)

	mongo.init_app(app)

	from .main.views import main

	app.register_blueprint(main)

	return app
