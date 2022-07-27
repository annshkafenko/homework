print("Привіт, мене звати Джарвіс!\nЯ допоможу тобі виконати елементарні математичні задачі.")
name = input("Як до тебе звертатись?")
print("Приємно познайомитись,", name, "!")

p = "+"
m = "-"
d = "*"
de = "/"
opr = input("Яку операцію ти хочеш виконати?\nВведи її знак")
if (str(opr) == str(p)):
    a = float(input("Введи перше число"))
    b = float(input("Введи друге число"))
    print(a + b)
elif (str(opr) == str(m)):
    a = float(input("Введи перше число"))
    b = float(input("Введи друге число"))
    print(a - b)
elif (str(opr) == str(d)):
    a = float(input("Введи перше число"))
    b = float(input("Введи друге число"))
    print(a * b)
elif (str(opr) == str(de)):
    a = float(input("Введи перше число"))
    b = float(input("Введи друге число"))
    print(a / b)
else:print("Я поки що не можу виконати таку операцію")
print("Бувай!")