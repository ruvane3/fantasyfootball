import numpy as np
from scipy.stats import norm

standings = {
    "FANtasy": [9, 1, 1174],
    "Emily's Team": [7, 3, 1105],
    "Run CMC": [6, 4, 1186],
    "League is Rigged": [6, 4, 1181],
    "Adam's Team": [6, 4, 1113],
    "James's Team": [5, 5, 1157],
    "Eat Lobster!": [5, 5, 1114],
    "Daniel's Team": [3, 7, 940],
    "Kyle's Team": [2, 8, 1005],
    "Christian's Team": [1, 9, 1026],
}

historicalPoints = {
    "FANtasy": [108, 129, 136, 82, 132, 107, 146, 101, 134, 98],
    "Emily's Team": [166, 127, 107, 107, 104, 109, 134, 86, 80, 86],
    "Run CMC": [140, 106, 125, 134, 115, 118, 105, 105, 131, 107],
    "League is Rigged": [94, 148, 165, 137, 102, 98, 128, 117, 118, 75],
    "Adam's Team": [127, 124, 102, 104, 101, 120, 112, 117, 104, 101],
    "James's Team": [99, 150, 135, 101, 122, 105, 127, 83, 136, 100],
    "Eat Lobster!": [110, 120, 130, 142, 101, 90, 107, 79, 97, 139],
    "Daniel's Team": [75, 148, 110, 77, 74, 75, 130, 79, 75, 97],
    "Kyle's Team": [81, 121, 105, 121, 81, 114, 83, 125, 90, 84],
    "Christian's Team": [95, 92, 101, 112, 119, 87, 104, 119, 130, 67]
}

meanStd = {
    "FANtasy": [0, 0],
    "Emily's Team": [0, 0],
    "Run CMC": [0, 0],
    "League is Rigged": [0, 0],
    "Adam's Team": [0, 0],
    "James's Team": [0, 0],
    "Eat Lobster!": [0, 0],
    "Daniel's Team": [0, 0],
    "Kyle's Team": [0, 0],
    "Christian's Team": [0, 0],
}

for team, data in historicalPoints.items():
    s = np.std(data)
    m = np.mean(data)
    meanStd[team] = [m, s]


# Set game results by changing -1 -> 0 for team1 victory or 1 for team2 victory
schedule = {
    11: [
        ["League is Rigged", "Run CMC", -1],
        ["Eat Lobster!", "Kyle's Team", -1],
        ["Daniel's Team", "Adam's Team", -1],
        ["James's Team", "Christian's Team", -1],
        ["Emily's Team", "FANtasy", -1],
    ],
    12: [
        ["League is Rigged", "Adam's Team", -1],
        ["Eat Lobster!", "Run CMC", -1],
        ["Daniel's Team", "Christian's Team", -1],
        ["James's Team", "FANtasy", -1],
        ["Emily's Team", "Kyle's Team", -1],
    ],
    13: [
        ["League is Rigged", "Christian's Team", -1],
        ["Eat Lobster!", "Adam's Team", -1],
        ["Run CMC", "Kyle's Team", -1],
        ["Daniel's Team", "FANtasy", -1],
        ["Emily's Team", "James's Team", -1],
    ],
    14: [
        ["League is Rigged", "FANtasy", -1],
        ["Eat Lobster!", "Christian's Team", -1],
        ["Daniel's Team", "Emily's Team", -1],
        ["James's Team", "Kyle's Team", -1],
        ["Adam's Team", "Run CMC", -1],
    ],
}

numSimulations = 20000
allSimilatedResults = []

for i in range(numSimulations):
    simulatedResults = {
        "FANtasy": [0, 0, 0],
        "Emily's Team": [0, 0, 0],
        "Run CMC": [0, 0, 0],
        "League is Rigged": [0, 0, 0],
        "Adam's Team": [0, 0, 0],
        "James's Team": [0, 0, 0],
        "Eat Lobster!": [0, 0, 0],
        "Daniel's Team": [0, 0, 0],
        "Kyle's Team": [0, 0, 0],
        "Christian's Team": [0, 0, 0],
    }

    for _, week in schedule.items():
        for matchup in week:
            team1 = matchup[0]
            team2 = matchup[1]
            forcewinner = matchup[2]

            simTeam1Score = np.random.normal(
                meanStd[team1][0], meanStd[team1][1])
            simTeam2Score = np.random.normal(
                meanStd[team2][0], meanStd[team2][1])

            # simulate game
            team1Won = 0
            team2Won = 0
            if forcewinner == -1:
                team1Won = 1 if simTeam1Score > simTeam2Score else 0
                team2Won = not team1Won
            else:
                # use the forced game result
                team1Won = 1 if forcewinner == 0 else 0
                team2Won = not team1Won

            # update simulation matchup
            prev = simulatedResults[team1]
            new = [prev[0] + team1Won, prev[1] +
                   team2Won, prev[2] + simTeam1Score]
            simulatedResults[team1] = new

            prev = simulatedResults[team2]
            new = [prev[0] + team2Won, prev[1] +
                   team1Won, prev[2] + simTeam2Score]
            simulatedResults[team2] = new

    allSimilatedResults.append(simulatedResults)


finalStandings = {
    "FANtasy": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Emily's Team": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Run CMC": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "League is Rigged": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Adam's Team": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "James's Team": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Eat Lobster!": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Daniel's Team": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Kyle's Team": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Christian's Team": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

for simulatedResult in allSimilatedResults:
    # [team, wins, points]
    unorderdTeams = []

    # add week 0 - 12 standings
    for team, data in standings.items():
        unorderdTeams.append(
            [team, data[0] + simulatedResult[team][0], data[2] + simulatedResult[team][2]])

    # see who wins the simulation by ordering by wins then points
    orderedTeams = sorted(unorderdTeams, key=lambda x: (-x[1], -x[2]))

    # update final standings
    for place in range(10):
        team = orderedTeams[place][0]
        finalStandings[team][place] += 1

print("{: <20}{: <8}{: <8}{: <8}{: <8}{: <8}{: <8}{: <8}{: <8}{: <8}{: <8}{: <12}".format(
    "Team", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Playoffs"))

for team in finalStandings:
    # total place finishes
    tpf = finalStandings[team]
    print("{: <20}{: <8.2%}{: <8.2%}{: <8.2%}{: <8.2%}{: <8.2%}{: <8.2%}{: <8.2%}{: <8.2%}{: <8.2%}{: <8.2%}{: <12.2%}".format(
        team, tpf[0] / numSimulations, tpf[1] / numSimulations, tpf[2] / numSimulations, tpf[3] / numSimulations, tpf[4] / numSimulations, tpf[5] / numSimulations, tpf[6] / numSimulations, tpf[7] / numSimulations, tpf[8] / numSimulations, tpf[9] / numSimulations, (tpf[0] + tpf[1] + tpf[2] + tpf[3]) / numSimulations))
