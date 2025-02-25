import json
from supply_database_utils import Supply_Database_Utils

def remove_vehicle(self):
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

    # Creating database utils object to interact with the database
    database_utils = Supply_Database_Utils()

    # Grab the username and password from the dictionary and check them
    vin = dictionary["vin"]

    delete_result = database_utils.delete_vehicle_using_vin (vin)
    if delete_result != None and delete_result.acknowledged:
        self.send_response(200)
        response = "Vehicle " + vin + " deleted"
    else:
        self.send_response(404)
        response = "Could not delete vehicle: " + vin
    print (response)
    self.end_headers()
    self.wfile.write(response.encode('utf-8'))