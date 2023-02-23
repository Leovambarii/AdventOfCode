def main_1():
    with open('input.txt') as file:
        line = file.readline().rstrip('\n')
        for i in range(len(line)-3):
            sequence = line[i:i+4]
            if len(set(sequence)) == 4:
                print(i+4)
                break
def main_2():
    with open('input.txt') as file:
        line = file.readline().rstrip('\n')
        for i in range(len(line)-13):
            sequence = line[i:i+14]
            if len(set(sequence)) == 14:
                print(i+14)
                break

if __name__ == "__main__":
    # main_1()
    main_2()