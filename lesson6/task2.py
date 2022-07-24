class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_road_mass(self, asphalt_mass, depth):
        return self._length * self._width * asphalt_mass * depth


print(Road(20, 5000).get_asphalt_road_mass(25, 5))
