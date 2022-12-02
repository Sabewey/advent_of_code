# Advent of code Year 2022 Day 2 solution
# Author = Erik
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def part_1(input):
    points = 0
    looseWinDraw = [0, 6, 3]
    XYZ = [1, 2, 3]

    for line in input.splitlines():
        one, two = line.split(" ")
        if one == 'A':
            if two == 'Y':
                points += looseWinDraw[1] + XYZ[1]
            elif two == 'Z':
                points += looseWinDraw[0] + XYZ[2]
            else:
                points += looseWinDraw[2] + XYZ[0]
        elif one == 'B':
            if two == 'X':
                points += looseWinDraw[0] + XYZ[0]
            elif two == 'Z':
                points += looseWinDraw[1] + XYZ[2]
            else:
                points += looseWinDraw[2] + XYZ[1]
        elif one == 'C':
            if two == 'X':
                points += looseWinDraw[1] + XYZ[0]
            elif two == 'Y':
                points += looseWinDraw[0] + XYZ[1]
            else:
                points += looseWinDraw[2] + XYZ[2]
    return points

#PART 2
def part_2(input):
    points = 0
    looseDrawWin = [0, 3, 6]
    XYZ = [1, 2, 3]

    for line in input.splitlines():
        one, two = line.split(" ")
        if one == 'A':
            if two == 'Y':
                points += XYZ[0] + looseDrawWin[1]
            elif two == 'Z':
                points += XYZ[1] + looseDrawWin[2]
            else:
                points += XYZ[2] + looseDrawWin[0]
        elif one == 'B':
            if two == 'X':
                points += XYZ[0] + looseDrawWin[0]
            elif two == 'Z':
                points += XYZ[2] + looseDrawWin[2]
            else:
                points += XYZ[1] + looseDrawWin[1]
        elif one == 'C':
            if two == 'X':
                points += XYZ[1] + looseDrawWin[0]
            elif two == 'Y':
                points += XYZ[2] + looseDrawWin[1]
            else:
                points += XYZ[0] + looseDrawWin[2]
    return points

points1 = part_1(input)
points2 = part_2(input)

print("Part One : "+ str(points1))



print("Part Two : "+ str(points2))