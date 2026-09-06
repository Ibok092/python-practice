num = [input() for i in range(int(input()))]
virus = "anton"
for el in num:
    p = 0
    for i in el:
        if i == virus[p]:
            p += 1
            if p == 5:
                break
    if p == 5:
        print(num.index(el) + 1, end=" ")