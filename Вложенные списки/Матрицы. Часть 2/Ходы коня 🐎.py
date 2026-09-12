hod = input()

ing = ["a", "b", "c", "d", "e", "f", "g", "h"]
y_kon = ing.index(hod[0])
x_kon = 8 - int(hod[1])

matrix = [["." for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i == x_kon and j == y_kon:
            matrix[i][j] = "N" 
        elif abs(i - x_kon) * abs(j - y_kon) == 2:
            matrix[i][j] = "*"

for row in matrix:
    print(*row)
