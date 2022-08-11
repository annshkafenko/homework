# cnt = 0
# while cnt < 10:
#     cnt += 1
#     print(cnt, "ddd")
#     if cnt % 2:
#         continue
#
#     print("I`M HERE", cnt)
# else:
#     print("Hi")
b = 0
n = input("Введіть число від 3 до 9: ")
if n.isdigit():
    n = int(n) + b
    if 9 >= n >= 3:
        print("ok")
    else:
        print("xyu")
else:
    print("no")
