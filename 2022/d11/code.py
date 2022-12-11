class Monkey():
    def __init__(self, xs, op, testLambda, ret):
        self.items = xs
        self.op = op
        self.testlambda = testLambda
        self.ret = ret
        self.inspect = 0

    def operation(self, old):
        self.inspect += 1
        return self.op(old)
    
    def test(self, old):
        return self.ret[0] if self.testlambda(old) else self.ret[1]

    def add(self, b):
        self.items.append(b)
    
    def deleteHead(self):
        self.items.pop(0)

#Annoying input today, so decided to manually input it
one = Monkey([74, 73, 57, 77, 74], lambda x: x * 11, lambda x: x % 19 == 0, [6, 7])
two = Monkey([99, 77, 79], lambda x: x + 8, lambda x: x % 2 == 0, [6, 0])
three = Monkey([64, 67, 50, 96, 89, 82, 82], lambda x: x + 1, lambda x: x % 3 == 0, [5, 3])
four = Monkey([88], lambda x: x * 7, lambda x: x % 17 == 0, [5, 4])
five = Monkey([80, 66, 98, 83, 70, 63, 57, 66], lambda x: x + 4, lambda x: x % 13 == 0, [0, 1])
six = Monkey([81, 93, 90, 61, 62, 64], lambda x: x + 7, lambda x: x % 7 == 0, [1, 4])
seven = Monkey([69, 97, 88, 93], lambda x: x * x, lambda x: x % 5 == 0,[7, 2])
eight = Monkey([59, 80], lambda x: x + 6, lambda x: x % 11 == 0, [2, 3])
monkeys = [one, two, three, four, five, six, seven, eight]

cap = 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2
for round in range(10000):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            monkey.items[0] = monkey.operation(monkey.items[0]) % cap #// 3 Part 1
            sendTo = monkey.test(monkey.items[0])
            monkeys[sendTo].add(monkey.items[0])
            monkey.deleteHead()

#Part one is 20 rounds and with // 3, part two is 10000 rounds and with % cap
inspects = sorted([monkey.inspect for monkey in monkeys])[::-1]
print(inspects[0] * inspects[1])