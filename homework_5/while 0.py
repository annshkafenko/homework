total = 0
numb = 0
maximum = 0
minimum = 0
paired = 0
unpaired = 0

while True:
    n = int(input("Введіть ціле число: "))
    if n == 0:
        break
    else:
        total += n
        numb += 1
    if n > maximum:
        maximum = n
    if n % 2 == 0:
        paired += 1
    else:
        unpaired += 1



print("у"total)
print(total / numb)
print(maximum)
print("Кіл-сть парних:", paired)
print("Кіл-сть непарних: ", unpaired)








# # list1 = 0
# # numb = 0
# # while True:
#     n = int(input("Введіть ціле число: "))
#     if n == 0:
#         break
#     else:
#         list1 += n
#         numb += 1
# print(list1 / numb)
