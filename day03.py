import sys

priority = lambda c: ord(c) - (96 if c.islower() else 38)

def part1():
    res = 0
    for line in sys.stdin:
        mid = len(line) // 2
        common = set(line[:mid]).intersection(set(line[mid:]))
        res += priority(common.pop())
    return res

def part2():
    group, res = [], 0
    for i, line in enumerate(sys.stdin):
        group.append(set(line.rstrip()))
        if i % 3 == 2:
            common = set.intersection(*group)
            res += priority(common.pop())
            group.clear()
    return res

if __name__ == "__main__":
    # print(part1())
    print(part2())
