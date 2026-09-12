n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
for i in reversed(matrix):
    print(*i)