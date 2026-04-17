from models.vehicle import Vehicle


v1 = Vehicle("KA-01-1234", "Tata Nexon EV", 80)


print("Vehicle ID:", v1.vehicle_id)
print("Model:", v1.model)
print("Battery:", v1.battery_percentage)