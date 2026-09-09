s = input().split() + [0]
res = []
p = 1
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        p += 1
    else:
        res.append([s[i - 1]] * p)
        p = 1
print(res)
