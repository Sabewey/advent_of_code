with open("C:/Users/erikb/programming/lek/advent_of_code/2023/18/input.txt", "r") as f:
    instructions = f.read().splitlines()

lines = []
grid = [[0 for i in range(10000)] for j in range(10000)]
x, y = 5000, 5000
for instruction in instructions:
    d, n, col = instruction.split()
    lines.append(int(n))
    if d == "U":
        for i in range(int(n)):
            grid[y][x] = 1
            y -= 1
    elif d == "D":
        for i in range(int(n)):
            grid[y][x] = 1
            y += 1
    elif d == "L":
        for i in range(int(n)):
            grid[y][x] = 1
            x -= 1
    elif d == "R":
        for i in range(int(n)):
            grid[y][x] = 1
            x += 1

def flood_fill_count(grid, x, y, visited):
    if grid[y][x] == 1:
        return 0

    count = 0
    stack = [(x, y)]
    while stack:
        nx, ny = stack.pop()
        if ny < 0 or ny >= len(grid) or nx < 0 or nx >= len(grid[0]) or visited[ny][nx] or grid[ny][nx] == 1:
            continue
        visited[ny][nx] = True
        count += 1
        stack.extend([(nx+1, ny), (nx-1, ny), (nx, ny+1), (nx, ny-1)])
    return count

def count_nbr(grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    return flood_fill_count(grid, 5010, 5005, visited)

#Part 1
print(sum(lines) + count_nbr(grid))


