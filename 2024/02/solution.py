with open("c:/Users/erikb/programming/lek/advent_of_code/2024/02/input.txt", "r") as f:
    data = [[int(x) for x in line.strip().split()] for line in f.readlines()]

def safe(line):
    old_flag = 0
    for i in range(len(line)-1):
        a = line[i]
        b = line[i+1]

        if abs(a-b) > 3 or abs(a-b) == 0:
            return False

        if a-b > 0:
            flag = 1
        else:
            flag = -1

        if old_flag == 1 and a-b < 0:
            return False
        if old_flag == -1 and a-b > 0:
            return False
        old_flag = flag
    return True

safe_count = 0
for line in data:
    if safe(line):
        safe_count += 1
print(f"Part One: {safe_count}")

# part 2: if removing one element makes the list safe, remove it
safe_count = 0
for line in data:
    for i in range(len(line)):
        if safe(line[:i] + line[i+1:]):
            safe_count += 1
            break
print(f"Part two: {safe_count}")

