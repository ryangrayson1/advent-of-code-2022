import sys
from collections import deque

def get_neis(R, C, heightmap, seen, row, col):
    neis = []
    for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= row+r < R and 0 <= col+c < C and not seen[row+r][col+c] \
            and heightmap[row][col] + 1 >= heightmap[row+r][col+c]:
            neis.append((row+r, col+c))
            seen[row+r][col+c] = True
    return neis

def part1(S, E, heightmap):
    R, C = len(heightmap), len(heightmap[0])
    seen = [[False] * C for _ in range(R)]
    seen[S[0]][S[1]] = True
    q = deque([(S[0], S[1], 0)])

    while q:
        row, col, dist = q.popleft()
        for nei_row, nei_col in get_neis(R, C, heightmap, seen, row, col):
            if (nei_row, nei_col) == E:
                return dist + 1
            q.append((nei_row, nei_col, dist + 1))
    
    return -1


def get_neis2(R, C, heightmap, seen, row, col):
    neis = []
    for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= row+r < R and 0 <= col+c < C and not seen[row+r][col+c] \
            and heightmap[row][col] <= heightmap[row+r][col+c] + 1:
            neis.append((row+r, col+c))
            seen[row+r][col+c] = True
    return neis


def part2(E, heightmap):
    R, C = len(heightmap), len(heightmap[0])
    seen = [[False] * C for _ in range(R)]
    seen[E[0]][E[1]] = True
    q = deque([(E[0], E[1], 0)])

    while q:
        row, col, dist = q.popleft()
        for nei_row, nei_col in get_neis2(R, C, heightmap, seen, row, col):
            if heightmap[nei_row][nei_col] == 0:
                return dist + 1
            q.append((nei_row, nei_col, dist + 1))
    
    return -1


if __name__ == "__main__":
    S = E = None
    heightmap = []
    for r, line in enumerate(sys.stdin):
        heightmap.append(list(map(lambda h: ord(h) - 97, line.rstrip())))
        if 'S' in line:
            S = (r, line.index('S'))
            heightmap[r][S[1]] = 0
        if 'E' in line:
            E = (r, line.index('E'))
            heightmap[r][E[1]] = 25
        
    print(part1(S, E, heightmap))
    print(part2(E, heightmap))
