from tqdm import tqdm

with open("c:/Users/erikb/programming/lek/advent_of_code/2024/06/input.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

def find_start(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "^":
                return (i, j), (-1, 0) # Up
            elif cell == ">":
                return (i, j), (0, 1) # Right
            elif cell == "v":
                return (i, j), (1, 0) # Down
            elif cell == "<":
                return (i, j), (0, -1) # Left
    return None


def safe_get(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return True
    return False

def draw_path_in_grid(grid, start):
    (i, j), (dx, dy) = start
    seen = set()
    while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        # Mark the cell as visited
        seen.add((i, j))
        grid[i][j] = "X"
        # Check if we can move forward
        while safe_get(grid, i + dx, j + dy) and grid[i + dx][j + dy] == "#":
            dx, dy = dy, -dx # Turn right
        i += dx
        j += dy
    return grid, seen
start = find_start(grid)
grid_copy = [row.copy() for row in grid]
grid_copy, seen = draw_path_in_grid(grid_copy, start)

# Debugging function
def print_grid(grid):
    for row in grid:
        print("".join(row))
print_grid(grid_copy)

print(f"Part One: {len(seen)}")

# Part 2
def find_loops(grid, start):
    (i, j), (dx, dy) = start
    seen = set()
    while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        # Mark the cell as visited
        seen.add((i, j, dx, dy))
        # Check if we can move forward
        while safe_get(grid, i + dx, j + dy) and grid[i + dx][j + dy] == "#":
            dx, dy = dy, -dx # Turn right
        i += dx
        j += dy
        if (i, j, dx, dy) in seen:
            return True
    return False

count = 0
start = find_start(grid)
for (i, j) in tqdm(seen):
    if grid[i][j] == ".":
        grid[i][j] = "#"
        if find_loops(grid, start):
            count += 1
        grid[i][j] = "."
print(f"Part 2: {count}")
