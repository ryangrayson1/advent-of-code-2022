import sys

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def trim_move(N, move):
    if move < 0:
        return -(abs(move) % (N-1))
    return move % (N-1)

def part1(coords):
    N = len(coords)
    coords = list(enumerate(coords))
    for i in range(N):
        for j in range(N):
            if i == coords[j][0]:
                m = trim_move(N, coords[j][1])
                for _ in range(abs(m)):
                    if m < 0:
                        if j == 0:
                            swap(coords, j, N-1)
                            j = N - 1
                        else:
                            swap(coords, j, j-1)
                            j -= 1
                    else:
                        if j == N-1:
                            swap(coords, j, 0)
                            j = 0
                        else:
                            swap(coords, j, j+1)
                            j += 1
                break
    
    coords = [c for _, c in coords]
    z = coords.index(0)
    return coords[(z + 1000) % N] + coords[(z + 2000) % N] + coords[(z + 3000) % N]


def part2(coords):
    D = 811589153
    N = len(coords)
    coords2 = []
    for i, c in enumerate(coords):
        coords2.append((i, c * D))

    for _ in range(10):
        for i in range(N):
            for j in range(N):
                if i == coords2[j][0]:
                    m = trim_move(N, coords2[j][1])
                    for _ in range(abs(m)):
                        if m < 0:
                            if j == 0:
                                swap(coords2, j, N-1)
                                j = N - 1
                            else:
                                swap(coords2, j, j-1)
                                j -= 1
                        else:
                            if j == N-1:
                                swap(coords2, j, 0)
                                j = 0
                            else:
                                swap(coords2, j, j+1)
                                j += 1
                    break
    
    coords = [c for _, c in coords2]
    z = coords.index(0)
    return coords[(z + 1000) % N] + coords[(z + 2000) % N] + coords[(z + 3000) % N]
    

if __name__ == "__main__":
    coords = list(map(lambda k: int(k.rstrip()), sys.stdin))
    print(part1(coords.copy()))
    print(part2(coords.copy()))
