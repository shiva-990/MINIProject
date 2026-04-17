from abc import ABC, abstractmethod

class Vehicle(ABC):   # 🔥 Abstract class
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model

        self.__battery_percentage = battery_percentage
        self.__maintenance_status = "Good"
        self.__rental_price = 0

    # ✅ Getters
    def get_battery(self):
        return self.__battery_percentage

    def get_maintenance_status(self):
        return self.__maintenance_status

    def get_rental_price(self):
        return self.__rental_price

    # ✅ Setters
    def set_battery(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print("Invalid battery percentage!")

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    def set_rental_price(self, price):
        if price >= 0:
            self.__rental_price = price
        else:
            print("Invalid rental price!")

    # 🔥 Abstract method
    @abstractmethod
    def calculate_trip_cost(self, value):
        pass