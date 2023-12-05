import math

numbers = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def make_string_list(file):
    """Makes a list of strings from break-separated text in a file"""

    contents = open(file, "r")
    return [word.strip() for word in contents]

def get_digit_sum(text):
    """returns the numeric sum of the first and last digit in a text string"""
    first = find_first_digit(text)
    last = find_last_digit(text)

    print("found first and last:", first, last)
    return int(first + last)

def find_first_digit(string):
    """finds first numeric digit in a string"""

    first = math.inf
    found = ""

    for key in numbers:
        idx = string.find(key)
        if (-1 < idx < first):
            first = idx
            found = key

    for i in range(0, len(string)):
        if string[i].isnumeric():
            if i < first:
                return string[i]
            else:
                return numbers[found]

    return numbers[found]

def find_last_digit(string):
    """finds last numeric digit in a string"""

    last = -math.inf
    found = ""

    for key in numbers:
        idx = string.rfind(key)
        if (-1 < idx > last):
            last = idx
            found = key

    for i in range(len(string) - 1, -1, -1):
        if string[i].isnumeric():
            if i > last:
                return string[i]
            else:
                return numbers[found]

    return numbers[found]


strings = make_string_list("in.txt")


sum = 0
entry_number = 1

for s in strings:
    print(entry_number)
    entry_number += 1

    new_val = get_digit_sum(s)
    sum += new_val

print(sum)
