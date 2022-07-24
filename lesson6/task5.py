class Stationery:
    title = "Название"

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")

class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")

dukentre1 = Pen("Дукентр 1")
dukentre1.draw()
dukentre2 = Pencil("Дукентр 2")
dukentre2.draw()
dukentre3 = Handle("Дукентр 3")
dukentre3.draw()