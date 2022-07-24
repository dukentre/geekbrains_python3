from functools import reduce

def tryParseInt(s):
    try:
        return int(s)
    except ValueError:
        return 0

handleWrite = open("task5.txt", "w", encoding="utf-8")

for i in range(255):
    handleWrite.write(f"{i} ")

handleWrite.close()

handleRead = open("task5.txt", "r")

print(reduce(lambda acc,num: tryParseInt(acc) + tryParseInt(num), handleRead.readline().split(" ")))

handleRead.close()