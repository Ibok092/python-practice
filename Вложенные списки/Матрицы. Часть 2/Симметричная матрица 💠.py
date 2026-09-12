n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
flag = "YES"
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i] and i != j:
            flag = "NO"
            break
    if flag == "NO":
        break
print(flag)