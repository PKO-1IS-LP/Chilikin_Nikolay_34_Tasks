a = int(input("Введите сторону А: "))
b = int(input("Введите сторону B: "))
c = int(input("Введите сторону C: "))

if (a + b > c) and (b + c > a) and (a + c > b) and a > 0 and b > 0 and c > 0:
    print("Треугольник существует")
else:
    print("Треугольника не существует")