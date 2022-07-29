# Задание 1

array = [2, '3', True, [1, 2, 3], {1, 2, 3}, (31231, 121)]
for el in array:
    print(type(el))

# Задание 2

array = list(input("Введите список символов: "))
for i in range(0, len(array), 2):
    print(i)
    if i+1 < len(array):
        array[i], array[i + 1] = array[i + 1], array[i]
print(array)

# Задание 3

array = ["Зима","Зима","Весна","Весна","Весна","Лето","Лето","Лето","Осень","Осень","Осень","Зима"]
dictionary = {
    1: "Зима",
    2: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима",
}
month = int(input("Укажите месяц: "))
print(array[month])
print(dictionary[month])

# Задание 4

string = input("Введите слова через пробел: ")
array = string.split(" ")
for i in range(len(array)):
    print(f"{i}: {array[i][:10]}")

# Задание 5__

array = []
while True:
    number = input("Введите число: ")
    try:
        index = array.index(number)
        array.insert(index,number)
    except:
        array.append(number)
    print(array)