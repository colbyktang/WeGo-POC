import unittest
from demand_order import Order
from demand_order import Order_Status

class order_test_case(unittest.TestCase):

#####################################################
## TESTING get_username
#####################################################

# Expecting success username jquade
    def test_order_username_jquade(self):
        print ("Test Order Username jquade")
        order = Order("jquade", "12203 Arrowwood dr. Austin TX", "St. Edwards", "bus", "March 4th 2020, 8:05:43 pm")
        actual = order.username
        expected = "jquade"
        self.assertEqual(expected, actual)

# Expecting failure username empty
    @unittest.expectedFailure
    def test_order_username_empty(self):
        print ("Test Order Username empty")
        order = Order("jquade", "12203 Arrowwood dr. Austin TX", "St. Edwards", "bus", "March 4th 2020, 8:05:43 pm")
        actual = order.username
        expected = ""
        self.assertEqual(expected, actual)

# Expecting failure username ctang
    @unittest.expectedFailure
    def test_order_username_ctang(self):
        print ("Test Order Username ctang")
        order = Order("jquade", "12203 Arrowwood dr. Austin TX", "St. Edwards", "bus", "March 4th 2020, 8:05:43 pm")
        actual = order.username
        expected = "ctang"
        self.assertEqual(expected, actual)

#####################################################
## TESTING get_pickup_address
#####################################################

# Expecting success pickup address 12203 Arrowwood dr. Austin TX
    def test_order_pickup_address_12203(self):
        print ("Test Order Pickup Address 12203 Arrowwood dr. Austin TX")
        order = Order("jquade", "12203 Arrowwood dr. Austin TX", "St. Edwards", "bus", "March 4th 2020, 8:05:43 pm")
        actual = order.pickup_address
        expected = "12203 Arrowwood dr. Austin TX"
        self.assertEqual(expected, actual)

# Expecting failure pickup address empty
    @unittest.expectedFailure
    def test_order_pickup_address_empty(self):
        print ("Test Order Pickup Address Empty")
        order = Order("jquade", "12203 Arrowwood dr. Austin TX", "St. Edwards", "bus", "March 4th 2020, 8:05:43 pm")
        actual = order.pickup_address
        expected = ""
        self.assertEqual(expected, actual)


#####################################################
## TESTING get_dropoff_address
#####################################################

# Expecting success dropoff address St. Edwards
# to be continued...


#####################################################
## TESTING Order Status Enum
#####################################################


# Expecting success order status NOT_COMPLETED
    def test_order_status_0(self):
        print ("Test Order Status NOT_COMPLETED as a integer")
        order = Order("jquade", "12203 Arrowwood dr. Austin TX", "St. Edwards", "bus", "March 4th 2020, 8:05:43 pm")
        order.order_status = 0
        actual = order.order_status
        expected = "NOT_COMPLETED"
        self.assertEqual(expected, actual)

# Expecting success order status NOT_COMPLETED
    def test_order_status_NOT_COMPLETED(self):
        print ("Test Order Status NOT_COMPLETED as an enum")
        order = Order("jquade", "12203 Arrowwood dr. Austin TX", "St. Edwards", "bus", "March 4th 2020, 8:05:43 pm")
        order.order_status = Order_Status.NOT_COMPLETED
        actual = order.order_status
        expected = "NOT_COMPLETED"
        self.assertEqual(expected, actual)

# Expecting failure order status NOT_COMPLETED
# This is an issue
    @unittest.expectedFailure
    def test_order_status_string(self):
        print ("Test Order Status NOT_COMPLETED as a string")
        order = Order("jquade", "12203 Arrowwood dr. Austin TX", "St. Edwards", "bus", "March 4th 2020, 8:05:43 pm")
        order.order_status = "NOT_COMPLETED"
        actual = order.order_status
        expected = "NOT_COMPLETED"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
