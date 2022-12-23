def part1(s):
    for i in range(3, len(s)):
        if len(set(s[i-3:i+1])) == 4:
            return i+1

def part2(s):
    for i in range(13, len(s)):
        if len(set(s[i-13:i+1])) == 14:
            return i+1

if __name__ == "__main__":
    s = input()
    print(part1(s))
    print(part2(s))
