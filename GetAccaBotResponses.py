from AccaBot import getResponseData
import pprint
from collections import Counter

# Get the response form date
preds = getResponseData()
pp = pprint.PrettyPrinter()
# pp.pprint(preds)

# Process the data - create list of strings from selections
selection_ls = []
for dict in preds:
    sel_string = ('{} v {}: {}'.format(dict.get('Home Team'),dict.get('Away Team'),dict.get('Bet')))
    selection_ls.append(sel_string)

# this code gets the most common x strings from the list of user provided selections where the bet is a BTTS bet.
# Capture this is a function then call for each market
# Save results back to Google Sheets for tweeting out later on
# print(selection_ls)

# BTTS
btts = [s for s in selection_ls if "BTTS" in s]
best_bet = Counter(btts).most_common(3)
print(best_bet)

# Home Win
home_win = [s for s in selection_ls if "Home Win" in s]
best_bet = Counter(home_win).most_common(3)
print(best_bet)

# Over 2.5 Goals
two_or_more = [s for s in selection_ls if "Over 2.5 Goals" in s]
best_bet = Counter(two_or_more).most_common(3)
print(best_bet)
