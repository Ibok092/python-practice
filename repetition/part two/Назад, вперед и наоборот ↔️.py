x = [int(i) for i in input().split()]
for i in range(0, len(x) - 1, 2):
     x[i],x[i+1]=x[i+1],x[i] 
print(*x)