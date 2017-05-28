import requests
import json

def json_read_byeweek(bye_week):
	url = "https://www.fantasyfootballnerd.com/service/byes/json/hcfb7mbis7ny/"
	r = requests.get(url)
	json_byeweek = r.json()
	week = 5
	while True:
		for i in json_byeweek['Bye Week ' + str(week)]:
			bye_week.append(byeWeek(i['team'], i['byeWeek'], i['displayName']))
		week += 1
		if week == 12:
			break