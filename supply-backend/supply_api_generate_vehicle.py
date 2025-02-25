import json

from supply_vehicle_generator import Vehicle_Generator
from supply_database_utils import Supply_Database_Utils

def generate_vehicle(self):
    v_generator = Vehicle_Generator()
        # randomly generate a new vehicle
    new_vehicle = v_generator.generate_vehicle()
    vehicle_name = new_vehicle.dictionary["vehicle_name"]

    # Creating database utils object to interact with the database
    database_utils = Supply_Database_Utils()
    insert_result = database_utils.insert_vehicle(new_vehicle)

    # Inserting new generated vehicle in database
    if insert_result != None:
        response = "Vehicle " + vehicle_name + " entered into database!"
        self.send_response(200)
        print (response)
    else:
        response = "Vehicle " + vehicle_name + " already exists in the database!"
        self.send_response(404)
        print (response)

    # convert python dictionary into a JSON object
    json_object = json.dumps(new_vehicle.dictionary)
    self.send_header('Content-Type', 'application/json')

    #Signify that you are done sending the headers:
    self.end_headers()

    #converting a the response string to bytes because the body only recieves
    # bytes.
    self.wfile.write(json_object.encode(encoding='utf_8'))