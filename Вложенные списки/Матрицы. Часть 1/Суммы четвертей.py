n = int(input())
s = [[int(x) for x in input().split()] for _ in range(n)]
res1 = []
res2 = []
res3 = []
res4 = []
for i in range(n):
    for j in range(n):
        if i > j and i < n - 1 - j:
            res1.append(s[i][j])
        elif i > j and i > n - 1 - j:
            res2.append(s[i][j])
        elif i < j and i > n - 1 - j:
            res3.append(s[i][j])
        elif i < j and i < n - 1 - j:
            res4.append(s[i][j])
print(f"Верхняя четверть: {sum(res4)}")
print(f"Правая четверть: {sum(res3)}")
print(f"Нижняя четверть: {sum(res2)}")
print(f"Левая четверть: {sum(res1)}")
