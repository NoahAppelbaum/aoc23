import re
import math

def source_to_destination(input, map):
    """Finds appropriate output based on map rules:
    [Source start, Destination start, range],
    where in->out if no range is found
    """

    for entry in map:
        [destination_start, source_start, rang] = entry

        if source_start <= input < (source_start + rang):
            return destination_start + input - source_start

    return input


def parse_maps(text):
    """parse source-destination maps from text input. Outputs a list of matrices
    """
    out = []
    map = []
    for line in text:
        current = [int(el) for el in re.findall("\d+", line)]

        if not len(current):
            if len(map):
                out.append(map)
                map = []
        else:
            map.append(current)

    map.append(current)
    out.append(map)

    return out


lines = [line.strip() for line in open("in.txt", "r")]
seeds = [int(el) for el in re.findall("\d+", lines[0])]
maps = parse_maps(lines[2:])

# logic logic logic -- go through maps for each seed, save lowest ultimate output
lowest = math.inf

for seed in seeds:
    print("starting with seed", seed)
    val = seed
    for i in range(0,len(maps)):
        val = source_to_destination(val, maps[i])
        print("map outputs:", val)

    if val < lowest:
        lowest = val

print(lowest)
