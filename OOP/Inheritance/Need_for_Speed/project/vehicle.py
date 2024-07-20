class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption: float = 1.25
        self.fuel: float = fuel
        self.horse_power: int = horse_power

    def drive(self, kilometers):
        if self.fuel - (kilometers * self.fuel_consumption) >= 0:
            self.fuel -= (kilometers * self.fuel_consumption)
