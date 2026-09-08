list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
suma = sum([sum(i) for i in list1]) / sum([len(i) for i in list1])
print(suma)