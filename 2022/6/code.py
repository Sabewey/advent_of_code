with open("input.txt", "r") as f:
    data = f.read()
    
def nDistinctChars(n):
    charList = []
    for c in data:
        charList.append(c)

        lastN = set(charList[-n:])
        if len(lastN) == n:
            print(len(charList))
            break

print("Part 1:")
nDistinctChars(4)
print("Part 2:")
nDistinctChars(14)