import requests
import json

def json_read_players(player_list):
	url = "https://www.fantasyfootballnerd.com/service/players/json/hcfb7mbis7ny"
	r = requests.get(url)
	json_players = r.json()
	for i in json_players['Players']:
		player_list.append(Player(i['playerId'], i['active'], i['jersey'], i['lname'], i['fname'], i['displayName'], i['team'], i['position'], i['height'], i['weight'], i['dob'], i['college']))