with open("c:/Users/erikb/programming/lek/advent_of_code/2024/09/input.txt", "r") as f:
    line = f.readline().strip()

def decode(line):
    i = 0
    decoded = []
    block = 0
    while i < len(line):
        nbr = int(line[i])
        if i % 2 == 0:
            decoded.extend([block] * nbr)
            block += 1
        else:
            decoded.extend(["."] * nbr)
        i += 1
    return decoded


def compress(line):
    left = 0
    right = len(line) - 1

    while left < right:
        while left < len(line) and line[left] != ".":
            left += 1
        while right >= 0 and line[right] == ".":
            right -= 1
        if left < right:
            line[left] = line[right]
            line[right] = "."
    return line

def checksum(line):
    res = 0
    for idx, block in enumerate(line):
        if block == ".":
            continue
        else:
            res += idx * int(block)
    return res

decoded = decode(line)
print(decoded)
moved = compress(decoded)
print(moved)
check = checksum(moved)
print(check)