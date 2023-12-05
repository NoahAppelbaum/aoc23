# access file
# split into strings
# for each string:
#   multiple pointers until two digits found (or else last = first)
#       -> keep running sum

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
    for char in string:
        if char.isnumeric():
            return char

def find_last_digit(string):
    """finds last numeric digit in a string"""
    for i in range(len(string) - 1, -1, -1):
        if string[i].isnumeric():
            return string[i]

# strings = make_string_list("in.txt")


# sum = 0

# for s in strings:
#     new_val = get_digit_sum(s)
#     sum += new_val

# print(sum)
