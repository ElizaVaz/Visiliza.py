words = {"актёр", "тапёр", "щипцы", "почёт", "аллея", "отчёт", "капля", "дымок", "курица", "капиляр"}
wordss = {"дыра", "дом", "рыба", "я", "капуста", "пирог", "рог", "вина", "стремя", "имя", "вена"}
wordsss = {"выход" "жизнь", "старт", "финиш", "кровь", "утрата", "победа", "слеза", "смерть", "артерия"}
words = words | wordss | wordsss  # список слов который может попасться в игре
word = list(words.pop())

glasn = ["а", "у", "о", "и", "э", "ы", "я", "ю", "е", "ё"]
soglasn = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х"]
soglasn.extend(["ц", "ч", "ш", "щ", "ъ", "ь"])
bil = list()

print("В слове:", len(word), "букв.")
print("Чтобы выбрать один из вариантов введите соответсвующую ему цыфру.")
print("1. Правила игры (help()).")
print("2. Вывести все гласные, которые вы ещё не вводили.")
print("3. Вывести все согласные, которые вы ещё не вводили.")
print("4. Ввести букву.")
print("5. Ввести слово.")
x = ["_"] * len(word)
lives = 11
otvet = input().strip()
while x != word:    # цикл в котором вы либо угодаете слово либо потратите все жизни
    if otvet == "4":
        a = input("Введите предпологаемую букву: ").strip()
        if len(a) != 1:
            print("- ты уверен что это одна буква?")
        chance = 0
        stuped_n = 0
        while a in bil:
            print(f"Это буква уже была. Даю тебе {stuped_n} шанс.")
            stuped_n += 1
            a = input("Введите предпологаемую букву: ").strip()
        if a in glasn:
            bil.append(a)
            glasn.remove(a)
        elif a in soglasn:
            bil.append(a)
            soglasn.remove(a)
        else:
            print("Это вообще буква?")
            print("Мдэ...")
        for i in range(len(word)):
            if word[i] == a:
                x[i] = a
                chance = 1
                break
        for j in range(len(x)):
            print(x[j], end="")
        print("")
        if chance == 0:
            lives -= 1
            print("У вас осталось:", lives)
        if lives == 0:
            print("Вы проиграли!")
            print("____________________________________________\n_________$$$$$$$$$$$$$$$$$$$________________")
            print("________$$_________________$$$______________\n_______$_____________________$$$$___________")
            print("______$______$$$$$$_____________$$__________\n_____$____$$$$____$$$___$$$$$$$$_$$_________")
            print("____$$___$$_________$__$$_______$_$$________\n____$____$__________$__$________$__$________")
            print("____$____$_____$___$$__$____$___$__$________\n____$____$$________$____$______$$__$________")
            print("____$_____$$$$$$$$$______$$$$$$$___$________\n____$______________________________$________")
            print("____$$_____________________________$________\n_____$____________________________$$________")
            print("_____$$___________$$$$$$$$$_______$_________\n______$$________________________$$__________")
            print("________$$____________________$$$___________\n_________$$$$$$$$$$$$$$$$$$$$$$_____________")
            print("____________________________________________")
            break
        if x == word:
            print("Вы выйграли! Ураааааааа!")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢉⣉⣁⣀⣀⣈⣉⡉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⠿⠋⣀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠙⠿⣿⣿⣿⣿⣿\n⣿⣿⣿⡟⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⢻⣿⣿⣿")
            print("⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠙⣿⣿\n⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠙⣿⣿")
            print("⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠛⠿⠿⠿⠿⠛⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿\n⡟⢀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡀⢻")
            print("⠇⢸⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⡇⠘\n⠄⢸⣿⡄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⣆⠄⠄⠄⠄⠄⠄⠄⠄⢠⣿⡇⠄")
            print("⡆⢸⣿⣿⣷⣦⣤⣀⣀⣤⣤⣾⣿⣿⣿⣿⣿⣿⣷⣤⣤⣀⣀⣤⣴⣶⣿⣿⡇⢠\n⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼")
            print("⣿⡄⠸⣿⣿⣿⣿⣿⡈⠙⠻⠿⣿⣿⣿⣿⣿⣿⠿⠟⠋⢁⣿⣿⣿⣿⣿⠇⢠⣿\n⣿⣿⣄⠘⢿⣿⣿⣿⣿⣦⣄⡀⠄⠄⠈⠁⠄⠄⢀⣠⣴⣿⣿⣿⣿⡿⠃⣠⣿⣿")
            print("⣿⣿⣿⣧⡀⠙⢿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⡿⠋⢀⣴⣿⣿⣿\n⣿⣿⣿⣿⣿⣶⣄⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⣠⣴⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣈⣉⠉⠉⠉⠉⣉⣁⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    if otvet == "2":
        print(f"Вы ещё не называли гласные: {str(glasn)[1:-1]}.")
    if otvet == "3":
        print(f"Вы ещё не называли согласные: {str(soglasn)[1:-1]}.")
    print("1. Правила игры (help()).")
    print("2. Вывести все гласные, которые вы ещё не вводили.")
    print("3. Вывести все согласные, которые вы ещё не вводили.")
    print("4. Ввести букву.")
    print("5. Ввести слово.")
    otvet = input()

input()
