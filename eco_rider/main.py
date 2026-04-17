from models.electric_car import ElectricCar
from models.electric_scooter import ElectricScooter
from services.fleet_manager import *

# Existing setup
add_hub("Downtown")
add_hub("Airport")

car1 = ElectricCar("KA-01", "Nexon EV", 85, 5)
car2 = ElectricCar("KA-02", "MG ZS EV", 60, 5)
scooter = ElectricScooter("KA-03", "Ather 450X", 90, 90)

add_vehicle_to_hub("Downtown", car1)
add_vehicle_to_hub("Downtown", car2)
add_vehicle_to_hub("Airport", scooter)

# 🔍 UC8
search_by_hub("Downtown")
search_high_battery(80)