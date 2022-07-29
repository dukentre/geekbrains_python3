class Cell:
    def __init__(self, cells):
        self.__cells = cells

    @property
    def cells(self):
        return self.__cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if (self.cells > other.cells):
            return Cell(self.cells - other.cells)
        else:
            return Exception("Количество ячеек становится отрицательным")

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_in_row):
        last_cells = self.cells
        output = ""
        while last_cells > 0:
            if (cells_in_row <= last_cells):
                output += "*" * cells_in_row
                last_cells -= cells_in_row
            else:
                output += "*" * last_cells
                last_cells = 0
            output += "\n"


        return output


cell1 = Cell(10)
cell2 = Cell(2)

print((cell1 + cell2).cells)
print((cell1 - cell2).cells)
print((cell1 * cell2).cells)
print((cell1 / cell2).cells)

print(Cell(38).make_order(4))
