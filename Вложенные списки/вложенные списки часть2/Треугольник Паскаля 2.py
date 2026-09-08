def pascal(n):
    suma = [1]
    for _ in range(n):
        print(*suma)
        v = []
        temp_suma = [0] + suma + [0]
        for i in range(1, len(temp_suma)):
            v.append(temp_suma[i - 1] + temp_suma[i])
        suma = v
pascal(int(input()))