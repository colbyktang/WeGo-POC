import unittest
from supply_dispatch import Dispatch

class dispatch_test_case(unittest.TestCase):
    # Expecting vehicle object to be instantiated
    def test_dispatch_instantiation(self):
        print ("Test Dispatch Object")
        
        dispatch = Dispatch("start", ["stop1", "stop2"], "order_id", "vehicle_id")
        print (dispatch.dictionary)
        actual = (dispatch != None)
        expected = True
        self.assertEqual(expected, actual)

    def test_dispatch_attributes(self):
        print ("Test Dispatch Object")
        
        dispatch = Dispatch("start", ["stop1", "stop2"], "order_id", "vehicle_id")
        print (dispatch.dictionary)
        actual = (dispatch != None)
        expected = True
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
