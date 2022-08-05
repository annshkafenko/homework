
n = int(input("Введіть ціле число: "))
total = n
middle = 1
maximum = n
minimum = n
paired = 0
unpaired = 0
if n == 0:
    print("Перше число не може дорівнювати 0")
else:
    if n % 2 == 0:
        paired += 1
    else:
        unpaired += 1
while True:
    n = int(input("Введіть ціле число: "))
    if n == 0:
        break
    else:
        total += n
        middle += 1
        if n > maximum:
            maximum = n
        elif n < minimum:
            minimum = n
        if n % 2 == 0:
            paired += 1
        else:
            unpaired += 1

print(total)
print(total / middle)
print(maximum)
print(minimum)
print(paired)
print(unpaired)