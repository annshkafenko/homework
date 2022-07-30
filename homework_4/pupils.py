klass1 = float(input("Введіть кількість учнів у 1-му класі"))
klass2 = float(input("Введіть кількість учнів у 2-му класі"))
klass3 = float(input("Введіть кількість учнів у 3-му класі"))
tables = (klass1 + klass2 + klass3) // 2
remain = (klass1 + klass2 + klass3) % 2
print("Усього потрібно закупити ", tables + remain, " парт")
