import json
from supply_database_utils import Supply_Database_Utils
from supply_vehicle import Vehicle

def register_vehicle(self):
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
    dictionary = json.loads(body)

    # Grab the username and password from the dictionary and check them
    is_available = dictionary["is_available"]
    vin = dictionary["vin"]
    vehicle_name = dictionary["vehicle_name"]
    vehicle_type = dictionary["vehicle_type"]
    vehicle_color = dictionary["vehicle_color"]

    # Creating database utils object to interact with the database
    database_utils = Supply_Database_Utils()

    vehicle_object = Vehicle(vin, vehicle_name, vehicle_type, vehicle_color, is_available)
    insert_result = database_utils.insert_vehicle(vehicle_object)

    if insert_result != None:
        response = "Vehicle " + vehicle_name + " entered into database!"
        print (response)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
    else:
        response = "Vehicle " + vehicle_name + " already exists in the database!"
        print (response)
        self.send_response(403)
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))