import sys

R, D, L, U = 0, 1, 2, 3

class S:
    def init_mms(self):
        self.row_min = [-1] * self.R
        self.row_max = [-1] * self.R
        for row in range(self.R):
            for col in range(self.C):
                if self.grid[row][col] != ' ':
                    if self.row_min[row] == -1:
                        self.row_min[row] = col
                    self.row_max[row] = col
        
        self.col_min = [-1] * self.C
        self.col_max = [-1] * self.C
        for col in range(self.C):
            for row in range(self.R):
                if self.grid[row][col] != ' ':
                    if self.col_min[col] == -1:
                        self.col_min[col] = row
                    self.col_max[col] = row

    def __init__(self, grid, row, col, dir):
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0])
        self.row = row
        self.col = col
        self.dir = dir
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.init_mms()
    
    def p(self):
        d = ['>', 'v', '<', '^']
        self.grid[self.row][self.col] = d[self.dir]
        for row in self.grid:
            print(*row)
        print()
        self.grid[self.row][self.col] = '.'

def move(s, m):
    r, c = s.moves[s.dir]
    for _ in range(m):
        new_row = s.row + r
        new_col = s.col + c
        if r != 0 and new_row < s.col_min[new_col]:
            new_row = s.col_max[new_col]
        elif r != 0 and s.col_max[new_col] < new_row:
            new_row = s.col_min[new_col]
        elif c != 0 and new_col < s.row_min[new_row]:
            new_col = s.row_max[new_row]
        elif c != 0 and s.row_max[new_row] < new_col:
            new_col = s.row_min[new_row]
        
        if s.grid[new_row][new_col] == '#':
            return

        s.row = new_row
        s.col = new_col

def part1(grid, instrs):
    s = S(grid, 0, grid[0].index('.'), 0)
    for i, instr in enumerate(instrs):
        if i % 2:
            s.dir = (s.dir + instr) % 4
        else:
            move(s, instr)
    
    return 1000 * (s.row + 1) + 4 * (s.col + 1) + s.dir


def get_cube_transitions(s):
    transitions = {}
    f2r = s.row_max[0]
    f3r = s.row_max[50]
    f5r = s.row_max[100]
    f6r = s.row_max[150]
    f6d = s.col_max[0]
    f5d = s.col_max[50]
    f2d = s.col_max[100]
    f1l = s.row_min[0]
    f3l = s.row_min[50]
    f4l = s.row_min[100]
    f6l = s.row_min[150]
    f4u = s.col_min[0]
    f1u = s.col_min[50]
    f2u = s.col_min[100]

    for i in range(50):

        transitions[(i, f1l, L)] = (149 - i, f4l, R) # 1L -> 4L
        transitions[(i + 100, f4l, L)] = (49 - i, f1l, R) # 4L -> 1L
    
        transitions[(i + 50, f3l, L)] = (f4u, i, D) # 3L -> 4U
        transitions[(f4u, i, U)] = (i + 50, f3l, R) # 4U -> 3L

        transitions[(i + 150, f6l, L)] = (f1u, i + 50, D) # 6L -> 1U
        transitions[(f1u, i + 50, U)] = (i + 150, f6l, R) # 1U -> 6L

        transitions[(f6d, i, D)] = (f2u, i + 100, D) # 6D -> 2U
        transitions[(f2u, i + 100, U)] = (f6d, i, U) # 2U -> 6D

        transitions[(i + 150, f6r, R)] = (f5d, i + 50, U) # 6R -> 5D
        transitions[(f5d, i + 50, D)] = (i + 150, f6r, L) # 5D -> 6R

        transitions[(i + 100, f5r, R)] = (49 - i, f2r, L) # 5R -> 2R
        transitions[(i, f2r, R)] = (149 - i, f5r, L) # 2R -> 5R

        transitions[(i + 50, f3r, R)] = (f2d, i + 100, U) # 3R -> 2D
        transitions[(f2d, i + 100, D)] = (i + 50, f3r, L) # 2D -> 3R
    
    return transitions


def move2(s, m, transitions):
    for _ in range(m):
        r, c = s.moves[s.dir]
        new_row = new_col = new_dir = None
        if (s.row, s.col, s.dir) in transitions:
            new_row, new_col, new_dir = transitions[(s.row, s.col, s.dir)]
        else:
            new_row = s.row + r
            new_col = s.col + c
            new_dir = s.dir
        
        if s.grid[new_row][new_col] == '#':
            return
        
        s.row = new_row
        s.col = new_col
        s.dir = new_dir

def part2(grid, instrs):
    s = S(grid, 0, grid[0].index('.'), 0)
    transitions = get_cube_transitions(s)
    for i, instr in enumerate(instrs):
        if i % 2:
            s.dir = (s.dir + instr) % 4
        else:
            move2(s, instr, transitions)
    
    return 1000 * (s.row + 1) + 4 * (s.col + 1) + s.dir


if __name__ == "__main__":
    grid, instrs = [], []
    for line in sys.stdin:
        line = line.rstrip()
        if len(line) == 0:
            continue
        if line[0].isnumeric():
            num = ""
            for c in line:
                if c.isnumeric():
                    num += c
                else:
                    instrs.append(int(num))
                    instrs.append(1 if c == 'R' else -1)
                    num = ""
            instrs.append(int(num))
            break
        grid.append(list(line))
    
    C = max(len(row) for row in grid)
    for row in grid:
        row.extend([' '] * (C - len(row)))

    print(part1(grid, instrs))
    print(part2(grid, instrs))
