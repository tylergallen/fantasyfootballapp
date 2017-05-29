from json_reads import read_byeWeeks
from json_reads import read_players
from json_reads import read_schedule
from json_reads import read_teams

def read_from_json():
	byeWeeks = []
	players = []
	schedule = []
	teams = []
	byeWeeks = read_byeWeeks.json_read_byeweek(byeWeeks)
	players = read_players.json_read_players(players)
	schedule = read_schedule.json_read_schedule(schedule)
	teams = read_teams.json_read_teams(teams)


if __name__ == "__main__":
	read_from_json()
