import re
from functools import reduce

handle = open("task6.txt","r")

items = {}

for line in handle:
    items[line.split(":")[0]] = reduce(lambda acc,num: int(acc) + int(num), re.findall(r'\d+', line))

print(items)

handle.close()