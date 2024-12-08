from itertools import product

with open("c:/Users/erikb/programming/lek/advent_of_code/2024/07/input.txt", "r") as f:
    lines = [[int(nbr) for nbr in line.replace(":", "").strip().split(" ")] for line in f.readlines()]


def evaluate(operations, operands):
    operations_copy = operations[:] # Dont need cus new list of ops everytime
    operands_copy = operands[:]
    
    cumulative = operands_copy.pop(0)
    for i in range(len(operands_copy)):
        op = operations_copy.pop(0)
        if op == "*":
            cumulative *= operands_copy.pop(0)
        elif op == "+":
            cumulative += operands_copy.pop(0)
        elif op == "||":
            cumulative = int(str(cumulative) + str(operands_copy.pop(0)))
    return cumulative

count = 0
faulty_lines = []
for line in lines:
    include = False
    ans = line[0]
    operands = line[1:]

    combinations = product(["*", "+"], repeat = len(operands) - 1)
    
    for ops in combinations:
        evaluated = evaluate(list(ops), operands)
        if evaluated == ans:
            include = True
    if include:
        count += ans
    else:
        faulty_lines.append(line)        
print(f"Part one: {count}")
    
for line in faulty_lines:
    include = False
    ans = line[0]
    operands = line[1:]

    combinations = product(["*", "+", "||"], repeat = len(operands) - 1)
    
    for ops in combinations:
        evaluated = evaluate(list(ops), operands)
        if evaluated == ans:
            include = True
    if include:
        count += ans

print(f"Part two: {count}")

# UGH spent about an hour and a half scratching my head because i didnt get the right answer for part 2
# With the code below.. I had overcomplicated the problem, and the solution was much simpler than i thought
# Uggly solution but itll do for tonight.


# for line in lines2:
#     print("checking line", line)
#     include = False
#     ans = line[0]
#     operands = line[1:]
#     if len(operands) == 2:
#         if int(str(operands[0]) + str(operands[1])) == ans:
#             count += ans
#             continue

#     for i in range(1, len(operands)-1):
#         pre = operands[:i]
#         post = operands[i:]
#         combinations_pre = product(["*", "+"], repeat=len(pre)-1)
#         combinations_post = product(["*", "+"], repeat=len(post)-1)
#         for ops_pre in combinations_pre:
#             if include:
#                 break
#             for ops_post in combinations_post:
#                 evaluated_pre = evaluate(list(ops_pre), pre)
#                 evaluated_post = evaluate(list(ops_post), post)
#                 if int(str(evaluated_pre) + str(evaluated_post)) == ans:
#                     include = True
#                     break
#     if include:
#         count += ans

# print(f"Part two: {count}")
