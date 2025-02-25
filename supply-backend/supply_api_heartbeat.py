import json
from supply_database_utils import Supply_Database_Utils

# Heartbeat request
def request_beat (self):
    # Displaying the headers of the paht being sent in
    #print('Headers:"', self.headers, '"')

    # Displaying the type of the content of the request
    #print('Content-Type:', self.headers['content-type'])

    # Displaying the body of the POST request:

    # Collecting the length of the body read the characters
    # that are contained in the body.
    length = int(self.headers['content-length'])
    body = self.rfile.read(length)

    # converting the body into a dictionary
    dictionary = json.loads(body)
    
    vehicle_id = dictionary["vehicle_id"]    
    vehicle_status = dictionary["vehicle_status"]
    vehicle_position = dictionary["vehicle_position"]
    database_utils = Supply_Database_Utils()
    print ("Heartbeat from vehicle", vehicle_id, vehicle_status, vehicle_position)

    if vehicle_status == "OK":
        database_utils.update_vehicle_status_position(vehicle_id, vehicle_status, vehicle_position)
        self.send_response(200)
        dispatch = database_utils.get_vehicle_dispatch(vehicle_id)
        if dispatch != None:
            self.send_response(200)
            respond_json (self, "DISPATCH", dispatch["route"])
        else:
            respond_json (self, "COOL")
            
    elif vehicle_status == "OTW":
        database_utils.update_vehicle_status_position(vehicle_id, vehicle_status, vehicle_position)
        self.send_response(200)
        respond_json (self, "COOL")

    elif vehicle_status == "DONE":
        database_utils.update_vehicle_status_position(vehicle_id, vehicle_status, vehicle_position)
        self.send_response(200)
        respond_json (self, "COOL")

    elif vehicle_status == "MAINT":
        database_utils.update_vehicle_status_position(vehicle_id, vehicle_status, vehicle_position)
        self.send_response(200)
        respond_json (self, "COOL")
        
    else:
        self.send_response(404)
        respond_json (self, "WHAT?")
    
def respond_json (self, response, route = []):
    python_dictionary = {
        "response": response,
        "route": route
    }
    print ("Response to vehicle: " + str(python_dictionary))
    json_object = json.dumps(python_dictionary)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    self.wfile.write(json_object.encode(encoding='utf_8'))