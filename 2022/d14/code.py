#No time for cleanup right now, but here is the code with comments for part 1 and 2.
#Part 1: How many sand grains will settle? without floor
#Part 2: How many sand grains will settle? with floor

with open("input.txt", "r") as f:
    size = 1000 #Guessing the size of the matrix, its fine since the cave is roughly 500x500
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    paths = [[tuple.strip().split(",") for tuple in line.split(" -> ")] for line in f.readlines()]
    
def create_path(path):
    maxDepth = 0
    dx, dy = 0, 0
    #eg: path = [['498', '4'], ['498', '6'], ['496', '6']]
    while len(path) > 1:
        src = path.pop(0)
        maxDepth = max(maxDepth, int(src[1]))
        dst = path[0]
        if src[0] == dst[0]:
            dx = 0
            if src[1] < dst[1]:
                dy = 1
            else:
                dy = -1
        else:
            dy = 0
            if src[0] < dst[0]:
                dx = 1
            else:
                dx = -1
        r, c = int(src[0]), int(src[1])
        while (r, c) != (int(dst[0]), int(dst[1])):
            matrix[r][c] = 1
            r += dx
            c += dy
        matrix[r][c] = 1 #Set the last one
    return maxDepth

def sand_fall_and_settles():
    dx, dy = 0, 1
    currPos = (500, 0)
    settled = False
    while not settled and (matrix[500][0] != 2):
        r, c = currPos
        if matrix[r][c+1] == 1 or matrix[r][c+1] == 2:
            if matrix[r-1][c+1] == 0:   #left side is free, so we go left
                dx, dy = -1, 1
            elif matrix[r+1][c+1] == 0: #left side is blocked, so we try right
                dx, dy = 1, 1
            else:                       #both sides are blocked, so we settle
                dx, dy = 0, 0
                settled = True
                matrix[r][c] = 2
        else:
            dx, dy = 0, 1
        currPos = (r+dx, c+dy)
    #Check if sand has reached the bottom
    # if (currPos[0] >= size-1) or (currPos[1] >= size-1):
    #     return False
    # return True
    #Check if sand has reached the top
    if currPos[0] == 500 and currPos[1] == 0:
        return False
    return True
    
#Draw the matrix - for debugging
def draw(xL, xR, yL, yR):
    for y in range(yL, yR+1):
        for x in range(xL, xR+1):
            if x == 500 and y == 0:
                print("+", end="")
            else:
                if matrix[x][y] == 1:
                    print("#", end="")
                elif matrix[x][y] == 2:
                    print("o", end="")
                else:
                    print(".", end="")
        print()

def main():
    #Creat paths
    maxDepth = 0
    for path in paths:
        maxDepth = max(maxDepth, create_path(path))
    
    #Create floor 2 lower than the max depth
    for x in range(size):
        matrix[x][maxDepth+2] = 1
    
    #Sand fall
    nbr = 0
    while sand_fall_and_settles():
        nbr += 1
        # draw(488, 512, 0, 11)
        # print("")
    print(nbr + 1) # +1 for the last sand that settles for part 2
main()