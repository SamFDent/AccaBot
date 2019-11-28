from AccaBot import getResponseData
import pprint
from collections import Counter

# Get the response form data
preds = getResponseData()
pp = pprint.PrettyPrinter()
# pp.pprint(preds)

# Create dictionary with each Betting Market as a Key, then have a sub-dictionary for each HomeTeam that is encounters
# and a count as the value
parsed_dict = dict()
for dictionary in raw_dicts:
    bet = dictionary['Bet']
    if bet not in parsed_dict.keys():
        parsed_dict[bet] = dict()
    if dictionary['Home Team'] not in parsed_dict[bet].keys():
        parsed_dict[bet][dictionary['Home Team']] = 0
    parsed_dict[bet][dictionary['Home Team']] += 1

most_frequent_bet = ""
most_frequent_team = ""
highest_frequency = 0
for bet in parsed_dict.keys():
    for team in parsed_dict[bet].keys():
        if parsed_dict[bet][team] > highest_frequency:
            most_frequent_bet = bet
            most_frequent_team = team
            highest_frequency = parsed_dict[bet][team]
            
            print(most_frequent_bet)
            print(most_frequent_team)
            print(highest_frequency)
