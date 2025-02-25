import json
from supply_vehicle import Vehicle
from supply_dispatch import Dispatch
from long_latitude_request import return_eta
from long_latitude_request import get_route_address

from supply_database_utils import Supply_Database_Utils

def request_vehicle(self):
    # Displaying the headers of the paht being sent in
    print('Headers:"', self.headers, '"')

    # Displaying the type of the content of the request
    print('Content-Type:', self.headers['content-type'])

    # Displaying the body of the POST request:

    # Collecting the length of the body read the characters
    # that are contained in the body.
    length = int(self.headers['content-length'])
    body = self.rfile.read(length)

    # converting the body into a dictionary
    incomingDictionary = json.loads(body)
    print ("Incoming Dictionary: " + str(incomingDictionary))
    
    # Grab strings of the incoming dictionary
    vehicle_type = str(incomingDictionary["vehicle_type"])
    username = str(incomingDictionary["username"])
    timestamp = str(incomingDictionary["timestamp"])
    pickup_address = str(incomingDictionary["pickup_address"])
    dropoff_address = str(incomingDictionary["dropoff_address"])
    order_id = str(incomingDictionary["order_id"])

    # Creating database utils object to interact with the database
    database_utils = Supply_Database_Utils()

    # Retrieve available vehicle from database based on vehicle type
    vehicleDictionary = database_utils.get_available_vehicle_from_type(vehicle_type)
    print ("Vehicle Dictionary: " + str(vehicleDictionary))

    # what if there's no available vehicle yet?
    # dispatch put on hold until an available vehicle is up
    # dispatch queue?
    # when an OK or done heartbeat comes in, give the vehicle a dispatch
    # respond with routes

    # Find an available vehicle of type
    if vehicleDictionary != None:
        # Grab strings of vehicle values
        vehicle_id = str(vehicleDictionary["_id"])
        vehicle_name = str(vehicleDictionary["vehicle_name"])
        vehicle_vin = str(vehicleDictionary["vin"])

        # Retrieve eta from map services based on pickup and dropoff address
        eta = str(json.loads(return_eta(pickup_address,dropoff_address))["eta"])
        
        # get the route coordinates
        route = get_route_address (pickup_address, dropoff_address)

        # create dispatch
        new_dispatch = Dispatch (
            timestamp, 
            [pickup_address, dropoff_address],
            route,
            order_id,
            vehicle_id
        )
        
        # take all the dictionaries and combine them into one
        python_dictionary = {
            "vehicle_id": vehicle_id,
            "vehicle_name": vehicle_name,
            "vehicle_type": vehicle_type,
            "vehicle_vin": vehicle_vin,
            "username": username,
            "timestamp": timestamp,
            "eta": eta,
            "pickup_address": pickup_address,
            "dropoff_address": dropoff_address,
            "route": route,
            "order_id": order_id
        }

        # insert dispatch into database
        insert_dispatch_result = database_utils.insert_dispatch(new_dispatch)

        if insert_dispatch_result.acknowledged:
            new_dispatch.dispatch_id = insert_dispatch_result.inserted_id
            print ("Inserted dispatch into database successfully!")
            print (database_utils.get_dispatch_from_id(insert_dispatch_result.inserted_id))
        else:
            print ("Dispatch could not be inserted database!")

        # convert python dictionary into a JSON object
        json_object = json.dumps(python_dictionary)

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')

        #Signify that you are done sending the headers:
        self.end_headers()

        #converting a the response string to bytes because the body only recieves
        # bytes.
        self.wfile.write(json_object.encode(encoding='utf_8'))

    # No available vehicles found
    else:
        self.send_response(403)
        self.end_headers()
        response = 'Could not find available vehicle, Code 403'

        bytesStr = response.encode('utf-8')
        self.wfile.write(bytesStr)