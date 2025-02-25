import json
import requests

from demand_order import Order
from demand_order import Order_Status

from demand_database_utils import Demand_Database_Utils

def send_order (self):
    #Displaying the headers of the paht being sent in
    print('Headers:"', self.headers, '"')

    #Displaying the type of the content of the request
    print('Content-Type:', self.headers['content-type'])

    #Displaying the body of the POST request:

    #Collecting the length of the body read the characters
    #that are contained in the body.
    length = int(self.headers['content-length'])
    body = self.rfile.read(length)

    # converting the body into a dictionary
    dictionary = json.loads(body)
    username = str(dictionary["username"])
    pickup_address = str(dictionary["pickup_address"])
    dropoff_address = str(dictionary["dropoff_address"])
    vehicle_type = str(dictionary["vehicle_type"])
    timestamp = str(dictionary["timestamp"])

    # Creating order object to store the dictionary received from the front-end
    new_order = Order(username, pickup_address, dropoff_address, vehicle_type, timestamp)

    # Creating database utils object to interact with the database
    database_utils = Demand_Database_Utils()

    # Insert order into database
    response_order = database_utils.insert_order(new_order)
    did_order_insert_succeed = response_order.acknowledged
    if (did_order_insert_succeed):
        print ("Order inserted into the database!")
        # if insertion is successful, take the order id and insert it into the object
        new_order.id = str(response_order.inserted_id)
        outgoing_dictionary = new_order.dictionary

        # since order.dictionary does not include order_id for database reasons,
        # we update the dictionary with order_id to send to the supply side
        outgoing_dictionary.update({'order_id': new_order.id})

        # send a POST request to supply server for a vehicle
        url = 'https://supply.team12.softwareengineeringii.com/api/cs/requestvehicle'
        request = requests.post(url, data=json.dumps(outgoing_dictionary))
        status_code = request.status_code
        print ("POST Response TEXT: " + request.text)
        print ("STATUS CODE: " + str(status_code))

        # If the POST came back successfully, update the order object, 
        # then pass the json object to the front-end.
        # Otherwise, pass an error response.
        if status_code == 200:
            # update order object in the database with vehicle vin, eta, and order status
            incoming_supply_dictionary = json.loads(request.content)
            vehicle_vin = str(incoming_supply_dictionary["vehicle_vin"])
            vehicle_eta = str(incoming_supply_dictionary["eta"])
            new_order.update_order_with_vehicle (vehicle_eta, vehicle_vin, Order_Status.IN_PROGRESS)
            response_order = database_utils.update_order(new_order)

            print ("Updated order in database")
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')

            #Signify that you are done sending the headers:
            self.end_headers()
            self.wfile.write(request.content)
        else:
            self.send_response(status_code)
            self.end_headers()

            # Error has occurred, cancel order
            new_order.cancel_order()
            response_order = database_utils.update_order(new_order)
            res = 'RECEIVED ERROR CODE FROM SUPPLY: ' + status_code + ', CANCELING ORDER!'
            bytesStr = res.encode('utf-8')
            self.wfile.write(bytesStr)
    else:
        self.send_response(403)
        self.end_headers()

        # Error has occurred, cancel order
        new_order.cancel_order()
        res = 'RECEIVED ERROR CODE FROM TRYING TO INSERT ORDER INTO DATABASE: ' + 403 + ', CANCELING ORDER!'
        bytesStr = res.encode('utf-8')
        self.wfile.write(bytesStr)