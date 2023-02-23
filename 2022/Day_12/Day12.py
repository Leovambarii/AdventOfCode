from collections import deque, defaultdict

directions = [(0,1),(1,0),(0,-1),(-1,0)]
with open("input.txt") as file:
    data = file.read().strip()
lines = [list(x) for x in data.split("\n")]
n = len(lines)
m = len(lines[0])
s_i,s_j = [(i,j) for i in range(n) for j in range(m) if lines[i][j] == "S"][0]
t_i,t_j = [(i,j) for i in range(n) for j in range(m) if lines[i][j] == "E"][0]
lines[s_i][s_j] = "a"
lines[t_i][t_j] = "z"
lines = [[ord(letter) - ord("a") for letter in line] for line in lines]
distance = defaultdict(lambda : 1000000)
part = 2
if part == 1:
    q = deque([(s_i, s_j)])
else:
    q = deque([(i,j) for i in range(n) for j in range(m) if lines[i][j] == 0])

for x,y in q:
    distance[x, y] = 0
    
sol = 100000
while len(q) > 0:
    c_i, c_j = q.popleft()
    if (c_i, c_j) == (t_i, t_j):
        sol = distance[t_i, t_j]
        print(sol)
        break
    for dx, dy in directions:
        n_i, n_j = c_i+dx, c_j+dy
        if n_i in range(n) and n_j in range(m):
            if lines[c_i][c_j] >= lines[n_i][n_j]-1:
                dist = distance[c_i,c_j]+1
                if dist < distance[n_i, n_j]:
                    q.append((n_i, n_j))
                    distance[n_i, n_j] = dist