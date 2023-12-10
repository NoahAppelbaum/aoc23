import re


def destination_to_source(input, map):
    """Finds appropriate output based on map rules:
    [Source start, Destination start, range],
    where in->out if no range is found
    """

    for entry in map:
        [destination_start, source_start, rang] = entry

        if destination_start <= input < (destination_start + rang):
            return source_start + input - destination_start

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
seeds = [int(el) for el in re.findall("\d+", lines[0])] #start, range, ...
maps = parse_maps(lines[2:])



def test_locations():
    """serially test locations for possible seeds up the line"""

    location = 0
    while True:
        val = location
        print("checking location", val)
        for i in range(len(maps) - 1, -1, -1):
            val = destination_to_source(val, maps[i])

        for i in range(0, len(seeds), 2):
            seed = seeds[i]

            if seed <= val < (seed + seeds[i+1]):
                return location

        location += 1

print(test_locations())


# Go backwards!
# lowest location on up through the chain, at the top check against seed ranges

# ....CAN I BINARY SEARCH? Uh... probably not actually. Well... maybe yes??
#       No, because the seed data is not ordered relative to location output?
#           Like 4 location could be not present in the seeds, but 2 could be, and 1 could not
