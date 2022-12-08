with open("input.txt", "r") as f:
    data = [ [ int(c) for c in row.strip() ] for row in f.readlines() ]

def column(grid, j, start = 0, end = len(data)) -> list:
    return [row[j] for row in grid[start:end]]

#Part 1
def visible(n, xs) -> bool:
    for x in xs:
        if x >= n:
            return False
    return True

size = len(data)
sum = 0
for r in range(1, size - 1):
    for c in range(1, size - 1):
        if visible(data[r][c], data[r][:c]) or visible(data[r][c], data[r][c+1:]) or \
             visible(data[r][c], column(data, c, end=r)) or visible(data[r][c], column(data, c, start=r+1)):
             sum += 1
sum += size * 4 - 4 #Add the edges
print(f"Part 1: {sum}")


#Part 2
def scored(height, arr) -> int:
    count = 0
    for i in arr:
        count += 1
        if i >= height:
            break
    return count


maxScore = 0
for r in range(1, size - 1):
    for c in range(1, size - 1):
        currHeight = data[r][c]
        left = scored(currHeight, data[r][:c][::-1])
        right = scored(currHeight, data[r][c + 1:])
        up = scored(currHeight, column(data, c, end=r)[::-1])
        down = scored(currHeight, column(data, c, start=r+1))
        score = left * right * up * down
        if score > maxScore:
            maxScore = score

print(f"Part 2: {maxScore}")