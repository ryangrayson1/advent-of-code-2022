import sys

def md(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def get_cover(ranges):
    ranges.sort()
    merged = []
    for l, r in ranges:
        if merged and merged[-1][1] >= l:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r))
        else:
            merged.append((l, r))
    res = 0
    for l, r in merged:
        res += r - l + 1
    return res

def part1(sensors, beacons):
    TGT = 2000000
    ranges, beacons_at_tgt = [], set()
    for (sr, sc), (br, bc) in zip(sensors, beacons):
        if br == TGT:
            beacons_at_tgt.add(bc)
        dist_from_tgt = abs(sr - TGT)
        width_at_mid = 2 * md(sr, sc, br, bc) + 1
        width_at_tgt = width_at_mid - 2 * dist_from_tgt
        if width_at_tgt > 0:
            ranges.append((sc - width_at_tgt // 2, sc + width_at_tgt // 2))
        
    return get_cover(ranges) - len(beacons_at_tgt)


def merge(ranges):
    ranges.sort()
    merged = []
    for l, r in ranges:
        if merged and merged[-1][1] + 1 >= l:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r))
        else:
            merged.append((l, r))
    
    return merged

def part2(sensors, beacons):
    MX = 4000000
    for TGT in range(2620000, 2630000):
        ranges, beacons_at_tgt = [], set()
        for (sr, sc), (br, bc) in zip(sensors, beacons):
            if br == TGT:
                beacons_at_tgt.add(bc)
            dist_from_tgt = abs(sr - TGT)
            width_at_mid = 2 * md(sr, sc, br, bc) + 1
            width_at_tgt = width_at_mid - 2 * dist_from_tgt
            if width_at_tgt > 0:
                ranges.append((sc - width_at_tgt // 2, sc + width_at_tgt // 2))
    
        merged = merge(ranges)
        trimmed = []
        for l, r in merged:
            if r < 0 or MX < l:
                continue
            trimmed.append((max(l, 0), min(r, MX)))
        
        if len(trimmed) > 1:
            col = trimmed[0][1] + 1
            # print(TGT, col)
            return TGT + 4000000 * col
    
    return -1
            

if __name__ == "__main__":
    sensors, beacons = [], []
    for line in sys.stdin:
        line = line.rstrip().split()
        sensors.append((int(line[3][2:-1]), int(line[2][2:-1])))
        beacons.append((int(line[9][2:]), int(line[8][2:-1])))
    
    print(part1(sensors, beacons))
    print(part2(sensors, beacons))
