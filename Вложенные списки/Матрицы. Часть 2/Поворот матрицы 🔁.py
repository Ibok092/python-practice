n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    p = 1
    for j in range(n):
        print(matrix[n - p][i], end=" ")
        p += 1
    print()