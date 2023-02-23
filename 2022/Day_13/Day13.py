# Challange too hard - used posted solution and reviewed the code
with open("input.txt") as file:
    data = file.read().strip()

data = data.split("\n\n")
pairs = []
for pair in data:
    line_1, line_2 = pair.split("\n")
    pairs.append((eval(line_1), eval(line_2)))
data = pairs

def comparing(a,b):
    if type(a) is int and type(b) is int:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    elif type(a) is list and type(b) is int:
        b = [b]
    elif type(a) is int and type(b) is list:
        a = [a]
    n = len(a)
    m = len(b)
    for aa, bb in zip(a, b):
        result = comparing(aa, bb)
        if result != 0:
            return result
    if n < m:
        return -1
    elif n == m:
        return 0
    else:
        return 1

sol = 0
for i, (line_1, line_2) in enumerate(data):
    if comparing(line_1, line_2) == -1:
        sol += i+1
print(sol)

# Part 2
packets = []
for line_1, line_2 in data:
    packets.append(line_1)
    packets.append(line_2)

packets.append([[2]])
packets.append([[6]])

for i in range(len(packets)):
    for j in range(len(packets)-1):
        if comparing(packets[j], packets[j+1]) > 0:
            packets[j], packets[j+1] = packets[j+1], packets[j]

divisor_position_1, divisor_position_2 = [i for i in range(len(packets)) if packets[i] == [[2]] or packets[i] == [[6]]]
print((divisor_position_1+1)*(divisor_position_2+1))