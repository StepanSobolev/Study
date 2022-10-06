class Planet:
    planet_list_radisuses = [0, ]

    def __init__(self, radius: int | float, gabarit: int | float, color: str, speed: int | float):
        self.radius = radius if max(Planet.planet_list_radisuses) < radius else (max(Planet.planet_list_radisuses) + 10)
        self.gabsrit = gabarit
        self.color = color
        self.speed = speed
        Planet.planet_list_radisuses.append(self.radius)


mars = Planet(15, 10, 'red', 20)
earth = Planet(20, 10, 'red', 20)
moon = Planet(15, 10, 'red', 20)
vener = Planet(30, 10, 'red', 20)
print(Planet.planet_list_radisuses)
print(f'{mars.radius=}, {earth.radius=} {moon.radius=} {vener.radius=}')
