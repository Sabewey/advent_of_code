with open("input.txt", "r") as f:
    lines = f.readlines()
    #Remove every third line
    data = [eval(line.strip()) for line, idx in zip(lines, range(len(lines))) if idx % 3 != 2]

def compareElements(a, b):
    if isinstance(a, list) and isinstance(b, list):
        return compareLists(a, b)
    elif isinstance(a, list) and isinstance(b, int):
        return compareLists(a, [b])
    elif isinstance(a, int) and isinstance(b, list):
        return compareLists([a], b)
    else:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

def compareLists(a, b):
    maxIndex = min(len(a), len(b))
    for i in range(maxIndex):
        diff = compareElements(a[i], b[i])
        if diff == -1:
            return -1
        elif diff == 1:
            return 1
    lenDiff = len(a) - len(b)
    if lenDiff == 0:
        return 0
    elif lenDiff < 0:
        return -1
    else:
        return 1

(two, six) = ([[2]], [[6]])
lessThanTwo = 0
lessThanSix = 0
rightIndexes = []
index = 1
for i in range(0, len(data) - 1, 2):
    left = data[i]
    right = data[i+1]

    print(f"left: {left}")
    print(f"right: {right}")
    
    if compareElements(left, two) in [-1, 0]:
        lessThanTwo += 1
    if compareElements(right, two) in [-1, 0]:
        lessThanTwo += 1
    if compareElements(left, six) in [-1, 0]:
        lessThanSix += 1
    if compareElements(right, six) in [-1, 0]:
        lessThanSix += 1
    if compareElements(left, right) in [0, -1]:
        rightIndexes.append(index)

    index += 1
    print("")

# PART 1 
print(sum(rightIndexes))
# PART 2
print((lessThanTwo + 1) * (lessThanSix + 2)) # +1 because Elves index start at 1, +2 because of elve indx and inserted [[2]]