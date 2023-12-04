from collections import defaultdict

with open('C:/Users/erikb/programming/lek/advent_of_code/2023/04/input.txt') as f:
    data = [line.strip().split(':') for line in f.readlines()]

points = []
copies = defaultdict(int)
total = []
for idx, game in enumerate(data):
    winners, hand = game[1].strip().split('|')
    winners = set(winners.strip().split(' '))
    hand = set(hand.strip().split(' '))

    if '' in winners:
        winners.remove('')

    nbrWinnersInHand = 0  
    for winner in winners:
        if winner in hand:
            nbrWinnersInHand += 1
    
    for nbr in range(1, nbrWinnersInHand+1):
        if copies[idx+1] > 0:
            copies[idx+1 + nbr] += 1 * (1+copies[idx+1])
        else:
            copies[idx+1 + nbr] += 1


    if nbrWinnersInHand == 1:
        points.append(1)
    elif nbrWinnersInHand > 1:
        points.append(2**(nbrWinnersInHand-1))

    total.append(1+copies[idx+1])

#part1
print(sum(points))

#part2
print(sum(total))

