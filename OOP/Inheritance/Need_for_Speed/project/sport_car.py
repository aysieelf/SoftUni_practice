from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION: float = 10

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption: float = Car.DEFAULT_FUEL_CONSUMPTION
        self.DEFAULT_FUEL_CONSUMPTION: float = self.fuel_consumption