from functools import reduce

print(reduce(lambda acc, x: acc+x, [el for el in range(100,1001) if el % 2 == 0]))