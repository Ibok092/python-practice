lines, columns = int(input()), int(input())
matrix = [[0] * columns for i in range(lines)]
matrix1 = matrix
for i in range(lines):
    for j in range(columns):
        matrix[i][j] = input()
for el in matrix:
    print(*el)
print()
for i in range(columns):
    for j in range(lines):
        print(matrix[j][i], end=" ")
    print()