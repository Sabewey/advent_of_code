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

""" stacks = {
    1: "NZ",
    2: "DCM",
    3: "P",
} """

#'move 1 from 8 to 9'
def move(data, part):
    stacks_copy = stacks.copy()
    for instruction in data:
        n, From, To, = instruction[0], instruction[1], instruction[2]
        if part == 1:
            stacks_copy[To] = stacks_copy[From][:n][::-1] + stacks_copy[To]
            stacks_copy[From] = stacks_copy[From][n:]
        else:
            stacks_copy[To] = stacks_copy[From][:n] + stacks_copy[To]
            stacks_copy[From] = stacks_copy[From][n:]
    
    # Gather top of each stack
    res = ""
    for i in range(1,len(stacks_copy)+1):
        if len(stacks_copy[i]) > 0:
            res += stacks_copy[i][0]
    return res



print("Part One : "+ str(move(data, 1)))



print("Part Two : "+ str(move(data, 2)))