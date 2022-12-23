import sys
from collections import deque

def part1(cubes):
    surface = 0
    for x1, y1, z1 in cubes:
        open_faces = 6
        for x2, y2, z2 in cubes:
            if abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1:
                open_faces -= 1
        surface += open_faces
    return surface

def dfs(cubeset, seen, start):
    NEIS = [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]
    stack, contained = [start], [start]
    edge = False
    while stack:
        x, y, z = stack.pop()
        for a, b, c in NEIS:
            if not (0 < x+a < 21 and 0 < y+b < 21 and 0 < z+c < 21):
                edge = True
                continue
            nxt = (x+a, y+b, z+c)
            if nxt not in seen and nxt not in cubeset:
                seen.add(nxt)
                contained.append(nxt)
                stack.append(nxt)

    return [] if edge else contained
                
def part2(cubes):
    res = part1(cubes)
    cubeset = set(cubes)
    seen = set()
    for x in range(21):
        for y in range(21):
            for z in range(21):
                cube = (x, y, z)
                if cube not in seen and cube not in cubeset:
                    seen.add(cube)
                    contained = dfs(cubeset, seen, cube)
                    res -= part1(contained)
    return res
        
if __name__ == "__main__":
    cubes = []
    for line in sys.stdin:
        cubes.append(tuple(map(int, line.split(','))))

    print(part1(cubes))
    print(part2(cubes))
