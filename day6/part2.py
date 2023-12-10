import re

# multiples pointers could still work
# otherwise, binary search start and end of working solutions


def find_solutions(time, min_distance):
    left = 1
    right = time - 1

    left_undetermined = True
    right_undetermined = True

    def is_boat_win(hold, run_time):
        if hold * run_time > min_distance:
            return True
        else:
            return False

    while left_undetermined or right_undetermined:
        if left_undetermined:
            if is_boat_win(left, time - left):
                left_undetermined = False
            else:
                left += 1
        if right_undetermined:
            if is_boat_win(right, time - right):
                right_undetermined = False
            else:
                right -= 1

    return right - left + 1


lines = [re.findall("\d+", line) for line in open("in.txt", "r")]

time = int("".join(lines[0]))
min_distance = int("".join(lines[1]))

solutions = find_solutions(time, min_distance)


print(solutions)
