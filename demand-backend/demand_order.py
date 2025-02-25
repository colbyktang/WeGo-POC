from enum import Enum

# Class: Order
# Concern: Demand
# Required parameters:
    # username - String: Username of the user that placed the order
    # pickup_address - String: Address of the pickup location
    # dropoff_address - String: Address of the dropoff location
    # vehicle_type - String: The type of vehicle requested in the order
    # timestamp - String: Time the order was placed in MM-DD-YYYY: HH:MM:SS
# Optional variables
    # vehicle_eta - String: Estimated Time of Arrival of the order
    # vehicle_vin - String: Vehicle Identification Number of the vehicle assigned to the order
    # order_status - Order_Status -> String: Status of the order
        # NOT_COMPLETED = 0
        # IN_PROGRESS = 1
        # COMPLETED = 2
        # CANCELED = 3

####################### testing methods ####################################
#new_order = Order("jquade", "12203 Arrowwood dr. Austin TX", "St. Edwards", "bus", "March 4th 2020, 8:05:43 pm")

#print(new_order.get_username(),new_order.get_pickup_address(), new_order.get_dropoff_address())
#############################################################################

class Order:

    def __init__ (self, username, pickup_address, dropoff_address, vehicle_type, timestamp):
        self._id = 0
        self._username = username
        self._pickup_address = pickup_address
        self._dropoff_address = dropoff_address
        self._vehicle_type = vehicle_type
        self._timestamp = timestamp
        self._vehicle_eta = "N/A"
        self._vehicle_vin = "N/A"
        self._order_status = Order_Status.NOT_COMPLETED

    # getter method for order id, set upon adding order to database
    @property
    def id(self):
        return self._id

    # setter method for order id, set upon adding order to database
    @id.setter
    def id(self, id):
        self._id = id

    # getter method for username
    @property
    def username(self):
        return self._username

    # getter method for pickup address
    @property
    def pickup_address(self):
        return self._pickup_address

    # getter method for dropoff address
    @property
    def dropoff_address(self):
        return self._dropoff_address

    # getter method for vehicle type
    @property
    def vehicle_type(self):
        return self._vehicle_type

    # getter method for timestamp
    @property
    def timestamp(self):
        return self._timestamp

    # getter method for vehicle eta
    @property
    def vehicle_eta(self):
        return self._vehicle_eta

    # setter method for vehicle eta
    @vehicle_eta.setter
    def vehicle_eta(self, value):
        self._vehicle_eta = value

    # getter method for vehicle vin
    @property
    def vehicle_vin(self):
        return self._vehicle_vin

    # setter method for vehicle vin
    @vehicle_vin.setter
    def vehicle_vin(self, value):
        self._vehicle_vin = value

    # getter method for vehicle status
    @property
    def order_status(self):
        return Order_Status(self._order_status).name

    # setter method for order status
    @order_status.setter
    def order_status(self, status):
        # detect if status is an enum or an int
        if (type(status) == int):
            self._order_status = status
        elif (type(status) == Order_Status):
            self._order_status = status.value
        else:
            try:
                self._order_status = status
            except ValueError:
                print ("ORDER CLASS ERROR: Could not set order status! Neither enum nor int")

    # getter method for all values of order, does not include order_id
    @property
    def dictionary(self):
        order_dictionary = {
            "username": self.username,
            "pickup_address": self.pickup_address,
            "dropoff_address": self.dropoff_address,
            "vehicle_type": self.vehicle_type,
            "vehicle_eta": self.vehicle_eta,
            "vehicle_vin": self.vehicle_vin,
            "order_status": self.order_status,
            "timestamp": self.timestamp
        }
        return order_dictionary

    # update the order with the new info from supply side
    def update_order_with_vehicle(self, eta, vin, status):
        self.vehicle_eta = eta
        self.vehicle_vin = vin
        self.order_status = status

    # set the order to canceled status
    def cancel_order(self):
        self.order_status = Order_Status.CANCELED

class Order_Status(Enum):
    NOT_COMPLETED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CANCELED = 3