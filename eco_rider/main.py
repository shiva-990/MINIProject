from models.electric_car import ElectricCar
from models.electric_scooter import ElectricScooter


car = ElectricCar("KA-01", "Nexon EV", 80, 5)
scooter = ElectricScooter("KA-02", "Ather 450X", 60, 90)

# Store different objects in one list
vehicles = [car, scooter]


for v in vehicles:
    if isinstance(v, ElectricCar):
        cost = v.calculate_trip_cost(10)   # km
    else:
        cost = v.calculate_trip_cost(30)   # minutes

    print(f"{v.model} trip cost: {cost}")