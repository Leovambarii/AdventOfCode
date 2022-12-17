import numpy as np

def main_1():
    with open('input.txt') as file:
        lines = file.read().strip().split()
    grid = [list(map(int, list(line))) for line in lines]
    n = len(grid)
    m = len(grid[0])
    grid = np.array(grid)
    counter = 0
    for i in range(n):
        for j in range(m):
            h = grid[i, j]
            if j == 0 or np.amax(grid[i, :j]) < h:
                counter += 1
            elif j == m-1 or np.amax(grid[i, j+1:]) < h:
                counter += 1
            elif i == 0 or np.amax(grid[:i, j]) < h:
                counter += 1
            elif i == n-1 or np.amax(grid[i+1:, j]) < h:
                counter += 1
    print(counter)

def main_2():
    with open('input.txt') as file:
        lines = file.read().strip().split()
    grid = [list(map(int, list(line))) for line in lines]
    n = len(grid)
    m = len(grid[0])
    grid = np.array(grid)
    dd = [[0, 1], [0,-1], [1,0], [-1,0]]
    sol = 0
    for i in range(n):
        for j in range(m):
            h = grid[i, j]
            score = 1
            for di, dj in dd:
                ii, jj = i, j
                dist = 0
                ii += di
                jj += dj
                while (0<= ii < n and 0 <= jj < m) and grid[ii, jj] < h:
                    dist += 1
                    ii += di
                    jj += dj
                    if (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] >= h:
                        dist += 1
                score *= dist
            sol = max(sol, score)
    print(sol)


if __name__ == "__main__":
    # main_1()
    main_2()