import time

def update_vis(R, C, grid, visible, start, direction):
    row, col = start
    r, c = direction
    tallest = -1
    while 0 <= row < R and 0 <= col < C:
        if grid[row][col] > tallest:
            visible[row][col] = True
            tallest = grid[row][col]
        row += r
        col += c

def part1(grid):
    R, C = len(grid), len(grid[0])
    visible = [[False] * C for _ in range(R)]
    for row in range(R):
        update_vis(R, C, grid, visible, (row, 0), (0, 1))
        update_vis(R, C, grid, visible, (row, C-1), (0, -1))
    for col in range(C):
        update_vis(R, C, grid, visible, (0, col), (1, 0))
        update_vis(R, C, grid, visible, (R-1, col), (-1, 0))

    return sum(sum(row) for row in visible)


def update_score(R, C, grid, score, start, direction):
    row, col = start
    r, c = direction
    nearest = [(row, col) for _ in range(10)]
    while 0 <= row < R and 0 <= col < C:
        vis = float('inf')
        for lr, lc in nearest[grid[row][col]:]:
            dist = abs(row - lr) + abs(col - lc)
            vis = min(vis, dist)
        score[row][col] *= vis
        nearest[grid[row][col]] = (row, col)
        row += r
        col += c

def part2(grid):
    R, C = len(grid), len(grid[0])
    score = [[1] * C for _ in range(R)]
    for row in range(R):
        update_score(R, C, grid, score, (row, 0), (0, 1))
        update_score(R, C, grid, score, (row, C-1), (0, -1))
    for col in range(C):
        update_score(R, C, grid, score, (0, col), (1, 0))
        update_score(R, C, grid, score, (R-1, col), (-1, 0))
    
    return max(max(c for c in row) for row in score)


def parse(file):
    grid = []
    for row in open(file).readlines():
        grid.append(list(map(int, row.rstrip())))
    return grid

if __name__ == "__main__":
    grid = parse("day8.txt")
    print(part1(grid))
    
    p2start = time.time()
    print(part2(grid))
    p2end = time.time()
    print("part 2 runtime:", p2end - p2start)
