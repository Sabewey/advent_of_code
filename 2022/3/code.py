# Advent of code Year 2022 Day 3 solution
# Author = Erik
# Date = December 2022
import string

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def createMapping():
    mapping = {}
    for i, c in enumerate(string.ascii_lowercase, 1):
        mapping.update({c: i})
    for i, c in enumerate(string.ascii_uppercase, 27):
        mapping.update({c: i})
    return mapping
    

prioValues = createMapping()

def part_1(input):
    first_half = []
    second_half = set()
    prioSum = 0

    for line in input.splitlines():
        lineList = []
        for c in line:
            lineList.append(c)
        first_half = lineList[:len(lineList)//2]
        second_half = set(lineList[len(lineList)//2:])
        for c in first_half:
            if c in second_half:
                prioSum += prioValues[c]
                break
        
    return prioSum

def part_2(input):
    prioSum = 0
    lines = [set(), set(), set()]
    for index, line in enumerate(input.splitlines(), 0):
        for c in line:
            lines[index%3].add(c)
        if index % 3  == 2:
            for c in lines[0]:
                if c in lines[1] and c in lines[2]:
                    prioSum += prioValues[c]
                    break
            lines = [set(), set(), set()]
    return prioSum
        
        

#15730
print("Part One : "+ str(part_1(input)))



print("Part Two : "+ str(part_2(input)))