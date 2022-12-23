import sys

def build_grid(rocks):
    R = max(max(r for r, _ in line) for line in rocks) + 1
    C = max(max(c for _, c in line) for line in rocks) + 1
    grid = [['.'] * C for _ in range(R)]
    grid[0][500] = '+'

    for line in rocks:
        for i in range(len(line)-1):
            r1, c1 = line[i]
            r2, c2 = line[i+1]
            for row in range(min(r1, r2), max(r1, r2) + 1):
                for col in range(min(c1, c2), max(c1, c2) + 1):
                    grid[row][col] = '#'

    return R, C, grid

def drop_sand(R, C, grid):
    row, col = 0, 500
    if grid[row][col] == 'O':
        return False
    for row in range(R-1):
        if grid[row+1][col] == '.':
            continue
        elif col == 0:
            return False
        elif grid[row+1][col-1] == '.':
            col -= 1
        elif col == C-1:
            return False
        elif grid[row+1][col+1] == '.':
            col += 1
        else:
            grid[row][col] = 'O'
            return True
    return False

def part1(rocks):
    R, C, grid = build_grid(rocks)

    sand = 0
    while drop_sand(R, C, grid):
        sand += 1

    return sand

def part2(rocks):
    R, C, grid = build_grid(rocks)
    R += 2
    C += R + 1
    for row in grid:
        row.extend(['.'] * (C - len(row)))
    grid.append(['.'] * C)
    grid.append(['#'] * C)

    sand = 0
    while drop_sand(R, C, grid):
        sand += 1

    return sand

if __name__ == "__main__":
    rocks = []
    for line in sys.stdin:
        line = map(lambda l: l.split(','), line.rstrip().split(" -> "))
        rocks.append([(int(y), int(x)) for x, y in line])

    print(part1(rocks))
    print(part2(rocks))
