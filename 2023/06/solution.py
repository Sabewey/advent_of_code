import math

with open("C:/Users/erikb/programming/lek/advent_of_code/2023/06/input.txt", "r") as f:
    time = f.readline().strip().split(",")
    distance = f.readline().strip().split(",")

#Super simple solutions today, messy code

#part1
res = []
for i in range(len(time)):
    distances = []
    t = int(time[i])
    d = int(distance[i])
    #enumerate all possible options
    for j in range(1, t):
        #calculate distance travelled with this speed build up
        dist = j * (t - j)
        if dist > d:
            distances.append(dist)
    res.append(len(distances))
print(math.prod(res))

#part2
time = int(''.join(time))
distance = int(''.join(distance))
ways = []
for i in range(1, time):
    dist = i * (time - i)
    if dist > distance:
        ways.append(dist)
print(len(ways))