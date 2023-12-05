# parse/split string
# Make a frequency counter for greatest number

def evaluate_dice(pulls):

    dice = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for pull in pulls:
        handfuls = pull.split(", ")
        for die in handfuls:
            [n, color] = die.split(" ")
            color = color.strip()
            if int(n) > dice[color]:
                dice[color] = int(n)

    return dice["red"] * dice["green"] * dice["blue"]


def test_games(file):
    sum = 0

    for game in open(file, "r"):
        pulls = game.split(": ")[1].split("; ")

        sum += evaluate_dice(pulls)

    print(sum)


test_games("input.txt")
