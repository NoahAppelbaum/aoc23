# parse/split string
# Make a frequency counter for greatest number

dice = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def evaluate_dice(pulls):
    for pull in pulls:
        handfuls = pull.split(", ")
        for die in handfuls:
            [n, color] = die.split(" ")
            color = color.strip()
            print("looking at", n, color, "dice")
            if color not in dice:
                print("failing because", color, "is not in dice.")
                return False
            if dice[color] < int(n):
                print("failing because", n, "is too many", color, "dice")
                return False

    return True

def test_games(file):
    counter = 1
    sum = 0

    for game in open(file, "r"):
        print("Game", counter)
        pulls = game.split(": ")[1].split("; ")

        if (evaluate_dice(pulls)):
            sum += counter

        counter += 1

    print(sum)


test_games("input.txt")
