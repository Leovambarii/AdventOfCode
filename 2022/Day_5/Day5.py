def main_1():
    boxes_str = []
    stacks_numbers = []
    stacks = []
    flag = False
    with open('input.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            if line == '':
                flag = True
                stacks = boxes_str.pop().split(' ')
                for x in stacks:
                    if x.isnumeric():
                        stacks_numbers.append(int(x))
                stacks = [[] for _ in range(len(stacks_numbers))]

                for i in range(len(boxes_str)):
                    s = boxes_str[-1-i]
                    x = 0
                    for j in range(1, len(s), 4):
                        if s[j] != ' ':
                            stacks[x].append(s[j])
                        x += 1
                continue
            if not flag:
                boxes_str.append(line)
            else:
                line = line.split(' ')
                moves = int(line[1])
                stack_1 = int(line[3])-1
                stack_2 = int(line[5])-1
                for _ in range(moves):
                    stacks[stack_2].append(stacks[stack_1].pop())
    sol = ''
    for x in stacks:
        sol += x.pop()
    print(sol)

def main_2():
    boxes_str = []
    stacks_numbers = []
    stacks = []
    flag = False
    with open('input.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            if line == '':
                flag = True
                stacks = boxes_str.pop().split(' ')
                for x in stacks:
                    if x.isnumeric():
                        stacks_numbers.append(int(x))
                stacks = [[] for _ in range(len(stacks_numbers))]

                for i in range(len(boxes_str)):
                    s = boxes_str[-1-i]
                    x = 0
                    for j in range(1, len(s), 4):
                        if s[j] != ' ':
                            stacks[x].append(s[j])
                        x += 1
                continue
            if not flag:
                boxes_str.append(line)
            else:
                line = line.split(' ')
                moves = int(line[1])
                stack_1 = int(line[3])-1
                stack_2 = int(line[5])-1
                for i in range(moves):
                    stacks[stack_2].append(stacks[stack_1].pop(-moves+i))
    sol = ''
    for x in stacks:
        sol += x.pop()
    print(sol)



if __name__ == "__main__":
    # main_1()
    main_2()