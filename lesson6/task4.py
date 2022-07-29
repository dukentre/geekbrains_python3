class Car:
    speed = 10
    color = "red"
    name = "priora"
    is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на{direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")


class TownCar(Car):
    def __init__(self):
        super()
        self.speed = 12

    def show_speed(self):
        if (self.speed > 60):
            print(f"Вы превысили скорость! Текущая скорость {self.speed}")
        else:
            print(f"Текущая скорость {self.speed}")


class WorkCar(Car):
    def __init__(self):
        super()
        self.speed = 35

    def show_speed(self):
        if (self.speed > 40):
            print(f"Вы превысили скорость! Текущая скорость {self.speed}")
        else:
            print(f"Текущая скорость {self.speed}")


class SportCar(Car):
    def __init__(self):
        super()
        self.speed = 199


class PoliceCar(Car):
    def __init__(self):
        super()
        self.is_police = True


tc = TownCar()
tc.speed = 182391
tc.show_speed()
tc.go()
tc.stop()
tc.turn("лево")
