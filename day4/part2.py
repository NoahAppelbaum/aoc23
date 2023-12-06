# Queue it up!
# get total number of points and extendh the lines list with slice from card idx to idx + points
# Ohhh, gotta track what the initial number of the card was when split
# Keep running counter through iteration

import re

lines = [line.strip() for line in open("in.txt", "r")]
length = len(lines)


def make_lists(line):
    split = line.split("|")
    card = int(re.findall("\d+(?=.*:)", split[0])[0])
    winners = re.findall("\d+(?!.*:)", split[0])
    given = re.findall("\d+", split[1])
    return (card, winners, given)



n_cards = {n:1 for n in range(1, len(lines) + 1)}

# ^ save here on first run, so that I don't have to iterate again.
for line in lines:
    (card, winners, given) = make_lists(line)
    points = 0

    records = {}
    for w in winners:
        records[w] = 1


    for n in given:
        if records.get(n):
            points += 1


    for c in range(card + 1, card + 1 + points):
        n_cards[c] += n_cards[card]

sum = 0
for c in n_cards:
    sum += n_cards[c]

print(sum)
