# Rushed attempt to solve the problem today, but it works...
# Might come back and refactor it later

with open("input.txt", "r") as f:
    commands = [ command.split(" ") for command in f.read().splitlines() ][2:]

#Temporary dictionary to store the size of each directory excluding subdirectories
dirSizes = {
    "/": 0,
    #eg. "/a": 50
    #eg. "/a/b": 50
}
currLocation = "/"

# Handle all commands separately
for command in commands:
    if command[0] == "dir":
        if currLocation == "/":
            dirSizes["/" + command[1]] = 0
        else:
            dirSizes[currLocation + "/" + command[1]] = 0
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                currLocation = currLocation[:currLocation.rfind("/")]
            else:
                if currLocation == "/":
                    currLocation += command[2]
                else:
                    currLocation += "/" + command[2]
        if command[1] == "ls":
            # Maybe do something here?
            pass
    elif command[0].isdigit():
        dirSizes[currLocation] += int(command[0])

# Calculate the total size of each directory INCLUDING subdirectories
dirValue = {}
for k, v in dirSizes.items():
    dirValue[k] = v
    for i in range(1, k.count("/")):
        dirValue[k[:k.rfind("/")]] += v
        #remove the last directory
        k = k[:k.rfind("/")]
        
# Part 1
sum = 0
for k, v in dirValue.items():
    if v < 100000:
        sum += v

# Part 2
min = 100000000
for k, v in dirValue.items():
    if (v < min) and (v > 8381165):
        min = v
    
print("part 1: " + str(sum))
print("part 2: " + str(min))