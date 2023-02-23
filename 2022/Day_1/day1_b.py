elf_cal = 0
elves = [0, 0, 0]
with open('input.txt') as file:
    for line in file:
        line = line.rstrip('\n')
        if line != '':
            elf_cal += int(line)
        else:
            elves.append(elf_cal)
            elves = sorted(elves)[1:]
            elf_cal = 0
print(sum(elves))