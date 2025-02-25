# Web server to run the backend!
# Team 12
# Made by Will Luong, Colby Tang, Erik Hernandez, Jeffrey Quade

import http.server
from http.server import BaseHTTPRequestHandler
import json
import requests
import urllib.parse
from supply_vehicle import Vehicle

from supply_database_utils import Supply_Database_Utils
from supply_api_generate_vehicle import generate_vehicle
from supply_api_request_vehicle import request_vehicle
from supply_api_login import login
from supply_api_register_vehicle import register_vehicle
from supply_api_remove_vehicle import remove_vehicle
from supply_api_heartbeat import request_beat

class SupplyHTTPRequestHandler(BaseHTTPRequestHandler):

    # function to handle POST request to a server
    # a POST request got sent in as a parameter
    def do_POST(self):

        # get the path of the request that was sent in
        path = self.path

        # Handling a request vehicle request from POST
        if path == "/api/cs/requestvehicle":
            request_vehicle(self)

        # Handling a generate vehicle request from POST
        elif path == "/api/cs/generatevehicle":
            generate_vehicle(self)

        # Handling a login request from POST
        elif path == "/api/cs/login":
            login(self)

        # Register new vehicle, check if vehicle already exists in database
        elif path == "/api/cs/registervehicle":
            register_vehicle(self)

        # Register new vehicle, check if vehicle already exists in database
        elif path == "/api/cs/removevehicle":
            remove_vehicle(self)

        elif path == "/api/cs/requestbeat":
            request_beat(self)

        

        # Connection error:
        else:
            # If the path did not match any known request
            # a 404 Not Found error is thrown.
            print ("api/cs failed")
            self.send_response(404)
            self.end_headers()
            res = 'Path did not match any known request! Code 404'
            bytesStr = res.encode('utf-8')
            self.wfile.write(bytesStr)

    # function to deal with a GET request:
    def do_GET(self):
        print ("GET REQUEST")
        print ("GET self.path: " + self.path)
        split_path = self.path.split('?', 1)
        if 'api/cs' in split_path[0]:
            # Creating database utils object to interact with the database
            database_utils = Supply_Database_Utils()

            params = urllib.parse.parse_qs(split_path[1])

            # for debugging purpose:
            # use pymongo to retrieve user and vehicle from the database
            print(params)
            if "fm" in params:
                param = params['fm'][0]
                response = database_utils.get_fm_from_username(param)
                print("FM: " + str(response))
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode(encoding='utf_8'))

            elif "vehicle" in params:
                name = params['vehicle'][0]
                if "get" in params:
                    if params['get'][0] == "all":
                        response = database_utils.get_all_vehicles()
                    else:
                        response = database_utils.get_vehicle_from_name(name)
                else:
                    response = database_utils.get_vehicle_from_name(name)

                print("Vehicle: " + str(response))
                if response != None:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode(encoding='utf_8'))
                else:
                    self.send_response(403)
                    self.end_headers()
                    message = "403, could not find any params"
                    bytesStr = message.encode('utf-8')
                    self.wfile.write(bytesStr)

            elif "vehicletype" in params:
                vehicle_type = params['vehicletype'][0]
                if "get" in params:
                    if params['get'][0] == "available":
                        response = database_utils.get_available_vehicle_from_type(vehicle_type)
                    else:
                        response = database_utils.get_vehicle_from_type(vehicle_type)
                else:
                    response = database_utils.get_vehicle_from_type(vehicle_type)
                print("Vehicle: " + str(response))
                if response != None:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(response).encode(encoding='utf_8'))
                else:
                    self.send_response(403)
                    self.end_headers()
                    message = "403, could not find any params"
                    bytesStr = message.encode('utf-8')
                    self.wfile.write(bytesStr)

            # Check quickly if server is running
            elif "status" in params:
                self.send_response(200)
                self.end_headers()
                response = "Supply Web Server running! (200)"
                bytesStr = response.encode('utf-8')
                self.wfile.write(bytesStr)
            else:
                self.send_response(403)
                self.end_headers()
                message = "403, could not find any params"
                bytesStr = message.encode('utf-8')
                self.wfile.write(bytesStr)
        else:
            # Send a 404 Error handling if the route does not exist
            self.send_response(404)
            self.end_headers()

            message = "Route does not exist"
            bytesStr = str(message).encode('utf-8')
            self.wfile.write(bytesStr)

# Execute the web server:
def main():
    # Server port
    port = 4112

    # Create server
    httpServer = http.server.HTTPServer(('', port), SupplyHTTPRequestHandler)
    print("Supply running on port", port)

    # Start server, use CTRL+C to close it.
    try:
        httpServer.serve_forever()
    except KeyboardInterrupt:
        httpServer.server_close()
        print ("Supply server close")


if __name__ == "__main__":
    main()
