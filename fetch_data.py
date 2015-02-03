import os
import requests
import pymongo

from pymongo import MongoClient
client = MongoClient()
db = client.fpl
db.drop_collection('fantasyapp_data')
NO_OF_PLAYERS = 677

for i in range(1,NO_OF_PLAYERS+1):
	url = os.path.join("http://fantasy.premierleague.com/web/api/elements/", str(i))
	r = requests.get(url)
	data = {}
	data['fpl_data'] = r.json()
	fantasyapp_data = db.fantasyapp_data
	insert = fantasyapp_data.insert(data)
	print insert, i