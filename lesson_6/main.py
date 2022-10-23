#month = int(input("Ввидити номир месица: "))
#if month.isdigit() and 1 <= int(month) <= 12:
#    month = int(month)
#    if 3 <= month <= 5:
#        print("Весныа")
#    elif 6 <= month <= 8:
#        print("Лэто")
#    elif 9 <= month <= 11:
#        print("Лэто")
#    else:
#        print("Зима")
#else:
#    print("Э, чувак, ты АшИбСя")
#h = int(input("Часы: "))
#m = int(input("Минуты: "))
#s = int(input("Секунды: "))
#
#if 23 >= h >= 0 and 59 >= m >= 0 and 59 >= s >= 0
#    print("Формат правилъно")
#    print(f"{h}:{m}:{s}")
#else:
#    print("Ошибка")
#    if h > 23 or h < 0:
#        print("Часы в формате [0, 23]")
#    if h > 59 or m < 0:
#        print("Минуты в формате [0, 59]")
#    if h > 59 or s < 0:
#        print("Секунды в формате [0, 59]")
q1 = input("Какого цвета трава?\n"
           "а)Что?, б)Апельсин, в)60 бойцов, г)Зелёная\n"
           "--> ")
if q1 == "г":
    score = score + 1
    print("Правильно!")
else:
    print("Одна ошибка - и ты ошибся!")
    print("Твой счёт:", score)
    quit()
q2 = input("Сколька ног у стандартных паукофф\n"
           "а)Шесть, б)Семь, в)Восемь, г)Девять\n"
           "--> ")
if q1 == "в":
    score = score + 1
    print("Правильно!")
else:
    print("Одна ошибка - и ты ошибся!")
    print("Твой счёт:", score)
    quit()
q3 = input("Сколько метров может прорыть крот за 1 ночь\n"
           "а)76, б)8, в)100, г) 175\n"
           "--> ")
if q1 == "8":
    score = score + 1
    print("Правильно!")
else:
    print("Одна ошибка - и ты ошибся!")
    print("Твой счёт:", score)
    quit()
