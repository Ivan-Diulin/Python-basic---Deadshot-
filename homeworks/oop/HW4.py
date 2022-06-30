# HW4
######################
import math  # 8. Importing math module to get Pi number


# 1. Creating a class Vehicle with Attributes: name, max_speed, and total_capacity.
# Including method: fare, which calculates the price of the trip.
# Formula: total_capacity * 100.
class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self, total_capacity):
        return total_capacity * 100


# 2. Creating classes Bus and Car that inherit Vehicle.
class Bus (Vehicle):

    # 5. Overriding 'fare' method for Bus class by adding an extra 10% to the fare.
    def fare(self, total_capacity):
        return total_capacity * 100 + int(0.1 * (total_capacity * 100))

    # 6. Adding used_capacity attribute for Bus (number of people on the bus).
    # If used_capacity exceeds total_capacity raising an error.
    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name, max_speed, total_capacity)
        if used_capacity > total_capacity:
            raise Exception("Error: used_capacity cannot exceed total_capacity! Program halt.")

    # 7.1. Writing a magic method to Bus that is triggered when len() function is called.
    # The bus length is calculated with total_capacity division by 10
    def __len__(self):
        return int(self.total_capacity/10)

    # 7.2. Writing a magic method to Bus that is triggered when bool() function is called.
    # (the right bus contains less than 100 passengers)
    def __bool__(self):
        if self.total_capacity < 100:
            return True
        return False


# 8. Creating class Engine with attribute volume and method get_volume() that will return volume
class Engine:
    def __init__(self, cylinder_r, cylinder_h, cylinder_num):
        self.cylinder_r = cylinder_r
        self.cylinder_h = cylinder_h
        self.cylinder_num = cylinder_num

    def get_volume(self):
        return int(math.pi * self.cylinder_r ** 2 *
                   self.cylinder_h * self.cylinder_num)


# 9. Inheriting Engine by Car class.
class Car (Vehicle, Engine):
    pass


# 1. Example: total_capacity = 50 => fare = 5000
vehicle_1 = Vehicle("Auto", 400, 50)
print(f"1.\nPrice of the trip with passenger capacity {vehicle_1.total_capacity}"
      f" is {vehicle_1.fare(vehicle_1.total_capacity)}.")

# 3.Creating 3 car objects and 2 bus objects
car_1 = Car("car_1", 200, 60)
car_2 = Car("car_2", 300, 70)
car_3 = Car("car_3", 100, 40)
bus_1 = Bus("bus_1", 100, 100, 75)
bus_2 = Bus("bus_2", 80, 200, 90)

# 4.1. Checking if the object car_1 is instance of a class Car
print(f"4.1.\nIs the 'car_1' object an instance of the 'Car' class?\nAnswer - {isinstance(car_1, Car)}")

# 4.2. Checking if the object car_2 is instance of a class Vehicle
print(f"4.2.\nIs the 'car_2' object an instance of the 'Vehicle' class?\nAnswer - {isinstance(car_2, Vehicle)}")

# 4.3. Checking if the object bus_1 is instance of a class Car
print(f"4.3.\nIs the 'bus_1' object an instance of the 'Car' class?\nAnswer - {isinstance(bus_1, Car)}")

# 4.4. Checking if the object bus_1 is instance of a class Vehicle
print(f"4.4.\nIs the 'bus_1' object an instance of the 'Vehicle' class?\nAnswer - {isinstance(bus_1, Vehicle)}")

# 5. Overriding fare method for Bus class by adding an extra 10% to the fare.

# Example for Bus class: total_capacity = 50 => total_fare = 5500
bus_1.total_capacity = 50
print(f"5.1.\nIf passenger capacity of bus_1 is {bus_1.total_capacity}"
      f" then total fare including 10% added will be {bus_1.fare(bus_1.total_capacity)}")

# For Car class objects like car_1 method 'fare' was unaltered so with total_capacity = 50 total_fare will be 5000
car_1.total_capacity = 50
print(f"5.2.\nIf passenger capacity of car_1 is {car_1.total_capacity}"
      f" then total fare will be {car_1.fare(car_1.total_capacity)}")

# 6. For example of raising an error in Bus class object: uncomment and run to raise exception:
# bus_3 = Bus("bus_3", 80, 200, 900)

# 7.1. Printing the results of len() function for Bus class objects using __len__ magic method.
print(f"7.1.\nThe length of bus_1 with total of {bus_1.total_capacity} passengers is {len(bus_1)} m.")
print(f"The length of bus_2 with total of {bus_2.total_capacity} passengers is {len(bus_2)} m.")

# 7.2. Using __bool__ magic method on Bus class objects with bool() function
# (the right bus contains less than 100 passengers)
print(f"7.2.\nThe bus_1 with total of {bus_1.total_capacity} passengers is {bool(bus_1)} bus.")
print(f"The bus_2 with total of {bus_2.total_capacity} passengers is {bool(bus_2)} bus.")

# 8.Using method get_volume() to calculate engine's volume with previously set parameters.
engine_1 = Engine(3, 5, 4)
print(f"8.\nThe volume of a {engine_1.cylinder_num}-cylinder engine with "
      f"cylinder radius {engine_1.cylinder_r} and cylinder height {engine_1.cylinder_h} "
      f"is: V = {engine_1.get_volume()}.")

# 10. Check what is inheritance order of the Car class
print(f"10.\nThe inheritance order of the Car class:\n {Car.mro()}.")
