#alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТ"
#
#print(alphabet[::-1]) # вывод в обратном порядке
# [start:end:step]
#
#phrase = "анТОН"
#print(phrase.upper()) # поднять в верхний регистр
#print(phrase.lower()) # поднять в нижний регистр
#
#phrase1 = "Я КАртА, я каРТа, я КаРтА..."
#print(phrase1.capitalize())
#familiya = input("Фамилия: ")
#imya = input("Имя: ")
#otchestvo = input("Отчество: ")
#print(familiya, imya[0] + ".", otchestvo[0] + ".")
#print(f"{familiya} {imya[0]} {otchestvo[0]}.")
#x = input()
#print(x.count('a')) # кол-во маленьких "а"
#x = input("Введите фразу, разделяя слова запятыми: ")
#lst = x.split(",")
#print(x.split(",")) # split - разделить, раско
#phrase = input("Введите фразу: ")
#find = input("Что меняем: ")
#replace = input("На что меняем: ")
#
#print(phrase.replace(find, replace))
alphabet = {
    " ": " ",
    "а": "Абоба",
    "б": "Банан",
    "в": "Витёк",
    "г": "Горох",
}
x = input("Введи фразу чего-то:")
rus = ""
for bukva in x:
    rus = rus + alphabet[bukva] + " "
print(rus)
