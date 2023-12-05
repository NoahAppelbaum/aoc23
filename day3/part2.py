lines = [line.strip() for line in open("in.txt", "r")]

sum = 0



def check_gear(line_num, i):
    r_boundary = 1 if len(lines[0]) - 1 > i + 1 else 0
    line = lines[line_num]

    nums = []

    if i > 0:
        if line[i - 1].isdigit():
            n = line[i - 1]
            j = i - 2
            while j > 0 and line[j].isdigit():
                n = line[j] + n
                j -= 1

            nums.append(n)

    if i + 1 < len(line):
        if line[i + 1].isdigit():
            n = line[i + 1]
            j = i + 2
            while j < len(line) and line[j].isdigit():
                n = n + line[j]
                j += 1

            nums.append(n)

    if line_num > 0:
        for idx in range(
            (i - 1 if i > 0 else i),
            i + 1 + r_boundary
        ):
            if lines[line_num-1][idx].isdigit():
                n = lines[line_num-1][i + 1]
                j = i + 2
                while j < len(lines[line_num-1]) and lines[line_num-1][j].isdigit():
                    n = n + lines[line_num-1][j]
                    j += 1
                j = i - 2
                while j > 0 and lines[line_num-1][j].isdigit():
                    n = lines[line_num-1][j] + n
                    j -= 1

                nums.append(n)
                break

    if line_num < len(lines) - 1:
        for idx in range(
            (i - 1 if i > 0 else i),
            i + 1 + r_boundary
        ):
            if lines[line_num + 1][idx].isdigit():
                n = lines[line_num + 1][i + 1]
                j = i + 2
                while j < len(lines[line_num + 1]) and lines[line_num + 1][j].isdigit():
                    n = n + lines[line_num + 1][j]
                    j += 1
                j = i - 2
                while j > 0 and lines[line_num + 1][j].isdigit():
                    n = lines[line_num + 1][j] + n
                    j -= 1

                nums.append(n)
                break

    print("nums looking like", nums)

    if len(nums) == 2:
        return int(nums[0]) * int(nums[1])
    else:
        return 0


for l in range(0, len(lines)):
    print("Looking at line", l)
    line = lines[l]
    for i in range(0, len(line)):
        if line[i] == "*":
            sum += check_gear(l, i)

print(sum)
