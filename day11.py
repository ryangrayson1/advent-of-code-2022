import sys, copy

class Monkey:
    def __init__(self, items = [], op = '', op_val = 0, test_div = 0, tr = 0, fa = 0):
        self.items = items
        self.op = op
        self.op_val = op_val
        self.test_div = test_div
        self.tr = tr
        self.fa = fa
        self.inspect = 0

def part12(monkeys, rounds, div3):

    lcd = 1
    for m in monkeys:
        lcd *= m.test_div

    for _ in range(rounds):
        for m in monkeys:
            for worry in m.items:
                m.inspect += 1
                if m.op_val == 'o':
                    if m.op == '+':
                        worry += worry
                    else:
                        worry *= worry
                elif m.op == '+':
                    worry += m.op_val
                else:
                    worry *= m.op_val

                if div3:
                    worry //= 3
                else:
                    worry %= lcd

                if worry % m.test_div == 0:
                    monkeys[m.tr].items.append(worry)
                else:
                    monkeys[m.fa].items.append(worry)
            m.items.clear()
    
    # for i, m in enumerate(monkeys):
    #     print(i, m.inspect)

    monkeys.sort(key = lambda k: k.inspect)
    return monkeys[-2].inspect * monkeys[-1].inspect


if __name__ == "__main__":
    monkeys = []
    for i, line in enumerate(sys.stdin):
        line = line.rstrip().replace(',', '').split()
        if i % 7 == 0:
            monkeys.append(Monkey())
        elif i % 7 == 1:
            monkeys[-1].items = list(map(int, line[2:]))
        elif i % 7 == 2:
            monkeys[-1].op = line[-2]
            monkeys[-1].op_val = int(line[-1]) if line[-1].isnumeric() else 'o'
        elif i % 7 == 3:
            monkeys[-1].test_div = int(line[-1])
        elif i % 7 == 4:
            monkeys[-1].tr = int(line[-1])
        elif i % 7 == 5:
            monkeys[-1].fa = int(line[-1])
    
    # part 1f
    print(part12(copy.deepcopy(monkeys), 20, True))
    # part 2
    print(part12(copy.deepcopy(monkeys), 10000, False))
