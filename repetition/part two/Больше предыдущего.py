num = [int(i) for i in input().split()]
result = 0
for i in range(1, len(num)):
    if num[i - 1] < num[i]:
        result += 1
print(result)
