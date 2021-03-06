from classes import team_class

import requests
import json

def json_read_teams(team_list):
	url = "https://www.fantasyfootballnerd.com/service/nfl-teams/json/hcfb7mbis7ny"
	r = requests.get(url)
	json_teams = r.json()
	for i in json_teams['NFLTeams']:
		team_list.append(team_class.Team(i['code'], i['fullName'], i['shortName']))
	return team_list