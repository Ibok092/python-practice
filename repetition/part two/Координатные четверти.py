quarter1 = 0
quarter2 = 0
quarter3 = 0
quarter4 = 0
def finding_a_quartera():
    global quarter1, quarter2, quarter3, quarter4
    for _ in range(int(input())):
        s = input().split()
        x = int(s[0])
        y = int(s[1])
        if x > 0 and y > 0:
            quarter1 +=1
        elif x < 0 and y > 0:
            quarter2 += 1
        elif x < 0 and y < 0:
            quarter3 += 1
        elif x > 0 and y < 0:
            quarter4 += 1
    return f'''Первая четверть: {quarter1}
Вторая четверть: {quarter2}
Третья четверть: {quarter3}
Четвертая четверть: {quarter4}'''
print(finding_a_quartera())