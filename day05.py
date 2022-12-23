import sys, copy

def part1(stacks, instructions):
    for q, f, t in instructions:
        for _ in range(q):
            stacks[t].append(stacks[f].pop())
    tops = [s[-1] for s in stacks]
    return ''.join(tops)

def part2(stacks, instructions):
    for q, f, t in instructions:
        pile = [stacks[f].pop() for _ in range(q)]
        stacks[t].extend(reversed(pile))
    tops = [s[-1] for s in stacks]
    return ''.join(tops)

def get_stacks():
    stacks = []
    for line in sys.stdin:
        if line[1] == '1':
            break
        for i in range(1, len(line), 4):
            while len(stacks) <= i // 4:
                stacks.append([])
            if line[i] != ' ':
                stacks[i // 4].append(line[i])
    for s in stacks:
        s.reverse()
    return stacks

def get_instructions():
    input()
    instructions = []
    for line in sys.stdin:
        q, f, t = (int(x) for x in line.rstrip().split() if x.isnumeric())
        instructions.append((q, f - 1, t - 1))
    return instructions

if __name__ == "__main__":
    stacks = get_stacks()
    instructions = get_instructions()
    print(part1(copy.deepcopy(stacks), instructions))
    print(part2(copy.deepcopy(stacks), instructions))