while True:
    word_1 = input("Введіть перше слово: ")
    word_2 = input("Введіть друге слово: ")
    if word_1.isalpha() == True and word_2.isalpha() == True:
        word_1 = word_1[-1::-1]
        word_2 = word_2[-1::-1]
        word_1 = word_1.title()
        word_2 = word_2.title()
        print(word_1, word_2)
        break
    else:
        continue