# Challange too hard - used posted solution and reviewed the code

import re
with open('input.txt') as file:
    lines = [re.split('[\\s=;,]+', x) for x in file.read().splitlines()]
G = {x[1]: set(x[10:]) for x in lines}
F = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
I = {x: 1<<i for i, x in enumerate(F)}
T = {x: {y: 1 if y in G[x] else float('+inf') for y in G} for x in G}
for k in T:
    for i in T:
        for j in T:
            T[i][j] = min(T[i][j], T[i][k]+T[k][j])

def visit(valve, minutes, state, flow, solution):
    solution[state] = max(solution.get(state, 0), flow)
    for valve_ in F:
        new_minutes = minutes-T[valve][valve_]-1
        if I[valve_] & state or new_minutes <= 0:
            continue
        visit(valve_, new_minutes, state | I[valve_], flow+new_minutes*F[valve_], solution)
    return solution

sol_1 = max(visit(valve='AA', minutes=30, state=0, flow=0, solution={}).values())
visited2 = visit(valve='AA', minutes=26, state=0, flow=0, solution={})
sol_2 = max(v1+v2 for k1, v1 in visited2.items() for k2, v2 in visited2.items() if not k1 & k2)
print(sol_1, sol_2)