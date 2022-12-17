sol = 0
elf_cal = 0
with open('input.txt') as file:
    for line in file:
        line = line.rstrip('\n')
        if line != '':
            elf_cal += int(line)
        else:
            if elf_cal > sol:
                sol = elf_cal
            elf_cal = 0
print(sol)