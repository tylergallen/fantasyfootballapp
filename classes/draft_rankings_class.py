class DraftRanking:
	totalNumber = 0

	def __init__(self, playerId, position, displayName, fName, lName, team, byeWeek, standDev, nerdRank, positionRank, overallRank):
		self.playerId = playerId
		self.position = position
		self.displayName = displayName
		self.fName = fName
		self.lName = lName
		self.team = team
		self.byeWeek = byeWeek
		self.standDev = standDev
		self.nerdRank = nerdRank
		self.positionRank = positionRank
		self.overallRank = overallRank

		DraftRanking.totalNumber += 1

