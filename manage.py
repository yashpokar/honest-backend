from honest import create_app
from flask_script import Manager
from config import LocalConfig

app = create_app(LocalConfig)
manager = Manager(app)

@manager.command
def db_migrate():
	from db import KMLParse

	parser = KMLParse()
	parser.parse('delivery_areas.kml')
	parser.dump_into_database(app.config['MONGO_URI'], app.config['MONGO_COLLECTION_NAME'])

	print('Database migrated successfully.')

if __name__ == '__main__':
	manager.run()
