def main_1():
    score = 0
    with open('input.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            opponent, me = line[0], line[2]
            score_chosen = {'X':1, 'Y':2, 'Z':3}
            score += score_chosen[me]
            me = me.replace('X', 'A').replace('Y', 'B').replace('Z', 'C')
            if me == opponent:
                score += 3
            else:
                if line == 'C X' or line == 'A Y' or line == 'B Z':
                    score += 6
    print(score)

def main_2():
    score = 0
    with open('input.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            opponent, result = line[0], line[2]
            score_chosen = {'X':0, 'Y':3, 'Z':6}
            score += score_chosen[result]
            lost_chosen = {'A':3, 'B':1, 'C':2}
            draw_chosen = {'A':1, 'B':2, 'C':3}
            win_chosen = {'A':2, 'B':3, 'C':1}
            if result == 'X':
                score += lost_chosen[opponent]
            elif result == 'Y':
                score += draw_chosen[opponent]
            else:
                score += win_chosen[opponent]
    print(score)


if __name__ == "__main__":
    # main_1()
    main_2()