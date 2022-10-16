#x = 7
#
#if x > 10:
#    print("Я сработал!")
#else:
#    print("Ну я тоже сработав")
#
#phrase = "я карта"
#if phrase == "ya karta": # равно ли?
#   print("Мы карты!")
#
#game = "dota2"
#if game != "brawl stars": # не равно?
#    print("ну мовна и поигвать")
#
#
#if x >= 10 and (x == 0 or x == 666):
#    print("Я не выполнюсь хоть и ошибок нет")
#else:
#    print("Ну я тоже сработав")
#
#
#number = int(input("Введи число: "))
#if number > 0:
#    print("Положительное")
#elif number == 0:
#    print("Нулик")
#else:
#    print("Отрицательное")
#
#
#year = int(input("Введи год: "))
#if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#    print("високосненько")
#else:
#    print("не високосненько :(")
#
#
#number_1 = int(input("Введи первое число: "))
#operation = input("Введи операцию(-,+,*,/)").strip()
# удалить пробелы
#number_2 = int(input("Введи второе число: "))
#lst = ["-","+","*","/"]
#
#if operation in lst:
#    if operation == "-":
#        print(number_1 - number_2)
#    elif operation == "+":
#        print(number_1 + number_2)
#    elif operation == "*":
#        print(number_1 * number_2)
#    else:
#        print(number_1 / number_2)
#
#
#
#number_1 = int(input("Введи первое число: "))
#number_2 = int(input("Введи второе число: "))
#number_3 = int(input("Введи третье число: "))
#
#counter_pol = 0
#counter_otr = 0
#
# проверка первого числа
#if number_1 < 0:
#    counter_otr += 1
#else:
#    counter_pol += 1
#
# проверка второго числа
#if number_2 < 0:
#     counter_otr += 1
#else:
#     counter_pol += 1
#
# проверка третьего числа
#if number_3 < 0:
#     counter_otr += 1
#else:
#     counter_pol += 1
#
#number_1 = int(input("Введи первое число: "))
#number_2 = int(input("Введи второе число: "))
#number_3 = int(input("Введи третье число: "))
#
#lst = [number_1, number_2, number_3]
#
#maxi = max(lst)
#mini = min(lst)
#print("Минимальное: ", mini)
#print("Максимальное: ", maxi)
#
#ticket = input("Введи номер билета(6 знаков): ")
#if len(ticket) == 6:
#    first_half = ticket[:3]
#    last_half = ticket[-3:]
#
#    first_sum = first_half[0] + first_half[1] + first_half[2]
#    last_sum = first_half[0] + first_half[1] + first_half[2]
#
#    if first_sum == last_sum:
#        print("Счастливый билет! Тебе повезло!")
#    else:
#        print("К сожалению, тебе не повезло :(")
#else:
    #print("Ты можешь по-русски, а?! 🤬")
    # на сегодня всё