# Advent of code Year 2022 Day 4 solution
# Author = Erik
# Date = December 2022

part1_overlap = 0
part2_intersect = 0

def input(filename):
    with open(filename, 'r') as input_file:
        data = [ [ a, b, c, d ] for ((a, b), (c, d)) in [(tuple(a.split('-')), tuple(b.split('-'))) for (a, b) in [ line.strip().split(",") for line in input_file.readlines() ] ] ]
    return data

data = input("test.txt")
print(data)

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    for line in input.splitlines():
        res = [tuple.split('-') for tuple in line.split(',')]
        res = [int(item) for sublist in res for item in sublist]

        # PART 1: If the first range is in the second OR the second range is in the first, then the ranges overlap
        if (res[0] <= res[2] and res[1] >= res[3]) or (res[0] >= res[2] and res[1] <= res[3]):
            part1_overlap += 1
        # PART 2: If any of the numbers in first range is in the second range, then the ranges intersect
        if len(set([i for i in range(res[0], res[1]+1)]).intersection([i for i in range(res[2], res[3]+1)])) > 0:
            part2_intersect += 1

print("Part One : "+ str(part1_overlap))



print("Part Two : "+ str(part2_intersect))