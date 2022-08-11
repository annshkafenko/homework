b = 0
n = input("Введіть число від 3 до 9: ")
if n.isdigit():
    n = int(n) + b
    if 9 >= n >= 3:
        print("ok")
    else:
        print("Знаходиться поза діапазоном")
else:
    print("Не є числом")