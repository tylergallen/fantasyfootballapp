class Player:
	number_of_players = 0
	number_of_active_players = 0

	def __init__(self, playerId, active, jersey, lname, fname, displayName, team, position, height, weight, dob, college):
		self.playerId = playerId
		self.active = active
		self.jersey = jersey
		self.lname = lname
		self.fname = fname
		self.displayName = displayName
		self.team = team
		self.position = position
		self.height = height
		self.weight = weight
		self.dob = dob
		self.college = college

		Player.number_of_players += 1
		if active == "1":
			Player.number_of_active_players += 1
	
	def display_number_of_active_players():
		print (f'Total number of active players currently in the NFL: {number_of_active_players}')