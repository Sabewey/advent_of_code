with open("c:/Users/erikb/programming/lek/advent_of_code/2024/03/input.txt", "r") as f:
    data = [line for line in f.readlines()]

sum = 0
enabled = True
for line in data:
    for i in range(len(line)):
        if line[i:i+7] == "don't()":
            enabled = False
        elif line[i:i+4] == "do()":
            enabled = True
        if enabled:
            if line[i:i+4] == "mul(":
                d = i+4
                while line[d].isdigit():
                    d += 1
                if line[d] == ",":
                    nbr1 = int(line[i+4:d])
                    d += 1
                    c = d
                    while line[c].isdigit():
                        c += 1
                    if line[c] == ")":
                        nbr2 = int(line[d:c])
                        print(nbr1, nbr2)
                        print(f"mul: {nbr1*nbr2}")
                        sum += nbr1*nbr2
print(sum)