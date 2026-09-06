num = []
for i in range(int(input())):
    num.append(int(input()))
num1 = int(input())
flag = False
for i in range(0, len(num)):
    for j in range(i + 1, len(num)):
        if num[i] * num[j] == num1:
            flag = True
if flag:
    print("ДА")
else:
    print("НЕТ")