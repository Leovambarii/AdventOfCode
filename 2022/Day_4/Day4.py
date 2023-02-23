def main_1():
    counter = 0
    with open('input.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            elf_1, elf_2 = line.split(',')
            elf_1_v = [int(x) for x in elf_1.split('-')]
            elf_2_v = [int(x) for x in elf_2.split('-')]
            if (elf_1_v[0] <= elf_2_v[0] and elf_1_v[1] >= elf_2_v[1]) or (elf_2_v[0] <= elf_1_v[0] and elf_2_v[1] >= elf_1_v[1]):
                counter += 1
    print(counter)

def main_2():
    counter = 0
    with open('input.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            elf_1, elf_2 = line.split(',')
            elf_1_v = [int(x) for x in elf_1.split('-')]
            elf_2_v = [int(x) for x in elf_2.split('-')]
            for i in range(elf_1_v[0], elf_1_v[1]+1):
                if i in range(elf_2_v[0], elf_2_v[1]+1):
                    counter += 1
                    break;
    print(counter)



if __name__ == "__main__":
    # main_1()
    main_2()