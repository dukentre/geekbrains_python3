from abc import ABC


class Clothes(ABC):
    def __init__(self, name):
        self.__name = name


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    def __str__(self):
        return f"Это пальто {str(self.__size)} размера"

    @property
    def material__count(self):
        return self.__size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height

    def __str__(self):
        return f"Это костюм для роста {str(self.__height)} см"

    @property
    def material__count(self):
        return 2 * self.__height + 0.3


my_coat = Coat("By dukentre", 231)
my_suit = Suit("By dukentre", 231)

print(my_coat, my_coat.material__count)
print(my_suit, my_suit.material__count)
