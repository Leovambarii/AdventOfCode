def main_1():
    def check(cycles, cycle, result):
        cycle += 1
        if cycle in cycles:
            result += cycle * X
        return cycle, result
    cycles = [20, 60, 100, 140, 180, 220]
    result = 0
    X = 1
    cycle = 0
    with open('input.txt') as file:
        for line in file:
            l = line.rstrip('\n').split(' ')
            if l[0] == 'noop':
                cycle, result = check(cycles, cycle, result)
            else:
                val = int(l[1])
                cycle, result = check(cycles, cycle, result)
                cycle, result = check(cycles, cycle, result)
                X += val
    print(result)






def main_2():
    def check(cycles, cycle, result, pixels):
        cycle += 1
        pos = (cycle-1)%40
        if pos in {X-1, X, X+1}:
            pixels[cycle-1] = "#"
        return cycle, result
    pixels = list('.'*40*6)
    cycles = [20, 60, 100, 140, 180, 220]
    result = 0
    X = 1
    cycle = 0
    with open('input.txt') as file:
        for line in file:
            l = line.rstrip('\n').split(' ')
            if l[0] == 'noop':
                cycle, result = check(cycles, cycle, result, pixels)
            else:
                cycle, result = check(cycles, cycle, result, pixels)
                cycle, result = check(cycles, cycle, result, pixels)
                X += int(l[1])
    for i in range(0, 201, 40):
        print(''.join(pixels[i: i+40]))



if __name__ == "__main__":
    # main_1()
    main_2()