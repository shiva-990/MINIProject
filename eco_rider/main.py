from models.electric_car import ElectricCar
from models.electric_scooter import ElectricScooter
from services.fleet_manager import *


car = ElectricCar("KA-01", "Nexon EV", 80, 5)
scooter = ElectricScooter("KA-02", "Ather 450X", 60, 90)

# UC6: Fleet Management
add_hub("Downtown")
add_hub("Airport")

add_vehicle_to_hub("Downtown", car)
add_vehicle_to_hub("Downtown", scooter)

display_fleet()