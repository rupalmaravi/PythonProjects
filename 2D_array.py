# traverse 2d array
num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
i = 0
for rows in num_grid:
    for cols in rows:
        i = cols + 1
        print(i)
