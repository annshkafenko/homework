n = input("Введіть число: ")
result = ""
for i in n:
    if n.count(i) >= 2:
        result = "yes"
        break
    else:
        result = "no"
print(result)