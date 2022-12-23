import sys
from collections import defaultdict, Counter

def part1(size):
    res = 0
    for sz in size.values():
        if sz <= 100000:
            res += sz
    return res

def part2(size):
    space_avail = 70000000 - size['/']
    to_free = 30000000 - space_avail
    for sz in sorted(size.values()):
        if sz >= to_free:
            return sz

def dfs(children, size, cur):
    for nxt in children[cur]:
        size[cur] += dfs(children, size, nxt)
    return size[cur]

def get_dir_sizes():
    children = defaultdict(set)
    size = Counter()
    dir_stack = ['/']
    id = 0
    for line in sys.stdin:
        args = line.rstrip().split()
        if args[0] == '$':
            if args[1] == "cd":
                if args[2] == "..":
                    dir_stack.pop()
                else:
                    d = '/'.join(dir_stack + [args[2]])
                    children[dir_stack[-1]].add(d)
                    dir_stack.append(d)
        else:
            if args[0] == "dir":
                children[dir_stack[-1]].add(args[1])
            else:
                size[dir_stack[-1]] += int(args[0])
        id += 1

    dfs(children, size, '/')
    return size

if __name__ == "__main__":
    input()
    size = get_dir_sizes()
    print(part1(size))
    print(part2(size))
    