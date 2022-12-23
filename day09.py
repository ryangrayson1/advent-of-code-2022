import sys

def p(head, tail):
    hr, hc = head
    tr, tc = tail
    ro = 2 - hr
    co = 2 - hc
    grid = [['.'] * 5 for _ in range(5)]
    grid[tr+ro][tc+co] = 'T'
    grid[2][2] = 'H'
    for r in grid:
        print(*r)
    print()

def move(head, tail, r, c):
    head[0] += r
    head[1] += c
    if abs(head[0] - tail[0]) > 1:
        tail[0] += r
        tail[1] = head[1]
    elif abs(head[1] - tail[1]) > 1:
        tail[0] = head[0]
        tail[1] += c

def part1(moves):
    tail_pos = set()
    head = [0, 0]
    tail = [0, 0]

    for r, c, n in moves:
        for _ in range(n):
            move(head, tail, r, c)
            tail_pos.add(tuple(tail))
    
    return len(tail_pos)

def p2(rope):
    ro = -min(r for r, _ in rope)
    co = -min(c for _, c in rope)
    grid = [['_'] * 10 for _ in range(10)]
    i = 9
    for r, c in reversed(rope):
        grid[r+ro][c+co] = i if i > 0 else 'H'
        i -= 1
    for r in grid:
        print(*r)
    print()


def update(head, tail):
    diff0 = abs(head[0] - tail[0])
    diff1 = abs(head[1] - tail[1])

    if diff0 > 1:
        tail[0] = (head[0] + tail[0]) // 2
        if diff1 == 1:
            tail[1] = head[1]
    
    if diff1 > 1:
        tail[1] = (head[1] + tail[1]) // 2
        if diff0 == 1:
            tail[0] = head[0]


def part2(moves):
    tail_pos = set()
    rope = [[0, 0] for _ in range(10)]
    for r, c, n in moves:
        for _ in range(n):
            rope[0][0] += r
            rope[0][1] += c
            for i in range(9):
                update(rope[i], rope[i+1])

            tail_pos.add(tuple(rope[-1]))
            # p2(rope)
    
    return len(tail_pos)

if __name__ == "__main__":
    moves = []
    for line in sys.stdin:
        line = line.rstrip().split()
        m = []
        if line[0] == 'L':
            m.append(0)
            m.append(-1)
        elif line[0] == 'R':
            m.append(0)
            m.append(1)
        elif line[0] == 'U':
            m.append(-1)
            m.append(0)
        elif line[0] == 'D':
            m.append(1)
            m.append(0)
        m.append(int(line[1]))
        moves.append(m)
    
    print(part1(moves))
    print(part2(moves))