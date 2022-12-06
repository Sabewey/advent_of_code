with open("input.txt", "r") as f:
    data = f.read()
    
def nDistinctChars(n):
    charList = []
    for c in data:
        charList.append(c)

        lastN = set(charList[-n:])
        if len(lastN) == n:
            return len(charList)

print("Part 1: " + str(nDistinctChars(4)))
print("Part 2: " + str(nDistinctChars(14)))