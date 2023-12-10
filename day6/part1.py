import re

# grab digits -- two lists: time and min distance
# for each index, calc total solutions
#   -multiple pointers! min and max -- run, find last and first success and calc solutions
# keep running product of working solutions
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

product = 1

for i in range(0, len(lines[0])):
    time = int(lines[0][i])
    min_distance = int(lines[1][i])

    solutions = find_solutions(time, min_distance)

    product *= solutions


print(product)
