import sys, copy
from collections import deque

ORE, CLY, OBS, GEO = 0, 1, 2, 3

class State:
    def __init__(self, robots, resources):
        self.minute = 1
        self.robots = robots
        self.resources = resources
    
    def hash(self):
        return str(self.minute) + '|' + ','.join(str(r) for r in self.robots) + '|' + ','.join(str(r) for r in self.resources)
    
    def p(self):
        print(self.minute)
        print(*self.robots)
        print(*self.resources)
        print()

def get_next_states(blueprint, seen, max_geo, max_rob, s, m):
    if s.minute > m or s.resources[GEO] + 2 <= max_geo or s.robots[GEO] + 2 <= max_rob:
        return []

    s2 = copy.deepcopy(s)
    s2.minute += 1
    for i, r in enumerate(s.robots):
        s2.resources[i] += r

    nxt = [s2]
    if s.resources[ORE] >= blueprint[4] and s.resources[OBS] >= blueprint[5]:
        s3 = copy.deepcopy(s2)
        s3.resources[ORE] -= blueprint[4]
        s3.resources[OBS] -= blueprint[5]
        s3.robots[GEO] += 1
        if s3.hash() not in seen:
            nxt.append(s3)
            return nxt

    if s.resources[ORE] >= blueprint[0] and s.robots[ORE] < max(blueprint[:3] + blueprint[4:5]):
        s3 = copy.deepcopy(s2)
        s3.resources[ORE] -= blueprint[0]
        s3.robots[ORE] += 1
        if s3.hash() not in seen:
            nxt.append(s3)

    if s.resources[ORE] >= blueprint[1] and s.robots[CLY] < blueprint[3]:
        s3 = copy.deepcopy(s2)
        s3.resources[ORE] -= blueprint[1]
        s3.robots[CLY] += 1
        if s3.hash() not in seen:
            nxt.append(s3)

    if s.resources[ORE] >= blueprint[2] and s.resources[CLY] >= blueprint[3] and s.robots[OBS] < blueprint[5]:
        s3 = copy.deepcopy(s2)
        s3.resources[ORE] -= blueprint[2]
        s3.resources[CLY] -= blueprint[3]
        s3.robots[OBS] += 1
        if s3.hash() not in seen:
            nxt.append(s3)
    
    return nxt

def bfs(blueprint, i, m = 24):
    max_geo = max_rob = 0
    s1 = State([1, 0, 0, 0], [0] * 4)
    q, seen = deque([s1]), {s1.hash()}
    while q:
        s = q.popleft()
        if len(seen) % 10000 == 0:
            print(i, s.minute)
        max_geo = max(max_geo, s.resources[GEO])
        max_rob = max(max_rob, s.robots[GEO])
        for s2 in get_next_states(blueprint, seen, max_geo, max_rob, s, m):
            seen.add(s2.hash())
            q.append(s2)

    return max_geo

def part1(blueprints):
    res = 0
    for i, b in enumerate(blueprints):
        res += (i+1) * bfs(b, i)
    return res

def part2(blueprints):
    return bfs(blueprints[0], 0, 32) * bfs(blueprints[1], 1, 32) * bfs(blueprints[2], 2, 32)

if __name__ == "__main__":
    blueprints = []
    for line in sys.stdin:
        blueprints.append([])
        for token in line.split():
            if token.isnumeric():
                blueprints[-1].append(int(token))

    # print(part1(blueprints))
    print(part2(blueprints))
