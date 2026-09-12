n, m = [int(i) for i in input().split()]
matrix = [i for i in range(1, n * m + 1)]
res = []
for i in range(n):
    res.append(matrix[:m])
    del matrix[:m]
for el in res:
    for j in el:
        print(str(j).ljust(3), end="")
    print()