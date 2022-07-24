def numToRus(num):
    numbers = {
        1: "Один",
        2: "Два",
        3: "Три",
        4: "Четыре"
    }

    return numbers[num]


handle = open("task4.txt", "r")
handleWrite = open("task4-write.txt", "w", encoding="utf-8")

for line in handle:
    words = line.split(" ")
    print(numToRus(int(words[2][0:1])))
    handleWrite.write(f"{numToRus(int(words[2][0:1]))} - {words[2][0:1]} \n")

handle.close()

handleWrite.close()
