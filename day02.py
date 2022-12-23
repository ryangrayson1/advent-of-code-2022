import sys

def part1():
    score = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
    res = 0
    for line in sys.stdin:
        res += score[line.rstrip()]
    return res

def part2():
    score = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
    res = 0
    for line in sys.stdin:
        res += score[line.rstrip()]
    return res

if __name__ == "__main__":
    # print("Part 1:", part1())
    print("Part 2:", part2())