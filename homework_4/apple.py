# First task
pupils = float(input("Введіть кіл-ть школярів"))
apple = float(input("Введіть кіл-ть яблук"))
receive = apple // pupils
print("Кожному з школярів дістанеться ", receive, " яблук")
remaind = apple % pupils
print("В корзині залишиться ", remaind, "яблук")