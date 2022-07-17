handle = open("task2.txt", "r")

count = 0
for line in handle:
    count+=1
    print(f"Строка: {count}, количество слов в данной строке: {len(line.split(' '))}")

handle.close()