# Advent of code Year 2022 Day 5 solution
# Author = Erik
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    stack, data = input_file.read().split("\n\n")
    data = [ [ int(s) for s in line.split() if s.isdigit() ] for line in data.split("\n") ] # 'move 1 from 8 to 9'

stacks = {
    1: "NTBSQHGR",
    2: "JZPDFSH",
    3: "VHZ",
    4: "HGFJZM",
    5: "RSMLDCZT",
    6: "JZHVWTM",
    7: "ZLPFT",
    8: "SWVQ",
    9: "CNDTMLHW",
}
#'move 1 from 8 to 9'
for instruction in data:
    n, From, To, = instruction[0], instruction[1], instruction[2]
    stacks[To] = stacks[From][:n][::-1] + stacks[To]
    stacks[From] = stacks[From][n:]

res = ""
for i in range(1,10):
    res += stacks[i][0]


print("Part One : "+ str(res))



print("Part Two : "+ str(None))