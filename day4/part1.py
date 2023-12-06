# check if in
# generate arrays with regex. Noice.

import re

lines = [line.strip() for line in open("in.txt", "r")]

def make_lists(line):
    split = line.split("|")
    winners = re.findall("\d+(?!.*:)",split[0])
    given = re.findall("\d+", split[1])
    print(winners)
    return (winners, given)

sum = 0
for line in lines:
    (winners, given) = make_lists(line)

    records = {}
    points = 0
    for w in winners:
        records[w] = 1

    for n in given:
        if records.get(n):
            points = 1 if points == 0 else points * 2

    sum += points

print(sum)
