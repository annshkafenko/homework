string = input("Введіть рядок: ")
char = input("Введіть символ: ")
total = 0
start = 0
v = string.find(char)
while v >= 0:
    total += 1
    start = v + 1
    v = string.find(char, start)
print("Кіл-ть символів у даному рядку:  ", total)
