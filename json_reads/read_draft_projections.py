from classes import draft_projections_def
from classes import draft_projections_k
from classes import draft_projections_qb
from classes import draft_projections_rb
from classes import draft_projections_te
from classes import draft_projections_wr

import json
import requests

def json_read_draftprojections_def(projections_def):
	url = "https://www.fantasyfootballnerd.com/service/draft-projections/json/hcfb7mbis7ny/def/"
	r = requests.get(url)
	json_def = r.json()
	for i in json_def['DraftProjections']:
		projections_def.append(draft_projections_def.DraftProjectionDEF(i['playerId'], i['sacks'], i['interceptions'], i['fumbleRec'], i['TD'], i['specialTeamTD'], i['fantasyPoints'], i['displayName'], i['team']))
	return projections_def

def json_read_draftprojections_qb(projections_qb):
	url = "https://www.fantasyfootballnerd.com/service/draft-projections/json/hcfb7mbis7ny/qb/"
	r = requests.get(url)
	json_qb = r.json()
	for i in json_qb['DraftProjections']:
		projections_qb.append(draft_projections_qb.DraftProjectionsQB(i['playerId'], i['completions'], i['attempts'], i['passingYards'], i['passingTD'], i['passingInt'], i['rushAtt'], i['rushYards'], i['rushTD'], i['fumbles'], i['fantasyPoints'], i['displayName'], i['team']))
	return projections_qb

def json_read_draftprojections_k(projections_k):
	url = "https://www.fantasyfootballnerd.com/service/draft-projections/json/hcfb7mbis7ny/k/"
	r = requests.get(url)
	json_k = r.json()
	for i in json_k['DraftProjections']:
		projections_k.append(draft_projections_k.DraftProjectionsK(i['playerId'], i['xp'], i['fg'], i['fantasyPoints'], i['displayName'], i['team']))
	return projections_k

def json_read_draftprojections_rb(projections_rb):
	url = "https://www.fantasyfootballnerd.com/service/draft-projections/json/hcfb7mbis7ny/rb/"
	r = requests.get(url)
	json_rb = r.json()
	for i in json_rb['DraftProjections']:
		projections_rb.append(draft_projections_rb.DraftProjectionRB(i['playerId'], i['rushAtt'], i['rushYards'], i['rushTD'], i['fumbles'], i['rec'], i['recYards'], i['recTD'], i['fantasyPoints'], i['displayName'], i['team']))
	return projections_rb

def json_read_draftprojections_wr(projections_wr):
	url = "https://www.fantasyfootballnerd.com/service/draft-projections/json/hcfb7mbis7ny/wr/"
	r = requests.get(url)
	json_wr = r.json()
	for i in json_wr['DraftProjections']:
		projections_wr.append(draft_projections_wr.DraftProjectionWR(i['playerId'], i['rushAtt'], i['rushYards'], i['rushTD'], i['fumbles'], i['rec'], i['recYards'], i['recTD'], i['fantasyPoints'], i['displayName'], i['team']))
	return projections_wr

def json_read_draftprojections_te(projections_te):
	url = "https://www.fantasyfootballnerd.com/service/draft-projections/json/hcfb7mbis7ny/te/"
	r = requests.get(url)
	json_te = r.json()
	for i in json_te['DraftProjections']:
		projections_te.append(draft_projections_te.DraftProjectionTE(i['playerId'], i['rushAtt'], i['rushYards'], i['rushTD'], i['fumbles'], i['rec'], i['recYards'], i['recTD'], i['fantasyPoints'], i['displayName'], i['team']))
	return projections_te

