from classes import draft_tier_class

import requests
import json

def json_read_draft_tier(draft_tiers):
	url = "https://www.fantasyfootballnerd.com/service/tiers/json/hcfb7mbis7ny/"
	r = requests.get(url)
	json_tier = r.json()
	for i in json_tier:
		draft_tiers.append(draft_tier_class.DraftTier(i['playerId'], i['position'], i['tier'], i['displayName']))
	return draft_tiers