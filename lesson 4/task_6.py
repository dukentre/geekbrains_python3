from itertools import count, cycle

for i in count(3):
    print(i)
    if i == 10:
        break

count = 0;
for i in cycle([1,2,3,4,5,6,7,8]):
    print(i)
    if i == 8:
        count+=1
    if count == 2:
        break