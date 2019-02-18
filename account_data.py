import urllib.request
import urllib.error
import twurl
import json
import ssl
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def main_account_info():
	"""
	Reads main info about people from JSON file (name, location, and profile icon).
	
	None -> set
	"""
	f = open('account.txt', 'r', encoding='utf-8', errors='ignore')
	acct = f.readline()
	#acct = input('Enter Twitter Account:')
	url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
	print('Retrieving', url)
	connection = urllib.request.urlopen(url, context=ctx)
	data = connection.read().decode()

	js = json.loads(data)

	headers = dict(connection.getheaders())
	print('Remaining', headers['x-rate-limit-remaining'])

	name_location_icon_set = set()
	for u in js['users']:
		name_location_icon_set.add((u['screen_name'], u['location'], u['profile_image_url_https']))

	return name_location_icon_set


def find_coordinates(name_location_icon_set):
	"""
	Converts inline location for each person into latitude and longitude.
	
	set -> set
	"""
	name_coordinates_icon_set = set()
	geolocator = Nominatim(user_agent='FriendlyLocation', timeout=None)
	geocode = RateLimiter(geolocator.geocode,
						  min_delay_seconds=1,
						  max_retries=5)
	for triad in name_location_icon_set:
		location = geolocator.geocode(triad[1])
		if location:
			coordinates = (location.latitude, location.longitude)
			name_coordinates_icon_set.add((triad[0], coordinates, triad[2]))
		else:
			coordinates = 'N/A'

	return name_coordinates_icon_set


def build_map(name_coordinates_icon_set):
	"""
	Generates map based on location of scanned people.
	
	set -> None
	"""
	mymap = folium.Map(tiles='Mapbox Bright', zoom_start=13)
	fg_friends_location = folium.FeatureGroup(name='FriendlyLocation')
	for triad in name_coordinates_icon_set:
		icon = folium.features.CustomIcon(triad[2], icon_size=(35,35))
		folium.Marker(triad[1], popup=triad[0], icon=icon).add_to(mymap)
	mymap.save('map.html')
