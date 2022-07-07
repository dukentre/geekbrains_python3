import math

# Задание 1

dukentre = "hello"
privet = "goodbye"
print(dukentre, privet)

# Задание 2
seconds = int(input("Введите кол-во секунд "))
hours = math.floor(seconds / 60 / 60)
minutes = math.floor(seconds / 60 % 60)
seconds = math.floor(seconds % 60 % 60)
print(f"{ '0'+str(hours) if hours < 10 else hours}:{'0'+str(minutes) if minutes < 10 else minutes}:{'0'+str(seconds) if seconds < 10 else seconds}")

#Дальше некогда, потом доделаю