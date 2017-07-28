from classes import draft_rankings_class

import requests
import json

def json_read_draft_rankings(draft_rankings):
	url = "https://www.fantasyfootballnerd.com/service/draft-rankings/json/hcfb7mbis7ny/1/"
	r = requests.get(url)
	json_rankings= r.json()
	for i in json_rankings['DraftRankings']:
		draft_rankings.append(draft_rankings_class.DraftRanking(i['playerId'], i['position'], i['displayName'], i['fname'], i['lname'], i['team'], i['byeWeek'], i['standDev'], i['nerdRank'], i['positionRank'], i['overallRank']))
	return draft_rankings