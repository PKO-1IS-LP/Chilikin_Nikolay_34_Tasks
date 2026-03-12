x = int(input("Введите число: "))
for y in range(2, x + 1):
    if x % y == 0:
        print(y)
        break