"""
Create a Vehicle class with max_speed and mileage instance attributes
Create a Vehicle class without any variables and methods
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
Create a Bus class that inherits from the Vehicle class. Give the capacity argument
of Bus.seating_capacity() a default value of 50.
Use the following code for your parent Vehicle class. You need to use method overriding.
Define property that should have the same value for every class instance
"""

class Vehicle:
    color = "white"
    def __init__(self, max, mile, name):
        self.max_speed = max
        self.mileage = mile
        self.name = name

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"the seating capacity of a {self.name} is {self.capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

volvo = Vehicle(200,150, "volvo")
print(volvo.max_speed)
school_bus = Bus(180,12,"school volvo")
print(school_bus.max_speed, school_bus.mileage, school_bus.name)
print(school_bus.seating_capacity())
print("the color of the bus is", school_bus.color)
