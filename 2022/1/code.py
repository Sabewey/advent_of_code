# Advent of code Year 2022 Day 1 solution
# Author = Erik
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()


maxCalories = [0, 0, 0]
calories = 0

for line in input.splitlines():
    if line == "":
        if calories > maxCalories[0]:
            maxCalories[0] = calories
        elif calories > maxCalories[1]:
            maxCalories[1] = calories
        elif calories > maxCalories[2]:
            maxCalories[2] = calories
        calories = 0
    else:
        calories += int(line)


print("Part One : "+ str(maxCalories[0]))



print("Part Two : "+ str(sum(maxCalories)))