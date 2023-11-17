def maze(n, m, grid, start, target, k):
    if k >= 1:
        if start == target:
            return True
        else:
            if start[0] + 1 < n and grid[start[0] + 1][start[1]] == 0:
                if maze(n, m, grid, [start[0] + 1, start[1]], target, k - 1):
                    return True
            if start[0] - 1 >= 0 and grid[start[0] - 1][start[1]] == 0:
                if maze(n, m, grid, [start[0] - 1, start[1]], target, k - 1):
                    return True
            if start[1] + 1 < m and grid[start[0]][start[1] + 1] == 0:
                if maze(n, m, grid, [start[0], start[1] + 1], target, k - 1):
                    return True
            if start[1] - 1 >= 0 and grid[start[0]][start[1] - 1] == 0:
                if maze(n, m, grid, [start[0], start[1] - 1], target, k - 1):
                    return True
    return False

if __name__ == "__main__":
    n = 3
    m = 3
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
    start = [0, 0]
    target = [2, 2]
    k = 6

    print(maze(n, m, grid, start, target, k))
