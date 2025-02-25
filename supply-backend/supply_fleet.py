class Fleet:

    def __init__ (self, fleet_name, fleet_vehicle):
        self.fleet_name = fleet_name
        self.fleet_vehicle = fleet_vehicle

    # getter method for fleet name
    def get_fleet_name(self):
        return self.fleet_name

    # getter method for fleet vehicle
    def get_fleet_vehicle(self):
        return self.fleet_vehicle

    # getter method for all values of fleet
    def get_dictionary(self):
        fleet_dictionary = {
            "fleet_name": self.fleet_name,
            "fleet_vehicle": self.fleet_vehicle
        }
        return fleet_dictionary

####################### testing methods ####################################
#new_fleet = FleetManager("prison", "bus")

#print(new_fleet.get_fleet_name(),new_fleet.get_fleet_vehicle())
#############################################################################
