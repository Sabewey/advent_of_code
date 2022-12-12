with open("test.txt", "r") as f:
    data = [[ c for c in line.strip()] for line in f.readlines()]
    starts = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            curr = data[r][c]
            if curr == "S" or curr == "a":
                start = (r, c)
                starts.append(start)
                data[r][c] = "a"
            elif curr == "E":
                end = (r, c)
                data[r][c] = "z"

def isInBounds(r, c):
    return 0 <= r < len(data) and 0 <= c < len(data[0])

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def getNeighbors(r, c):
    neighbors = []
    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if isInBounds(nr, nc) and ord(data[nr][nc]) - ord(data[r][c]) <= 1:
            neighbors.append((nr, nc))
    return neighbors

def bfs(start, end):
    visited = set(start)
    queue = [(start, 0)]

    path = []
    res = 9999999
    while queue:
        curr, dist = queue.pop(0)
        path.append((curr, dist))
        if curr == end:
            res = dist
            return res
        for neighbor in getNeighbors(*curr):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return res

#print(bfs(start, end))
print(min(bfs(start, end) for start in starts))