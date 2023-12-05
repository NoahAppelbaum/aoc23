import re

lines = ["." + line.strip() + "." for line in open("in.txt", "r")]
lines.insert(0, '{message:<{width}}'.format(message="", width=len(lines[1])))
lines.append('{message:<{width}}'.format(message="", width=len(lines[1])))


# id star locations, then go through and search numbers around those points

stars = []
for y in range(0, len(lines)):
    res = re.finditer("[*]", lines[y])
    for match in res:
        stars.append((y, match.start()))


# Make iterable of numbers -- separated by line? (y), then contained like (start, end, n)

numbers = []
for y in range(0, len(lines)):
    matches = re.finditer("\d+", lines[y])
    numbers.append([
        (match.start(), match.end(), int(match.group())) for match in matches
    ])


# find numbers in range of *'s
sum = 0
for (y, x) in stars:

    touching = []
    for row in range(y - 1, y + 2):
        touching += [
            n for (start, end, n) in numbers[row] if
            x - 2 < start < x + 2 or
            x - 1 < end < x + 2
        ]
    if len(touching) == 2:
        sum += touching[0] * touching[1]

    print("the star at", (x, y), "is touching", touching)

print(sum)
