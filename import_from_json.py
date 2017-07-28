from json_reads import read_byeWeeks
from json_reads import read_players
from json_reads import read_schedule
from json_reads import read_teams
from json_reads import read_draft_rankings
from json_reads import read_draft_projections
from json_reads import read_draft_tier
import sqlite3
import os

def read_draft_from_json():
	players = []
	schedule = []
	teams = []
	draft_rankings = []
	bye_week = []
	projections_rb = []
	projections_wr = []
	projections_qb = []
	projections_te = []
	projections_def = []
	projections_k = []
	draft_tier = []
	#Creating the lists of Classes that will be used throughout this program
	teams = read_teams.json_read_teams(teams)
	bye_week = read_byeWeeks.json_read_byeweek(teams)
	players = read_players.json_read_players(players)
	schedule = read_schedule.json_read_schedule(schedule)
	draft_rankings = read_draft_rankings.json_read_draft_rankings(draft_rankings)
	projections_def = read_draft_projections.json_read_draftprojections_def(projections_def)
	projections_qb = read_draft_projections.json_read_draftprojections_qb(projections_qb)
	projections_wr = read_draft_projections.json_read_draftprojections_wr(projections_wr)
	projections_rb = read_draft_projections.json_read_draftprojections_rb(projections_rb)
	projections_te = read_draft_projections.json_read_draftprojections_te(projections_te)
	projections_k = read_draft_projections.json_read_draftprojections_k(projections_k)
	draft_tier = read_draft_tier.json_read_draft_tier(draft_tier)

	print("Read everything from website properly")

	if os.path.isfile('trial.db'):
		purge_database()

	create_draft_table()
	fill_database(players, draft_rankings, projections_def, projections_te, projections_k, projections_qb, projections_wr, projections_rb, draft_tier)
	print_entire_database()

def create_draft_table():
	#Opening the DATABASE
	conn = sqlite3.connect('trial.db')
	c = conn.cursor()

	#Create Tables
	c.execute('''CREATE TABLE players (playerId PRIMARY KEY, displayName, fName, lName, position, dob, team, byeWeek, tier, positionRank, overallRank)''')
	c.execute('''CREATE TABLE projection_qb (playerId REFERENCES players(playerId), completions, attempts, passingYards, passingTds, passingInts, rushAtt, rushYards, rushTds, fumbles, fantasyPoints)''')
	c.execute('''CREATE TABLE projection_def (playerId REFERENCES players(playerId), sacks, interceptions, fumbleRec, td, specialTeamTd, fantasyPoints)''')
	c.execute('''CREATE TABLE projection_k (playerId REFERENCES players(playerId), xp, fg, fantasyPoints)''')
	c.execute('''CREATE TABLE projection_wr (playerId REFERENCES players(playerId), rushAtt, rushYards, rushTds, fumbles, rec, recYards, recTd, fantasyPoints)''')
	c.execute('''CREATE TABLE projection_rb (playerId REFERENCES players(playerId), rushAtt, rushYards, rushTds, fumbles, rec, recYards, recTd, fantasyPoints)''')
	c.execute('''CREATE TABLE projection_te (playerId REFERENCES players(playerId), rushAtt, rushYards, rushTds, fumbles, rec, recYards, recTd, fantasyPoints)''')

	print ('Tables created correctly')
	conn.commit()
	conn.close()

def fill_database(players, draft_rankings, projections_def, projections_te, projections_k, projections_qb, projections_wr, projections_rb, draft_tier):
	conn = sqlite3.connect('trial.db')
	c = conn.cursor()

	for i in players:
		if i.active == '1':
			c.execute('INSERT INTO players (playerId, displayName, fName, lName, position, dob, team) VALUES(?, ?, ?, ?, ?, ?, ?)', (i.playerId, i.displayName, i.fname, i.lname,i .position, i.dob, i.team))

	print('Stored into tables properly (hopefully)')
	
	conn.commit()
	conn.close()

def purge_database():
	os.remove('trial.db')
	print('Deleted the db file')

def print_entire_database():
	conn = sqlite3.connect('trial.db')
	c = conn.cursor()
	c.execute('SELECT * FROM players')
	rows = c.fetchall()
	for row in rows:
		print(row)

	conn.commit()
	conn.close()
	

if __name__ == "__main__":
	read_draft_from_json()


