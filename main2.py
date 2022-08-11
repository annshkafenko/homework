# n = 0
# while n <= 0:
#   n = int(input("Введіть позитивне число: "))

# print(n)

# піднесення до степені
# k = 1
# while k < 10:
#   print( 2**k )
#  k += 1

# range(s, [stop], [step])

# r = range(10, 300, 5)
# print(r.__sizeof__())
# n = range(10, 3000000)
# print(r.__sizeof__())

# print(list(r))
# v = range(2, 2000)
# print(v[5])

# for i in range(1, 11):
#    print(2**i)

# print('/U0001F61A')

import time

cnt = 0
for i in range(10):
    if i % 2:
        print('\U0001FAF5', end='\r')
        time.sleep(1)
        cnt += 1
        print("+", cnt)
    if i % 3:
        print('\U0001F440', end='\r')
        time.sleep(1)
        cnt -= 1
        print("-", cnt)
    else:
        print('\U0000270B', end='\r')
        time.sleep(1)
        cnt *= 2
        print("*2", cnt)
