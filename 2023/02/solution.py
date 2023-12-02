with open("input.txt", "r") as f:
    data = [line.strip().split(";") for line in f.readlines()]

# 12r 13g 14b
nbr_cubes = {'red': 12, 'green': 13, 'blue': 14}
impossible = set()

res2 = 0
for i, game in enumerate(data):
    max_dict = {"red":0, "green":0, "blue":0}
    for cube_set in game:
        if ':' in cube_set:
            cube_set = cube_set[cube_set.find(':')+1:].strip()

        count_dict = {'red': 0, 'green': 0, 'blue': 0}
        cubes = cube_set.split(", ")
        for cube in cubes:
            parts = cube.split()
            if len(parts) == 2:
                count, color = parts
                count_dict[color] = int(count)
                if count_dict[color] > max_dict[color]:
                    max_dict[color] = count_dict[color]
            else:
                print(f"Unexpected format in cube string: {cube}")
        for color in count_dict:
            if count_dict[color] > nbr_cubes[color]:
                impossible.add(i + 1)
                break
    power = 1
    for nbr in max_dict.values():
        power *= nbr
    res2 += power

all_nbr = list(range(1, len(data) + 1))
res = sum([nbr for nbr in all_nbr if nbr not in impossible])
print(res)
print(res2)