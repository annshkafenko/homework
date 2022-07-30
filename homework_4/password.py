password1 = 12345
password2 = 13579
password3 = 1_000_000
user_password = int(input("Введіть пароль"))
if (user_password == password1) or (user_password == password2) or (user_password == password3):
    print("Пароль прийнято")
else:
    print("Неправильний пароль \nВам відмовлено у доступі")