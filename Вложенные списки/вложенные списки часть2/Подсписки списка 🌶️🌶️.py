s = input().split
res = [[]]
for i in range(len(s)):
    p = 1
    for j in range(i, len(s)):
        res.append(s[i: i + p])
        p += 1
print(res)