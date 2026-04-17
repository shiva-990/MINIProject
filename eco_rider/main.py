from models.electric_car import ElectricCar
from models.electric_scooter import ElectricScooter

car = ElectricCar("KA-01", "Nexon EV", 80, 5)
scooter = ElectricScooter("KA-02", "Ather 450X", 60, 90)

print("Car trip cost:", car.calculate_trip_cost(10))
print("Scooter trip cost:", scooter.calculate_trip_cost(30))