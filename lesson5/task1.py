handle = open("task1.txt", "w")
print("Вводите слова для записи в файл. Чтобы завершить запись, введите пустую строку.")
while True:
    text = input()
    if(text == ''):
        break
    handle.write(text+"\n")
handle.close()