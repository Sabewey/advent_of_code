with open("C:/Users/erikb/programming/lek/advent_of_code/2023/13/test.txt", "r") as f:
    data = f.read().split("\n\n")
    puzzles = [line.split("\n") for line in data]

def count_diff(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

ans = 0
part = 2
for puzzle in puzzles:
    # Check vertical sym-lines
    for c in range(1, len(puzzle[0])):
        for r in range(len(puzzle)):
            nbrChars = min(c, len(puzzle[0])-c)
            left = puzzle[r][:c][-nbrChars:]
            right = puzzle[r][c:][:nbrChars][::-1]
            diff = count_diff(left, right)
            if diff == (1 if part == 2 else 0):
                ans += 1
        
    ans2 = 0
    # Check horizontal sym-lines
    for r in range(1, len(puzzle)):
        nbrRows = min(r, len(puzzle)-r)
        up = puzzle[:r][-nbrRows:]
        down = puzzle[r:][:nbrRows][::-1]
        diff = count_diff(up, down)
        print(diff)
        if diff == (1 if part == 2 else 0):
            ans2 += 1
        # nbrRows = min(r, len(puzzle)-r)
        # up = puzzle[:r][-nbrRows:]
        # down = puzzle[r:][:nbrRows][::-1]
        # diff = count_diff(up, down)
        # if diff == (1 if part == 2 else 0):
        #     ans += r*100

print(ans)
print(ans2)
