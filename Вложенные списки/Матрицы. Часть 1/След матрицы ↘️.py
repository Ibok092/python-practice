n = int(input())
s = [input().split() for i in range(n)]
res = 0
for i in range(len(s)):
    res += int(s[i][i])
print(res)