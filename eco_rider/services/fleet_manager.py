fleet_hubs = {}

# Add new hub
def add_hub(hub_name):
    if hub_name in fleet_hubs:
        print("Hub already exists!")
    else:
        fleet_hubs[hub_name] = []
        print(f"{hub_name} hub created successfully")

# Add vehicle to hub
def add_vehicle_to_hub(hub_name, vehicle):
    if hub_name not in fleet_hubs:
        print("Hub does not exist!")
    else:
        if vehicle in fleet_hubs[hub_name]:
            print(f"Duplicate vehicle ID {vehicle.vehicle_id} not allowed!")
        else:
            fleet_hubs[hub_name].append(vehicle)
            print(f"{vehicle.model} added to {hub_name}")

# Display all hubs
def display_fleet():
    for hub, vehicles in fleet_hubs.items():
        print(f"\nHub: {hub}")
        for v in vehicles:
            print(f" - {v.model} ({v.vehicle_id})")