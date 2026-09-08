def pascal(n):
    suma = [0, 1, 0]
    for _ in range(n):
        v = []
        for i in range(1, len(suma)):
            v.append(suma[i - 1] + suma[i])
        suma = [0] + v + [0]
    return suma[1:-1]
print(pascal(int(input())))
