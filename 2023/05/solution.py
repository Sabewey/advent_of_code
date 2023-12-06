with open("C:/Users/erikb/programming/lek/advent_of_code/2023/05/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    initial_seeds = [e.strip() for e in data[0].split(':')][1].split(" ")
    initial_seeds = [int(e) for e in initial_seeds]
    intervals = [[seed, seed + initial_seeds[idx+1]] for idx, seed in enumerate(initial_seeds) if idx % 2 == 0]
    print(intervals)

MAP = {
    "seed-to-soil": {},
    "soil-to-fertilizer": {},
    "fertilizer-to-water": {},
    "water-to-light": {},
    "light-to-temperature": {},
    "temperature-to-humidity": {},
    "humidity-to-location": {}
}

#part2 reverse map
MAP2 = {
    "seed-to-soil": {},
    "soil-to-fertilizer": {},
    "fertilizer-to-water": {},
    "water-to-light": {},
    "light-to-temperature": {},
    "temperature-to-humidity": {},
    "humidity-to-location": {}
}

# Populate MAP
m = ""
first = True
for line in data[2:]:
    if line == "":
        first = True
        continue
    if first:
        m = line.split(" ")[0]
        first = False
        continue
    else:
        dst, src, len = line.split(" ")
        MAP[m][src] = (int(src), int(src) + int(len), int(dst)-int(src))
        #part2 backtracking
        MAP2[m][dst] = (int(dst), int(dst) + int(len), int(src)-int(dst))

MAP2 = dict(reversed(list(MAP2.items())))
print(MAP2)
#part2
# loop over all possible locations and find the initial seed if it exists in range
location = 0
found = False  # Flag to indicate if the seed is found

while not found:
    val = location
    for m in MAP2:
        for i in MAP2[m].values():
            if i[0] <= val < i[1]:
                val += i[2]
                break

    for inter in intervals:
        if inter[0] <= val < inter[1]:
            print(location)
            found = True
            break

    if location % 100000 == 0:
        print(location)
    
    location += 1

    if found:
        break  # Break the outer loop if the seed is found

final_location = []
# Go through the initial seeds and find the final location
#for seed in initial_seeds: #part1
for seed_range in intervals: #part2
    for seed in seed_range: #part2
        src = seed
        for m in MAP:
            for interval in MAP[m].values():
                if src in range(interval[0], interval[1]):
                    src = src + interval[2]
                    break
                else:
                    src = src

        final_location.append(src)

#part1
print(min(final_location))