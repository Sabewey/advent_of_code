with open("input.txt", "r") as f:
    data = [line for line in f.readlines()]

#part2
words = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

sum = 0
for sentence in data:
    first = None
    last = None
    s = ""
    for c in sentence:
        digit = None
        if c.isdigit():
            digit = c
        else:
            s += c
            for k,v in words.items():
                if s.endswith(k):
                    digit = str(v)
        if digit != None:
            if first == None:
                first = digit
            last = digit
    print(first + last)
    sum += int(first + last)

print(sum)    
