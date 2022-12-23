import sys

def part1(assignments):
    res = 0
    for s1, e1, s2, e2 in assignments:
        if s1 <= s2 <= e2 <= e1 or s2 <= s1 <= e1 <= e2:
            res += 1
    return res

def part2(assignments):
    res = 0
    for s1, e1, s2, e2 in assignments:
        if s1 <= s2 <= e1 or s2 <= s1 <= e2:
            res += 1
    return res

if __name__ == "__main__":
    assignments = []
    for line in sys.stdin:
        r1, r2 = line.rstrip().split(',')
        s1, e1 = map(int, r1.split('-'))
        s2, e2 = map(int, r2.split('-'))
        assignments.append((s1, e1, s2, e2))
    print(part1(assignments))
    print(part2(assignments))
