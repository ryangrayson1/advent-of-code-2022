import copy

global rocks, space
rocks = [
    [
        ['.','.','@','@','@','@','.']
    ],
    [
        ['.','.','.','@','.','.','.'],
        ['.','.','@','@','@','.','.'],
        ['.','.','.','@','.','.','.']
    ],
    [
        ['.','.','.','.','@','.','.'],
        ['.','.','.','.','@','.','.'],
        ['.','.','@','@','@','.','.']
    ],
    [
        ['.','.','@','.','.','.','.'],
        ['.','.','@','.','.','.','.'],
        ['.','.','@','.','.','.','.'],
        ['.','.','@','.','.','.','.']
    ],
    [
        ['.','.','@','@','.','.','.'],
        ['.','.','@','@','.','.','.']
    ]
]
space = [
    ['.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.']
]

def move_rock_hor(cave, rock, left):
    if left:
        for row, col in rock:
            if col == 0 or (col > 0 and cave[row][col-1] == '#'):
                return False
        for c in rock:
            c[1] -= 1
    else:
        for row, col in rock:
            if col == 6 or (col < 6 and cave[row][col+1] == '#'):
                return False
        for c in rock:
            c[1] += 1
    return True

def move_rock(cave, rock, jets, j):
    move_rock_hor(cave, rock, jets[j[0]] == '<')
    j[0] += 1
    j[0] %= len(jets)
    for row, col in rock:
        if row == 0 or cave[row-1][col] == '#':
            return False
    for c in rock:
        c[0] -= 1
    return True

def drop_rock(cave, r, jets, j):
    global rocks, space
    cave.extend(copy.deepcopy(space))
    cave.extend(copy.deepcopy(rocks[r][::-1]))

    rock = []
    for row in range(len(cave) - 4, len(cave)):
        for col in range(7):
            if cave[row][col] == '@':
                rock.append([row, col])
                cave[row][col] = '.'

    while move_rock(cave, rock, jets, j):
        pass

    for row, col in rock:
        cave[row][col] = '#'
    
    while '#' not in cave[-1]:
        cave.pop()

def part1(jets):
    cave, j = [], [0]
    for i in range(2022):
        drop_rock(cave, i % 5, jets, j)

    return len(cave)

def hsh(i, j, cave):
    s = [i, j[0]]
    for col in range(7):
        for row in range(1, len(cave) + 1):
            if cave[-row][col] == '#':
                s.append(row)
                break
        else:
            s.append(0)
    return ','.join([str(c) for c in s])


def part2(jets):
    T = 1000000000000
    seen = {}
    cave, j = [], [0]
    for i in range(T):
        drop_rock(cave, i % 5, jets, j)
        state = hsh(i % 5, j, cave)
        if state in seen:
            i1, h1 = seen[state]
            i2, h2 = i, len(cave)
            print("cycle found from i =", i1, "to i  =", i2)
            res = h1
            cycles = (T - i1) // (i2 - i1)
            res += cycles * (h2 - h1)
            extra = (T - i1) % (i2 - i1)
            for e in range(extra):
                drop_rock(cave, (i + e + 1) % 5, jets, j)
            res += len(cave) - h2 - 1
            return res
        else:
            seen[state] = (i, len(cave))

    return len(cave)


if __name__ == "__main__":
    jets = list(input())
    print(part1(jets))
    print(part2(jets))
