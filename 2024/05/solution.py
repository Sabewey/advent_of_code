from collections import defaultdict

with open("c:/Users/erikb/programming/lek/advent_of_code/2024/05/input.txt", "r") as f:
    content = f.read().strip()

rules, updates = content.split("\n\n")
rules = [(int(a), int(b)) for a, b in [rule.split("|") for rule in rules.split("\n")]]
updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

before_mapping = defaultdict(set)
for rule in rules:
    before_mapping[rule[0]].add(rule[1])

# Part 1
count = 0
incorrect_rows = []
for row in updates:
    reverse = row[::-1]
    valid = True
    for i, e in enumerate(reverse):
        rest_set = set(reverse[i+1:])
        before = before_mapping[e]
        if before.intersection(rest_set):
            valid = False
            incorrect_rows.append(row)
            break
    if valid:
        count += row[len(row)//2]
print(f"Part one {count}")


# Part 2
count = 0
corrected_rows = []
for row in incorrect_rows:
    corrected = False
    while not corrected:
        corrected = True
        reverse = row[::-1]
        for i, e in enumerate(reverse):
            rest_set = set(reverse[i+1:])
            after = before_mapping[e]
            if after.intersection(rest_set):
                pos = row.index(e)
                for j in range(pos):
                    if row[j] in after:
                        row.insert(pos, row.pop(j))
                        corrected = False
    corrected_rows.append(row)
    count += row[len(row)//2]
print(f"Part two: {count}")