with open("c:/Users/erikb/programming/lek/advent_of_code/2024/04/input.txt", "r") as f:
    grid = [[col for col in line.strip()] for line in f.readlines()]


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# This should work but doens't
# def check_sequence(grid, r, c, dr, dc):
#     nr, nc = r + dr, c + dc
#     if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] == "M":
#         nr += dr
#         nc += dc
#         if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] == "A":
#             nr += dr
#             nc += dc
#             if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] == "S":
#                 return True
#     return False

# count = 0
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == "X":
#             for dr, dc in DIRECTIONS:
#                 if check_sequence(grid, i, j, dr, dc):
#                     count += 1
#                     break

# This works :/
count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        r, c = i, j
        if grid[r][c] == "X":
            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                    if grid[nr][nc] == "M":
                        # Check which direction the M is facing
                        if dr == 1 and dc == 0:
                            print("down")
                            # Look for the next letter in the same direction
                            nr += dr
                            nc += dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                if grid[nr][nc] == "A":
                                    # Look for the next letter in the same direction
                                    nr += dr
                                    nc += dc
                                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                        if grid[nr][nc] == "S":
                                            count += 1
                        elif dr == -1 and dc == 0:
                            print("up")
                            nr += dr
                            nc += dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                if grid[nr][nc] == "A":
                                    nr += dr
                                    nc += dc
                                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                        if grid[nr][nc] == "S":
                                            count += 1
                        elif dr == 0 and dc == 1:
                            print("right")
                            nr += dr
                            nc += dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                if grid[nr][nc] == "A":
                                    nr += dr
                                    nc += dc
                                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                        if grid[nr][nc] == "S":
                                            count += 1
                        elif dr == 0 and dc == -1:
                            print("left")
                            nr += dr
                            nc += dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                if grid[nr][nc] == "A":
                                    nr += dr
                                    nc += dc
                                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                        if grid[nr][nc] == "S":
                                            count += 1
                        elif dr == 1 and dc == 1:
                            print("downright")
                            nr += dr
                            nc += dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                if grid[nr][nc] == "A":
                                    nr += dr
                                    nc += dc
                                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                        if grid[nr][nc] == "S":
                                            count += 1
                        elif dr == -1 and dc == -1:
                            print("upleft")
                            nr += dr
                            nc += dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                if grid[nr][nc] == "A":
                                    nr += dr
                                    nc += dc
                                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                        if grid[nr][nc] == "S":
                                            count += 1
                        elif dr == 1 and dc == -1:
                            print("downleft")
                            nr += dr
                            nc += dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                if grid[nr][nc] == "A":
                                    nr += dr
                                    nc += dc
                                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                        if grid[nr][nc] == "S":
                                            count += 1
                        elif dr == -1 and dc == 1:
                            print("upright")
                            nr += dr
                            nc += dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                if grid[nr][nc] == "A":
                                    nr += dr
                                    nc += dc
                                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
                                        if grid[nr][nc] == "S":
                                            count += 1

print(f"Part 1: {count}")


# Part 2
d = {
    "MS": "MS",
    "SM": "SM",
    "MM": "SS",
    "SS": "MM",
}

count2 = 0
for r in range(len(grid)):
    for c in range(len(grid[i])):
        if grid[r][c] == "A":
            if 0 < r < len(grid)-1 and 0 < c < len(grid[r])-1:
                top = grid[r-1][c-1] + grid[r-1][c+1]
                bottom = grid[r+1][c-1] + grid[r+1][c+1]
                if top in d:
                    if d[top] == bottom:
                        count2 += 1
                elif bottom in d:
                    if d[bottom] == top:
                        count2 += 1

print(f"Part 2: {count2}")