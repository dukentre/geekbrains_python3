handle = open("task3.txt", "r")

count = 0
sum = 0
for line in handle:
    words = line.split(' ')
    count+=1
    salary = float(words[1])
    sum+= salary
    if salary < 20000:
        print(f"{words[0]} получает меньше 20000 рублей ({salary})")
handle.close()

print(f"Средняя зарплата {sum / count}")