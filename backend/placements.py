def genPlacement(placementNum, teamName):
    return {
    "date": "2025-10-05 11:00:00",
    "placement": f"{placementNum}",
    "prizemoney": 1000000,
    "opponentname": f"{teamName}",
    "opponenttype": "team",
    "opponentplayers": {},
    "lastvsdata": {
        "opponenttype": "team",
        "opponentname": "Fnatic",
        "score": 2
    },
    "qualifier": "Americas Stage 2 (#2)",
    "wiki": "valorant"
    }
def genTournament(tournamentName, participantCount):
    placList=[]
    for t in range(participantCount):
        placList.append(genPlacement(t, ""+str(t)))
    return placList