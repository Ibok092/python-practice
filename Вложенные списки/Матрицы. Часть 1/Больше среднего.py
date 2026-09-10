n = int(input())
s = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(n):
    res = 0
    for j in range(n):
        if sum(s[i]) / len(s[i]) < s[i][j]:
            res += 1
    print(res)
