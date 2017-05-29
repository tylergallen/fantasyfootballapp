from classes import schedule_class

import requests
import json

def json_read_schedule(schedule_full):
	url = "https://www.fantasyfootballnerd.com/service/schedule/json/hcfb7mbis7ny/"
	r = requests.get(url)
	json_schedule = r.json()
	for i in json_schedule['Schedule']:
		schedule_full.append(schedule_class.Schedule(i['gameId'], i['gameWeek'], i['gameDate'], i['awayTeam'], i['homeTeam'], i['gameTimeET'], i['tvStation'], i['winner']))
