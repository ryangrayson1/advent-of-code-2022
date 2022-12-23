import sys

def part1(instructions):
    cycles = {20, 60, 100, 140, 180, 220}
    X, res = 1, 0
    for cycle, inc in enumerate(instructions):
        if cycle in cycles:
            res += X * cycle
        X += inc

    return res


def part2(instructions):
    X = 1
    for cycle, inc in enumerate(instructions):
        if cycle % 40 == 0:
            print()
        
        if cycle % 40 - 1 <= X <= cycle % 40 + 1:
            print('#', end = "")
        else:
            print('.', end = "")
        X += inc



if __name__ == "__main__":
    instructions = [0]
    for line in sys.stdin:
        line = line.rstrip().split()
        instructions.append(0)
        if line[0] == "addx":
            instructions.append(int(line[1]))

    print(part1(instructions))
    instructions.pop(0)
    part2(instructions)
    print()
    