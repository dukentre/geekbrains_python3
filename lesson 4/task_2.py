array = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# классика ниндзя кода
print([array[i] for i in range(len(array)) if (i > 0 and array[i] > array[i-1])])