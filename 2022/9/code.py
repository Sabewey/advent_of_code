with open("input.txt", "r") as file:
    data = [line.strip().split(" ") for line in file.readlines()]


def moveHeadtoTail(head, tail) -> bool:
    return abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

hx, tx, hy, ty = 0, 0, 0, 0
tVisited = []
for line in data:
    for i in range(int(line[1])):
        if line[0] == "R":
            hx += 1
        elif line[0] == "L":
            hx -= 1
        elif line[0] == "U":
            hy += 1
        elif line[0] == "D":
            hy -= 1
        if moveHeadtoTail((hx, hy), (tx, ty)):
            dix = sign(hx - tx)
            diy = sign(hy - ty)
            tx += dix
            ty += diy
            #Add the new point to the list
            tVisited.append((tx, ty))
print(len(set(tVisited)) + 1)