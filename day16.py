from sys import stdin
from collections import defaultdict, deque

def bfs(pressure, adj, adj_w, valve):
    q, seen = deque([(valve, 0)]), {valve}
    while q:
        cur, dist = q.popleft()
        for nei in adj[cur]:
            if nei not in seen:
                seen.add(nei)
                if pressure[nei] > 0:
                    adj_w[valve].append((nei, dist + 1))
                q.append((nei, dist + 1))

def make_weighted(pressure, adj):
    # turn into weighted graph and exclude 0 valves
    adj_w = defaultdict(list)
    for valve in adj:
        if valve == "AA" or pressure[valve] > 0:
            bfs(pressure, adj, adj_w, valve)
    return adj_w

def dfs(pressure, adj_w, seen, cur, m):
    if m > 30:
        return 0
    mx = 0
    for nei, dist in adj_w[cur]:
        if nei not in seen:
            seen.add(nei)
            mx = max(mx, dfs(pressure, adj_w, seen, nei, m + dist + 1))
            seen.remove(nei)

    return mx + pressure[cur] * (30 - m + 1)

def part1(pressure, adj):
    adj_w = make_weighted(pressure, adj)
    return dfs(pressure, adj_w, set(), "AA", 1)

def dfs2(pressure, adj_w, seen, cur_p, cur_e, mp, me):
    if mp > 26 and me > 26 or (len(seen) == len(adj_w) - 1):
        return 0
    mx = 0
    for nei_p, dist_p in adj_w[cur_p]:
        for nei_e, dist_e in adj_w[cur_e]:
            if nei_p == nei_e:
                if nei_p not in seen:
                    seen.add(nei_p)
                    if mp <= 26:
                        mx = max(mx, pressure[cur_p] * (26 - mp + 1) + dfs2(pressure, adj_w, seen, nei_p, cur_e, mp + dist_p + 1, me))
                    if me <= 26:
                        mx = max(mx, pressure[cur_e] * (26 - me + 1) + dfs2(pressure, adj_w, seen, cur_p, nei_e, mp, me + dist_e + 1))
                    seen.remove(nei_p)
            elif nei_p not in seen and nei_e not in seen and mp <= 26 and me <= 26:
                seen.add(nei_p)
                seen.add(nei_e)
                mx = max(mx, pressure[cur_p] * (26 - mp + 1) + pressure[cur_e] * (26 - me + 1) + dfs2(pressure, adj_w, seen, nei_p, nei_e, mp + dist_p + 1, me + dist_e + 1))
                seen.remove(nei_p)
                seen.remove(nei_e)
    return mx

def generate_paths(paths, adj_w, seen, cur_path, valve, m):
    seen.add(valve)
    cur_path.append((valve, m))
    done = True
    for nei, dist in adj_w[valve]:
        if nei not in seen and m + dist + 1 <= 26:
            done = False
            generate_paths(paths, adj_w, seen, cur_path, nei, m + dist + 1)

    if done:
        paths.append(cur_path.copy())
    seen.remove(valve)
    cur_path.pop()

def part2(pressure, adj):
    adj_w = make_weighted(pressure, adj)
    print(len(adj_w))
    # return dfs2(pressure, adj_w, set(), "AA", "AA", 1, 1)
    paths = []
    generate_paths(paths, adj_w, set(), [], "AA", 1)
    print("done w paths")
    print(len(paths))
    # for p in paths:
    #     print(p)

    res = 0
    for i, p1 in enumerate(paths):
        print(i)
        for p2 in paths:
            early, both = {}, p1 + p2
            for v, m, in both:
                if v not in early or early[v] > m:
                    early[v] = m
            pressure_here = sum(pressure[v] * (26 - m + 1) for v, m in early.items())
            res = max(res, pressure_here)

    return res


if __name__ == "__main__":
    pressure = {}
    adj = defaultdict(list)
    for line in stdin:
        line = line.rstrip().split()
        valve = line[1]
        pressure[valve] = int(line[4].split('=')[-1][:-1])
        for nei in line[9:]:
            adj[valve].append(nei.replace(',', ''))

    print(part1(pressure, adj))
    # part2 takes like 10 min
    print(part2(pressure, adj))
