klass1 = float(input("Введіть кількість учнів у 1-му класі"))
klass2 = float(input("Введіть кількість учнів у 2-му класі"))
klass3 = float(input("Введіть кількість учнів у 3-му класі"))
tables_1 = klass1 // 2
remain_1 = klass1 % 2
tables_2 = klass2 // 2
remain_2 = klass2 % 2
tables_3 = klass3 // 2
remain_3 = klass3 % 2
result = tables_1 + remain_1 + tables_2 + remain_2 + tables_3 + remain_3
print("Усього потрібно закупити ", result, " парт")
