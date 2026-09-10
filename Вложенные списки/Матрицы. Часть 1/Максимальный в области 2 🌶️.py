n = int(input())
s = [[int(x) for x in input().split()] for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            res.append(s[i][j])
print(max(res))
