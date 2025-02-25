from enum import Enum

# Class: Vehicle
# Concern: Supply
# Required parameters:
    # vin - String: Vehicle Identification Number
    # vehicle_name - String: Name of vehicle
    # vehicle_type - Vehicle_Type -> String: Type of the vehicle such as Bus, Van, Truck
    # vehicle_color - Vehicle_Color -> String: Color of the vehicle, such as Red, Blue, Green
    # is_available - Bool: Is the vehicle available for service?

# Optional parameters:
    # vehicle_position - [Float, Float]: The current position of the vehicle in latitude and longtitude pairs.

####################### testing methods ####################################
#new_vehicle = Vehicle("13rqwefasdfqefrqw", "Honda", "bus", "gray", True)

#print(new_vehicle.dictionary)
#############################################################################

class Vehicle:
    status_ok = "OK"
    status_otw = "OTW"
    status_done = "DONE"
    status_maint = "MAINT"

    def __init__ (self, vin, vehicle_name, vehicle_type, vehicle_color, is_available):
        self.vin = vin
        self.vehicle_name = vehicle_name
        self.vehicle_type = vehicle_type
        self.vehicle_color = vehicle_color
        self.is_available = is_available
        self.vehicle_status = self.status_ok
        self.vehicle_position = [0.0,0.0]

    # getter method for vin
    @property
    def vin(self):
        return self._vin

    # setter method for vin
    @vin.setter
    def vin(self, value):
        self._vin = value

    # getter method for vehicle name
    @property
    def vehicle_name(self):
        return self._vehicle_name

    @vehicle_name.setter
    def vehicle_name(self, value):
        self._vehicle_name = value

    # getter method for vehicle type
    @property
    def vehicle_type(self):
        return self._vehicle_type.name

    # setter method to set vehicle type, checks for enum
    @vehicle_type.setter
    def vehicle_type(self, v_type):
        if (type(v_type) == int):
            #print ("Vehicle Type, received an int")
            self._vehicle_type = Vehicle_Type(v_type)
        elif (type(v_type) == Vehicle_Type):
            #print ("Vehicle Type, received an enum")
            self._vehicle_type = v_type
        elif type(v_type) == str:
            #print ("Vehicle Type, received an str")
            self._vehicle_type = Vehicle_Type[v_type.upper()]
        else:
            print ("VEHICLE CLASS ERROR: Could not set vehicle color! Neither enum, string, nor int")
            raise Exception("Type: " + v_type)

    # getter method for vehicle color
    @property
    def vehicle_color(self):
        return self._vehicle_color.name

    # setter method to set vehicle type, checks for enum
    @vehicle_color.setter
    def vehicle_color(self, v_color):
        if type(v_color) == int:
            self._vehicle_color = Vehicle_Color(v_color)
        elif type(v_color) == Vehicle_Color:
            self._vehicle_color = v_color
        elif type(v_color) == str:
            self._vehicle_color = Vehicle_Color[v_color.upper()]
        else:
            print ("VEHICLE CLASS ERROR: Could not set vehicle color! Neither enum, string, nor int")
            raise Exception("Color: " + str(v_color))

    # getter method for vehicle availability
    @property
    def is_available(self):
        return self._is_available

    # setter method for vehicle availability
    @is_available.setter
    def is_available(self, value):
        if type(value) is bool:
            self._is_available = value
        else:
            raise Exception("Is available needs to be a bool: " + str(value))

    # getter method for vehicle position
    @property
    def vehicle_position(self):
        return self._vehicle_position

    # setter method for vehicle position
    @vehicle_position.setter
    def vehicle_position(self, value):
        #print (type(value))
        #print (type(value[0]))
        if type(value) == list and type(value[0]) == float:
            self._vehicle_position = value
        else:
            raise Exception("Position needs to be a [Float]: " + str(value))

    # getter method for vehicle position
    @property
    def vehicle_status(self):
        return self._vehicle_status

    # setter method for vehicle position
    @vehicle_status.setter
    def vehicle_status(self, value):
        if value is self.status_ok or value is self.status_otw or value is self.status_done or value is self.status_maint:
            self._vehicle_status = value
        else:
            raise Exception("ERROR: " + str(value) + " is not accepted")

    # getter method for all values of vehicle
    @property
    def dictionary(self):
        vehicle_dictionary = {
            "vin": self.vin,
            "vehicle_name": self.vehicle_name,
            "vehicle_type": self.vehicle_type,
            "vehicle_color": self.vehicle_color,
            "is_available": self.is_available,
            "vehicle_position": self.vehicle_position,
            "vehicle_status": self.vehicle_status
        }
        return vehicle_dictionary

class Vehicle_Type(Enum):
    BUS = 0
    TRUCK = 1
    VAN = 2

class Vehicle_Color(Enum):
    RED = 0
    BLUE = 1
    WHITE = 2
    GRAY = 3
    BLACK = 4
    YELLOW = 5
    SEA_FORM_GREEN = 6
    CAMO = 7