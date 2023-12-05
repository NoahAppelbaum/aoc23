symbols = "!@#$%^&*+=/-"
lines = [line.strip() for line in open("in.txt", "r")]

sum = 0

current_num = ""
num_start = 0



def check_symbols(line_num, end = 0):
    r_boundary = 1 if len(lines[0]) - 1 > num_start + len(current_num) else 0

    if num_start > 0:
        if lines[line_num][num_start - 1] in symbols:
            return True

    if lines[line_num][num_start + len(current_num) - end] in symbols:
        return True

    if line_num > 0:
        for idx in range(
            (num_start - 1 if num_start > 0 else num_start),
            num_start + len(current_num) + r_boundary
        ):
            if lines[line_num-1][idx] in symbols:
                return True
    if line_num < len(lines) - 1:
        for idx in range(
            (num_start - 1 if num_start > 0 else num_start),
            num_start + len(current_num) + r_boundary
        ):
            if lines[line_num + 1][idx] in symbols:
                return True

    return False

for l in range(0, len(lines)):
    print("Looking at line", l)
    line = lines[l]
    for i in range(0, len(line)):
        if line[i].isnumeric():
            if not current_num:
                num_start = i
            current_num += line[i]
            if i == len(line) -1:
                print("checking num:", current_num)
                if check_symbols(l, end = 1):
                    print("Adding", current_num)
                    sum += int(current_num)
                current_num = ""
        else:
            if current_num:
                print("checking num:", current_num)
                if check_symbols(l):
                    print("Adding", current_num)
                    sum += int(current_num)
            current_num = ""

print(sum)
