def main_1():
    with open('input.txt') as file:
        head_i, head_j = 0, 0
        tail_i, tail_j = 0, 0
        my_set = set()
        my_set.add(tuple([0,0]))
        for line in file:
            l = line.rstrip('\n').split(' ')
            k, a = l[0], int(l[1])
            for _ in range(a):
                if k == 'U':
                    head_j += 1
                elif k == 'D':
                    head_j -= 1
                elif k == 'R':
                    head_i += 1
                else:
                    head_i -= 1

                if abs(head_i-tail_i)<2 and abs(head_j-tail_j)<2:
                    continue
                if abs(head_i-tail_i)>=2 and head_j==tail_j:
                    if head_i>tail_i:
                        tail_i += 1
                    else:
                        tail_i -= 1
                elif abs(head_j-tail_j)>=2 and head_i==tail_i:
                    if head_j>tail_j: tail_j += 1
                    else: tail_j -= 1
                elif head_i != tail_i and head_j != tail_j:
                    if head_i > tail_i:
                        tail_i += 1
                    else:
                        tail_i -= 1
                    if head_j > tail_j:
                        tail_j += 1
                    else:
                        tail_j -= 1
                my_set.add(tuple([tail_i, tail_j]))
    print(len(my_set))





def main_2():
    pass



if __name__ == "__main__":
    main_1()
    # main_2()