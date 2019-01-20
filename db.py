import re
import xml.etree.ElementTree as ET
import pymongo


class KMLParse(object):
	def __init__(self):
		self.polygons = []

	def parse(self, file):
		tree = ET.parse(file)
		root = tree.getroot()

		ns = dict(url='http://www.opengis.net/kml/2.2')

		placemarks = root.findall('.//url:Placemark', ns)

		for placemark in placemarks:
			polygon = placemark.find('.//url:Polygon', ns)

			if polygon is None:
				continue

			coordinates = [
				[list(map(float, coordinate.split(',')))[:2]
					for coordinate in polygon.find('.//url:coordinates', ns).text.strip().split('\n')
			]]
			name = placemark.find('.//url:name', ns).text

			polygon = dict(
				geometry=dict(
					type='Polygon',
					coordinates=coordinates,
				),
				name=name
			)

			self.polygons.append(polygon)

	def dump_into_database(self, mongo_uri, collection_name):
		[dbhost, dbname] = re.findall(r'mongodb://([^/]+)/(.+)', mongo_uri)[0]

		client = pymongo.MongoClient(dbhost)
		db = client[dbname]

		db[collection_name].insert_many(self.polygons)
		db[collection_name].create_index([('geometry', pymongo.GEOSPHERE)])
