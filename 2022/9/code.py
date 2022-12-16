with open("input.txt", "r") as file:
    data = [line.strip().split(" ") for line in file.readlines()]

def needToMove(head, tail) -> bool:
    return abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
        
def moveKnots(knots, visited):
    for i in range(len(knots) - 1):
        if needToMove(knots[i], knots[i + 1]):
            dix = sign(knots[i][0] - knots[i + 1][0])
            diy = sign(knots[i][1] - knots[i + 1][1])
            knots[i + 1] = (knots[i + 1][0] + dix, knots[i + 1][1] + diy)
            #Add the new point to the list if its the tail
            if i == len(knots) - 2:
                visited.append(knots[i + 1])

def solution(knots):
    knots = [(0, 0) for _ in range(knots)] 
    visited = []
    for line in data:
        for i in range(int(line[1])):
            hx, hy = knots[0][0], knots[0][1]
            if line[0] == "R":
                hx += 1
            elif line[0] == "L":
                hx -= 1
            elif line[0] == "U":
                hy += 1
            elif line[0] == "D":
                hy -= 1
            knots[0] = (hx, hy)
            #Check if I need to move knot behind
            moveKnots(knots, visited)
    return set(visited)

print(f"part 1: {len(solution(2)) + 1}")
print(f"part 2: {len(solution(10)) + 1}")