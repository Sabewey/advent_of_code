with open("2.txt", "r") as f:
    lines = f.readlines()
    #Remove every third line
    data = [line.strip() for line, idx in zip(lines, range(len(lines))) if idx % 3 != 2]

#Return -1 if a < b, 0 if a == b, 1 if a > b
def compare(a, b):
    if isinstance(a, list):
        if len(a) != 0:
            if isinstance(b, list):
                for i in range(len(a)):
                    try:
                        if compare(a[i], b[i]) > 0: # compare(9, [8, 7, 6])
                            return 1
                    except IndexError:
                        return 1
            else:
                compare(a, [b]) # same as compare(a[0], b)?
        else:
            if isinstance(b, list):
                if len(b) != 0:
                    return -1
                else:
                    return 0
            else:
                return -1
    elif isinstance(b, list):
        return compare([a], b) # same as compare(a, b[0])?
    else:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    return -1



rightIndexes = []
index = 1
for i in range(0, len(data) - 1, 2):
    left = eval(data[i])
    right = eval(data[i+1])
    print(f"left: {left}")
    print(f"right: {right}")
    print("")
    if compare(left, right) == -1:
        rightIndexes.append(index)
    index += 1

print(rightIndexes)
print(sum(rightIndexes))
    