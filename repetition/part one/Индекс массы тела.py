weight, height = float(input()), float(input())
imt = weight / (height * height)
if 25 >= imt >= 18.5:
    print("Оптимальная масса")
elif imt < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")