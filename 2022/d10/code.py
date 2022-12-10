with open("input.txt", "r") as f:
    data = [line.strip().split(" ") for line in f.readlines()]

xValuesAtCycle = {241: 0}
x = 1
cycle = 0
for line in data:
    if line[0] == "noop":
       cycle += 1
       xValuesAtCycle[cycle] = x
    else:
        cycle += 1
        xValuesAtCycle[cycle] = x
        cycle += 1
        xValuesAtCycle[cycle] = x
        x += int(line[1])
print(sum(xValuesAtCycle[k] * k for k in range(20, 221, 40)))

string = ""
for r in range(6):
    for c in range(40):
        sign = "#" if abs(c - xValuesAtCycle[r*40+c+1]) <= 1 else "."
        string += sign
        if c == 39: string += "\n"
print(string)
