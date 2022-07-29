class Matrix:
    def __init__(self, matrix):
        self.__matrix = matrix

    def __str__(self):
        output = ""
        for row in self.__matrix:
            for col in row:
                output += str(col) + " "
            output += "\n"
        return output

    def __add__(self, other):
        new__array = self.__matrix.copy()
        for row in range(len(new__array)):
            for col in range(len(new__array[row])):
                new__array[row][col] += other[row][col]
        return Matrix(new__array)

    def __getitem__(self, item):
        return self.__matrix[item]


matrix = Matrix([
    [2, 3, 4, 5],
    [2, 4, 4, 1],
    [2, 5, 5, 5],
])

matrix2 = Matrix([
    [9, 9, -9, -9],
    [4, 4, 4, 4],
    [12312, -21321, 333, 1],
])
print(matrix)
print(matrix + matrix2)
