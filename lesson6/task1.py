import time


class TrafficLight:
    _color = "red"

    def running(self):
        while True:
            print(self._color)
            time.sleep(7)
            self._color = "yellow"
            print(self._color)
            time.sleep(2)
            self._color = "green"
            print(self._color)
            time.sleep(4)
            self._color = "red"

svetofor = TrafficLight()
svetofor.running()
