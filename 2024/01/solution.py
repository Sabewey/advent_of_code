from collections import defaultdict

with open("c:/Users/erikb/programming/lek/advent_of_code/2024/01/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

a = []
b = []
for line in data:
    split = line.split(" ")
    a.append(int(split[0]))
    b.append(int(split[-1]))

a.sort()
b.sort()
nbr_count_b = defaultdict(int)
for nbr in b:
    nbr_count_b[nbr] += 1


dist = 0
sim_score = 0
while len(a) > 0:
    distance = abs(a[0] - b[0])
    dist += distance 
    nbr = a.pop(0)
    b.pop(0)

    sim_score += nbr_count_b[nbr] * nbr

print(f"Part One: {dist}")
print(f"Part Two: {sim_score}")