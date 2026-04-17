from models.electric_car import ElectricCar
from models.electric_scooter import ElectricScooter
from services.fleet_manager import *


car1 = ElectricCar("KA-01", "Nexon EV", 80, 5)
car2 = ElectricCar("KA-01", "Duplicate Nexon", 70, 5)  # SAME ID

add_hub("Downtown")

add_vehicle_to_hub("Downtown", car1)
add_vehicle_to_hub("Downtown", car2) 

display_fleet()