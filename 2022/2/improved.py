def input(filename):
    with open(filename, 'r') as input_file:
        data = [ tuple(line.strip().split(" ")) for line in input_file.readlines() ]
    return data

P = { "X": 1, "Y": 2, "Z": 3, "win": 6, "draw": 3, "loose": 0 } # Points

game_scores = {
    ("A", "X"): P["draw"] + P["X"], # Rock vs Rock = Draw
    ("A", "Y"): P["win"] + P["Y"],
    ("A", "Z"): P["loose"] + P["Z"],
    ("B", "X"): P["loose"] + P["X"],
    ("B", "Y"): P["draw"] + P["Y"],
    ("B", "Z"): P["win"] + P["Z"],
    ("C", "X"): P["win"] + P["X"],
    ("C", "Y"): P["loose"] + P["Y"],
    ("C", "Z"): P["draw"] + P["Z"],
}

game_rules = {
    ("A", "X"): "Z",
    ("A", "Y"): "X",
    ("A", "Z"): "Y",
    ("B", "X"): "X",
    ("B", "Y"): "Y",
    ("B", "Z"): "Z",
    ("C", "X"): "Y",
    ("C", "Y"): "Z",
    ("C", "Z"): "X",
}

data = input("input.txt")
print(data)

def part_1(data):
    points = 0
    for game in data:
        points += game_scores[game]
    return points

def part_2(data):
    points = 0
    for game in data:
        points += game_scores[game[0], game_rules[game]]
    return points

print(part_1(data))
print(part_2(data))