from models.vehicle import Vehicle


v1 = Vehicle("KA-01-1234", "Tata Nexon EV", 80)

print("Battery:", v1.get_battery())

# Update battery
v1.set_battery(90)
print("Updated Battery:", v1.get_battery())

print("Vehicle ID:", v1.vehicle_id)
print("Model:", v1.model)
