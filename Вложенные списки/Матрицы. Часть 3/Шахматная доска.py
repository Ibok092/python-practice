n, m = [int(i) for i in input().split()]
matrix = [["." for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (j + i) % 2 != 0:
            matrix[i][j] = "*"
    print(*matrix[i])