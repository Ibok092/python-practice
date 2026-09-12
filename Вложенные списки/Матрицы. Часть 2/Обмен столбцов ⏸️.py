n = int(input())
m = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
a, b = [int(i) for i in input().split()]

for i in range(n):
    for j in range(m):
        if j == a:
            matrix[i][j], matrix[i][b] = matrix[i][b], matrix[i][j]
for el in matrix:
    print(*el)