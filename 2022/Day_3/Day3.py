def main_1():
    sol = 0
    with open('input.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            com_1, com_2 = line[:len(line)//2], line[len(line)//2:]
            for _, x in enumerate(com_1):
                if x in com_2:
                    if x.islower():
                        sol += ord(x)-96
                    else:
                        sol += ord(x)-38
                    break
    print(sol)


def main_2():
    sol = 0
    with open('input.txt') as file:
        lines = []
        for line in file:
            lines.append(line.rstrip('\n'))
            if len(lines) == 3:
                for _, x in enumerate(lines[0]):
                    if x in lines[1] and x in lines[2]:
                        if x.islower():
                            sol += ord(x)-96
                        else:
                            sol += ord(x)-38
                        break
                lines.clear()
    print(sol)


if __name__ == "__main__":
    # main_1()
    main_2()