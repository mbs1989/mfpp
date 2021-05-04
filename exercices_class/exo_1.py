"""
Create a Vehicle class with max_speed and mileage instance attributes
"""

class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def seatin_capacity(self, capacity):
        self.capacity = capacity
        return f"la capacite du vehicule {self.name} est {self.capacity}"

    def fare(self):
        result = self.capacity * 100
        return print("le resultat est", result)

class Bus(Vehicle):
    def seatin_capacity(self, capacity=60):
        self.capacity = capacity
        return f"la capacité du bus {self.name} est {self.capacity}"

scania = Bus(60, 100, "scania")
print(scania.max_speed)
print(scania.seatin_capacity(160))
print(scania.color)
print(scania.fare())
print(type(scania))
print(isinstance(scania, Vehicle))

volvo = Vehicle(150, 50, "volvo")
print(volvo.max_speed)
print(volvo.mileage)
print(volvo.seatin_capacity(5))
