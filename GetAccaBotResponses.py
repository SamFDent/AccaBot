from AccaBot import getResponseData
import pprint
from collections import Counter

# Get the response form data
preds = getResponseData()
# pp = pprint.PrettyPrinter()
# pp.pprint(preds)

# Create dictionary with each Betting Market as a Key, then have sub-dictionaries as values
# for each Home Team that is encountered and a frequency count as their value
# e.g.
# {
#     "Over 2.5 Goals": {
#         "AFC Wimbledon": 1
#     },
#     "Home Win": {
#         "Man United": 1
#     },
#     "BTTS": {
#         "Everton": 4,
#         "Arsenal": 2
#     }
# }

parsed_dict = dict()
for dictionary in preds:
    bet = dictionary['Bet']
    if bet not in parsed_dict.keys():
        parsed_dict[bet] = dict()
    if dictionary['Home Team'] not in parsed_dict[bet].keys():
        parsed_dict[bet][dictionary['Home Team']] = 0
    parsed_dict[bet][dictionary['Home Team']] += 1

# print(parsed_dict)

for bet in parsed_dict.keys():
    market = bet
    selection = ""
    frequency = 0
    for team in parsed_dict[bet].keys():
        if parsed_dict[bet][team] > frequency:
            selection = team
            frequency = parsed_dict[bet][team]

    print(f"{market} - {selection}")
    # print(market)
    # print(selection)
    # print(frequency)
