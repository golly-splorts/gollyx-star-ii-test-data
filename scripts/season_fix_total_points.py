import json

season0 = 2

with open(f'season{season0}/season.json', 'r') as f:
    season = json.load(f)

tp = {}

first_day = season[0]
for game in first_day:
    tp[game['team1Abbr']] = 0
    tp[game['team2Abbr']] = 0

for day in season:
    for i, game in enumerate(day):

        t1abbr = game['team1Abbr']
        t2abbr = game['team2Abbr']

        if i > 0:
            game['team1TotalPoints'] = tp[t1abbr]
            game['team2TotalPoints'] = tp[t2abbr]

        t1p = game['team1Score']
        t2p = game['team2Score']

        if t1abbr not in tp:
            tp[t1abbr] = t1p
        else:
            tp[t1abbr] += t1p

        if t2abbr not in tp:
            tp[t2abbr] = t2p
        else:
            tp[t2abbr] += t2p

with open(f'season{season0}/new_season.json', 'w') as f:
    json.dump(season, f, indent=4)
