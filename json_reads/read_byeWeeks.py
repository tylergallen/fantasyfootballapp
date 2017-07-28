from classes import byeweek_class

import requests
import json

def json_read_byeweek(bye_week):
	url = "https://www.fantasyfootballnerd.com/service/byes/json/hcfb7mbis7ny/"
	r = requests.get(url)
	json_byeweek = r.json()
	week = 5
	for i in json_byeweek['Bye Week ' + str(week)]:
		bye_week.append(i['byeWeek'])
		week += 1
		if week == 12:
			break
	return bye_week

def main(bye_week):
	json_read_byeweek(bye_week)

if __name__ == "__main__":
	main()
