from models.electric_car import ElectricCar
from models.electric_scooter import ElectricScooter

# Create objects
car = ElectricCar("KA-01-1234", "Tata Nexon EV", 80, 5)
scooter = ElectricScooter("KA-01-5678", "Ather 450X", 60, 90)

# Access inherited + own attributes
print("Car:", car.vehicle_id, car.model, car.seating_capacity)
print("Scooter:", scooter.vehicle_id, scooter.model, scooter.max_speed_limit)

# Access encapsulated data
print("Car Battery:", car.get_battery())