import random
import vin_generator
from supply_vehicle import Vehicle
from supply_vehicle import Vehicle_Type
from supply_vehicle import Vehicle_Color

# Class: Vehicle Generator
# Concern: Supply/Testing
# Vehicle parameters:
    # vin - String - Vehicle Identification Number
    # vehicle_name - String - Name of vehicle
    # vehicle_type - String - Type of the vehicle such as Bus, Van, Truck
    # vehicle_color - String - Color of the vehicle, such as Red, Blue, Green
    # is_available - Bool - Is the vehicle available for service?

class Vehicle_Generator:
    
    # Return a string of a vehicle name that is generated from the vin,
    # vehicle type, and vehicle color
    def generate_name(self, vin, vehicle_type, vehicle_color):
        serial_number = vin[9:]
        vehicle_type_letter = vehicle_type[0]
        vehicle_color_letter = vehicle_color[0]
        random_number_sequence = str(int(random.random() * 9)) + str(int(random.random() * 9)) + str(int(random.random() * 9))
        name = "A" + vehicle_type_letter + "-" + vehicle_color_letter + random_number_sequence + "-" + serial_number

        return name

    # Return a vehicle with a randomly generated vin, random type, random color,
    # random availability, random name based on this randomly generated information
    def generate_vehicle(self):
        vin = vin_generator.VIN().get_vin()
        vehicle_type = random.choice(list(Vehicle_Type)).name
        vehicle_color = random.choice(list(Vehicle_Color)).name
        is_available = True
        vehicle_name = self.generate_name(vin, vehicle_type, vehicle_color)

        return Vehicle (vin, vehicle_name, vehicle_type, vehicle_color, is_available)

    
