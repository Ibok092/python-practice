n = int(input())
m = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
mx = min(matrix[0])
for i in matrix:
    if max(i) > mx:
        mx = max(i)
        a, v = matrix.index(i), i.index(max(i))
print(a, v)