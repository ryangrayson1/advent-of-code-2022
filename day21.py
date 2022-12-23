import sys

def dfs(monkeys, yelled, cur):
    if cur not in yelled:
        if len(monkeys[cur]) == 1:
            yelled[cur] = int(monkeys[cur][0])
        else:
            l, o, r = monkeys[cur]
            l_res = dfs(monkeys, yelled, l)
            r_res = dfs(monkeys, yelled, r)
            if o == '+':
                yelled[cur] = l_res + r_res
            elif o == '-':
                yelled[cur] = l_res - r_res
            elif o == '*':
                yelled[cur] = l_res * r_res
            else:
                yelled[cur] = l_res // r_res

    return yelled[cur]

def part1(monkeys):
    yelled = {}
    dfs(monkeys, yelled, "root")
    return int(yelled["root"])

def part2(monkeys):
    lo, hi = 0, 1000000000000000
    while lo <= hi:
        mid = (lo + hi) // 2
        yelled = {}
        monkeys["humn"] = [str(mid)]
        dfs(monkeys, yelled, "root")
        l, _, r = monkeys["root"]
        if yelled[l] == yelled[r]:
            return mid
        if yelled[l] < yelled[r]:
            hi = mid + 1
        else:
            lo = mid - 1
    return -1

if __name__ == "__main__":
    monkeys = {}
    for line in sys.stdin:
        line = line.rstrip().split()
        monkeys[line[0][:-1]] = line[1:]

    print(part1(monkeys))
    print(part2(monkeys))
