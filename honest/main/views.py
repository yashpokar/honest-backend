import json
from flask import Blueprint, jsonify, request
from honest import mongo
import requests

main = Blueprint('main', __name__)

@main.route('/')
def home():
	address = request.args.get('address', None)

	if not address:
		return jsonify(error='Address is Required.', success=False), 401

	response = requests.post('https://www.latlong.net/_spm4.php',
		headers={
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
			'origin': 'https://www.latlong.net',
			'referer': 'https://www.latlong.net/',
		},
		data={
			'c1': 'Stumpergasse 51, 1060 Vienna',
			'action': 'gpcm',
			'cp': '',
		}
	)

	[latitude, longitude] = response.content.decode('utf-8').split(',')

	results = mongo.db.outlets.find_one({ 'geometry': { '$geoIntersects': { '$geometry': { 'type': 'Point', 'coordinates': [ float(longitude), float(latitude) ] } } } })

	if not results:
		return jsonify(success=False, error='not found')

	return jsonify(outlet=results['name'], success=True)
