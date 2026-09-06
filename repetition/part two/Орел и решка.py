s = input() + "О"
cnt1 = 0
cnt = 0
for i in range(len(s)):
    if s[i] == "Р":
        cnt += 1
    else:
        if cnt > cnt1:
            cnt1 = cnt
        cnt = 0
print(cnt1)