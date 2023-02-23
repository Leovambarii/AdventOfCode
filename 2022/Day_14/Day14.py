def calc_turns_1(abyss, blocked):
    turns = 0
    while True:
        start = [500, 0]
        while True:
            if start[1] >= abyss:
                print(turns)
                return
            if tuple([start[0], start[1]+1]) not in blocked:
                start[1] += 1
                continue
            if tuple([start[0]-1, start[1]+1]) not in blocked:
                start[0] -= 1
                start[1] += 1
                continue
            if(tuple([start[0]+1, start[1]+1])) not in blocked:
                start[0] += 1
                start[1] += 1
                continue
            blocked.add(tuple(start))
            turns += 1
            break

def calc_turns_2(abyss, blocked):
    turns = 0
    while tuple([500, 0]) not in blocked:
        start = [500, 0]
        while True:
            if start[1] >= abyss:
                break
            if tuple([start[0], start[1]+1]) not in blocked:
                start[1] += 1
                continue
            if tuple([start[0]-1, start[1]+1]) not in blocked:
                start[0] -= 1
                start[1] += 1
                continue
            if(tuple([start[0]+1, start[1]+1])) not in blocked:
                start[0] += 1
                start[1] += 1
                continue
            break
        blocked.add(tuple(start))
        turns += 1
    print(turns)

def main():
    blocked = set()
    abyss = 0
    with open('input.txt') as file:
        for line in file:
            x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
            for (x1, y1), (x2, y2) in zip(x, x[1:]):
                for x in range(min([x1, x2]), max([x1, x2])+1):
                    for y in range(min([y1, y2]), max([y1, y2])+1):
                        blocked.add(tuple([x, y]))
                        abyss = max(abyss, y+1)

    # calc_turns_1(abyss, blocked)
    calc_turns_2(abyss, blocked)

if __name__ == "__main__":
    main()