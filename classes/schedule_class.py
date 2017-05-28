class Schedule:
	current_week = 0
	total_weeks = 17

	def __init__(self, gameId, gameWeek, gameDate, awayTeam, homeTeam, gameTimeET, tvStation, winner):
		self.gameId = gameId
		self.gameWeek = gameWeek
		self.gameDate = gameDate
		self.awayTeam = awayTeam
		self.homeTeam = homeTeam
		self.gameTimeET = gameTimeET
		self.tvStation = tvStation
		self.winner = winner

	def set_current_week(current_week):
		self.current_week = current_week