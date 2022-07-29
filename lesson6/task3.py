class Worker:
    _income = {"wage": 0, "bonus": 0}
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


I = Position("Артем","Дукентров","Программист", 80000,20000)

print(I.get_full_name(),I.get_total_income())