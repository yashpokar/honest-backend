from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

mongo = PyMongo()
cors = CORS()

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)

	mongo.init_app(app)
	cors.init_app(app,
		resources={'*': {
			'origins': app.config['ALLOWED_ORIGINS'],
			'Access-Control-Allow-Origin': app.config['ALLOWED_ORIGINS']
	}})

	from .main.views import main

	app.register_blueprint(main)

	return app
