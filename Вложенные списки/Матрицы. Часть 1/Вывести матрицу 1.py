lines, columns = int(input()), int(input())
matrix = [[0] * columns for i in range(lines)]
for i in range(lines):
    for j in range(columns):
        matrix[i][j] = input()
for el in matrix:
    print(*el)