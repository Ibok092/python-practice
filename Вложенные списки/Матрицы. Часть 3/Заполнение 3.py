n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            matrix[i][j] = 1
for el in matrix:
    print(*el)