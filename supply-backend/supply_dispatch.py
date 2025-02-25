from enum import Enum
# Class: Dispatch
# Concern: Supply
# Required parameters:
    # start_timestamp - String: Time the vehicle started the order in MM-DD-YYYY: HH:MM:SS
    # stops - [String, String]: A list of stops for the route
    # route - [[Float, Float]]: Array of coordinates in the route
    # order_id - String: ID of the order that is assigned to the dispatch
    # vehicle_id - String: ID of the vehicle that is carrying out the dispatch

# Optional variables
    # end_timestamp - String:  Time the vehicle finishes the order in MM-DD-YYYY: HH:MM:SS
    # dispatch_status - Dispatch_Status -> String: Status of the dispatch
        # NOT_COMPLETED = 0
        # IN_PROGRESS = 1
        # COMPLETED = 2
        # CANCELED = 3
    # id - String: The id assigned when inserted into the database

####################### testing methods ####################################
# not real information
# new_dispatch = Dispatch (
#     "01-01-2020 11:11:11", 
#     ["3001 S Congress Avenue, Austin, TX", "1822 S Congress Avenue, Austin, TX"],
#     [[-97.735530, 30.267450]]
#     "2e12e12e2", 
#     "iuhuihhui"
# )

#print(new_dispatch.get_dictionary())
############################################################################

class Dispatch:

    def __init__ (self, start_timestamp, stops, route, order_id, vehicle_id = 0):
        self._start_timestamp = start_timestamp
        self._stops = stops
        self._route = route
        self._order_id = order_id
        self._vehicle_id = vehicle_id
        self._end_timestamp = ""

        self.dispatch_status = Dispatch_Status.NOT_COMPLETED
        self._id = 0

    # getter for dispatch id
    @property
    def id(self):
        return self._id
    
    # setter for dispatch id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def start_timestamp(self):
        return self._start_timestamp

    @property
    def end_timestamp(self):
        return self._end_timestamp

    @property
    def stops(self):
        return self._stops

    @property
    def route(self):
        return self._route

    @property
    def order_id(self):
        return self._order_id

    @property
    def vehicle_id(self):
        return self._vehicle_id

    # Return the string of enum
    @property
    def dispatch_status(self):
        return self._dispatch_status.name

    # setter for dispatch_status
    @dispatch_status.setter
    def dispatch_status(self, status):
        # if status is an int
        if (type(status) == int):
            self._dispatch_status = Dispatch_Status(status)
        # if status is an enum
        elif (type(status) == Dispatch_Status):
            self._dispatch_status = status
        # if status is a string
        elif type(status) == str:
            self._dispatch_status = Dispatch_Status[status.upper()]
        # if status is anything else, blow up
        else:
            print ("DISPATCH CLASS ERROR: Could not set dispatch status! Neither enum, string, nor int")
            raise Exception("Dispatch Status: " + status + " Data Type:" + type(status))

    # getter method for all values of dispatch in a dictionary
    @property
    def dictionary(self):
        dispatch_dictionary = {
            "start_timestamp": self.start_timestamp,
            "end_timestamp": self.end_timestamp,
            "stops": self.stops,
            "route": self.route,
            "order_id": self.order_id,
            "vehicle_id": self.vehicle_id,
            "dispatch_status": self.dispatch_status
        }
        return dispatch_dictionary

class Dispatch_Status(Enum):
    NOT_COMPLETED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CANCELED = 3