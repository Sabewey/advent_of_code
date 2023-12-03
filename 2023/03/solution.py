from collections import defaultdict

with open("C:/Users/erikb/programming/lek/advent_of_code/2023/03/input.txt", "r") as f:
    data = ["." + line.strip() + "." for line in f.readlines()]
    dot_row = "." * len(data[0])
    data = [dot_row] + data + [dot_row]

parts = []
gear_parts = defaultdict(list)
for row in range(1,len(data)):
    buffer = ""
    save = False
    add = False
    potential_gear = (None, None)
    for col in range(1, len(data[0])):
        if data[row][col].isdigit():
            # Check all adjacent squares
            for r2 in range(row-1, row+2):
                for c2 in range(col-1, col+2):
                    if not data[r2][c2].isdigit() and data[r2][c2] != '.':
                        if data[r2][c2] == '*':
                            potential_gear = (r2, c2)
                        save = True
                        add = True
            if data[row][col+1].isdigit():
                add = True
            if add:
                buffer += data[row][col]
        else:
            if len(buffer) != 0 and save:
                parts.append(int(buffer))
                save = False
                if potential_gear != (None, None):
                    gear_parts[potential_gear].append(int(buffer))
            potential_gear = (None, None)
            buffer = ""

#part1
print(sum(parts))

#part2
pwr = [value[0] * value[1] for key, value in gear_parts.items() if len(value) == 2]
print(sum(pwr))