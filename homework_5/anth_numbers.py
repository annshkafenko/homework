n = int(input('задайте N: '))
for i in range(1, n):
    d = 10
    while (i >= d):
      d = d * 10
    if ((i*i) % d) == i:
      print('число ', i, 'квадрат ', i*i)
