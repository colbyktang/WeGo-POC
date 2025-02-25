import unittest
from supply_vehicle import Vehicle
from vin_generator import VIN
from supply_vehicle_generator import Vehicle_Generator

# Use for expected failures
#@unittest.expectedFailure

# Instantiate a VIN generator
vin = VIN()

class vehicle_test_case(unittest.TestCase):

    # Expecting vehicle object to be instantiated
    def test_vehicle_instantiation(self):
        print ("Test Vehicle Instantiation")
        vehicle = Vehicle(vin.get_vin(), "Honda", "Truck", "Red", True)
        #print (vehicle.dictionary)
        actual = (vehicle != None)
        expected = True
        self.assertEqual(expected, actual)

    # Expecting vehicle generator to generate a vehicle
    def test_vehicle_generator(self):
        print ("Test Vehicle Generator")
        generator = Vehicle_Generator()
        test_vehicle = generator.generate_vehicle()
        actual = (test_vehicle != None)
        expected = True
        self.assertEqual(expected, actual)

    # Expecting vehicle type to be bus
    def test_vehicle_type(self):
        print ("Test Vehicle Type")
        vehicle = Vehicle(vin.get_vin(), "Honda", "Truck", "Red", True)
        vehicle.vehicle_type = "Bus"
        actual = vehicle.vehicle_type
        expected = "BUS"
        self.assertEqual(expected, actual)

    # Expecting vehicle color to be White
    def test_vehicle_color(self):
        print ("Test Vehicle Color")
        vehicle = Vehicle(vin.get_vin(), "Honda", "Truck", "Red", True)
        vehicle.vehicle_color = "White"
        actual = vehicle.vehicle_color
        expected = "WHITE"
        self.assertEqual(expected, actual)

    # Expecting vehicle color to throw an exception
    @unittest.expectedFailure    
    def test_vehicle_color_fail(self):
        print ("Test Vehicle Color Fail")
        vehicle = Vehicle(vin.get_vin(), "Honda", "Truck", "Red", True)
        vehicle.vehicle_color = 3
        actual = vehicle.vehicle_color
        expected = "WHITE"
        self.assertEqual(expected, actual)

    # Expecting vehicle position to store an array of two floats
    def test_vehicle_position(self):
        print ("Test Vehicle Position")
        vehicle = Vehicle(vin.get_vin(), "Honda", "Truck", "Red", True)
        vehicle.vehicle_position = [-70.00, -39.00]
        actual = vehicle.vehicle_position
        expected = [-70.00, -39.00]
        self.assertEqual(expected, actual)

    # Expecting a failure by passing wrong data type to vehicle position
    @unittest.expectedFailure
    def test_vehicle_position_fail(self):
        print ("Test Vehicle Position Fail")
        vehicle = Vehicle(vin.get_vin(), "Honda", "Truck", "Red", True)
        vehicle.vehicle_position = True
        actual = vehicle.vehicle_position
        expected = [-70.00, -39.00]
        self.assertEqual(expected, actual)

    # Expecting dictionary to successfully return a dictionary
    def test_dictionary(self):
        print ("Test Dictionary")
        vin_num = vin.get_vin()
        vehicle = Vehicle(vin_num, "Honda", "Truck", "Red", True)
        actual = vehicle.dictionary
        expected = {'vin': vin_num, 'vehicle_name': 'Honda', 'vehicle_type': 'TRUCK', 'vehicle_color': 'RED', 'is_available': True, 'vehicle_position': [0.0,0.0], 'vehicle_status': 'OK'}
        self.assertEqual(expected, actual)

        
if __name__ == '__main__':
    unittest.main()
