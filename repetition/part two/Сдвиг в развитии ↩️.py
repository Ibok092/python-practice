x = [int(i) for i in input().split()]
last = x.pop()
x.insert(0, last)
print(*x)