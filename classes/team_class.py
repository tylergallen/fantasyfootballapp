class Team:
	number_of_teams = 0

	def __init__(self, code, fullName, shortName):
		self.code = code
		self.fullName = fullName
		self.shortName = shortName
		Team.number_of_teams += 1

	def display_number_of_teams():
		print (f'Total number of teams in the NFL: {number_of_teams}')