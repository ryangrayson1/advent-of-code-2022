import sys

def compare(p, q):
    if type(p) is int and type(q) is int:
        if p < q:
            return -1
        if p > q:
            return 1
        return 0
    
    if type(p) is int:
        p = [p]
    if type(q) is int:
        q = [q]

    for a, b in zip(p, q):
        c = compare(a, b)
        if c != 0:
            return c
    
    if len(p) < len(q):
        return -1
    if len(p) > len(q):
        return 1
    return 0

class Packet:
    def __init__(self, p):
        self.p = p
    def __lt__(self, other):
        return compare(self.p, other.p) == -1

def part1(packets):
    res = 0
    for i in range(0, len(packets), 2):
        if compare(packets[i], packets[i+1]) < 1:
            res += i // 2 + 1
    return res

def part2(packets):
    packets.append([[2]])
    packets.append([[6]])
    packet_objects = [Packet(p) for p in packets]
    packet_objects.sort()
    res = 1
    for i, pobj in enumerate(packet_objects):
        if pobj.p == [[2]] or pobj.p == [[6]]:
            res *= (i+1)
    return res

if __name__ == "__main__":
    packets = []
    for i, line in enumerate(sys.stdin):
        if (i+1) % 3 == 0:
            continue
        stack = [[]]
        num = ""
        for c in line.rstrip()[1:-1]:
            if c == '[':
                stack.append([])
            elif c == ']':
                if num != "":
                    stack[-1].append(int(num))
                    num = ""
                stack[-2].append(stack.pop())
            elif c.isnumeric():
                num += c
            else:
                if num != "":
                    stack[-1].append(int(num))
                    num = ""
        if num != "":
            stack[-1].append(int(num))

        packets.append(stack[0])
    
    print(part1(packets))
    print(part2(packets))
