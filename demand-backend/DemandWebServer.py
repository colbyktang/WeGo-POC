# Web server to run the backend!
# Team 12
# Made by Will Luong, Colby Tang

import http.server
from http.server import BaseHTTPRequestHandler

import json
import requests
import urllib.parse

#from demand_order import Order
#from demand_order import Order_Status
from demand_api_order import send_order
from demand_api_login import demand_login
from demand_api_register import demand_register
from demand_database_utils import Demand_Database_Utils

class DemandHTTPRequestHandler(BaseHTTPRequestHandler):

    # function to handle POST request to a server
    # a POST request got sent in as a parameter
    def do_POST(self):

        # get the path of the request that was sent in
        path = self.path[1:]
        print ("Path: " + path)


        # Handling a registration request from POST
        if path == "api/cs/register":
            demand_register(self)

        # Handling a login request from POST
        elif path == "api/cs/login":
            demand_login(self)
            
        # call to send a request for a vehicle
        # json object being passed in with the following keys:
        #   username, pickup_address, dropoff_address, vehicle_type, timestamp  
        elif path == "api/cs/order":
            send_order(self)

        #Connection error:
        else:
            # If the path did not match any known request
            # a 404 Not Found error is thrown.
            print ("api/cs failed")
            self.send_response(404)
            self.end_headers()
            res = 'Path did not match any known request! Code 404! Path: ' + path
            bytesStr = res.encode('utf-8')
            self.wfile.write(bytesStr)

    #function to deal with a GET request:
    def do_GET(self):
        print ("GET REQUEST")
        print ("GET self.path: " + self.path)
        split_path = self.path.split('?', 1)
        if 'api/cs' in split_path[0]:
            # Creating database utils object to interact with the database
            database_utils = Demand_Database_Utils()

            params = urllib.parse.parse_qs(split_path[1])

            # for debugging purpose:
            # use pymongo to retrieve user and vehicle from the database
            print("Params: " + str(params))
            if "user" in params:
                username = params['user'][0]
                if "get" in params:
                    if params['get'][0] == "name":
                        response = database_utils.get_names_from_username(username)
                else:
                    response = database_utils.get_user_from_username(username)
                print(response)
                print("GET Response: " + str(response))

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode(encoding='utf_8'))
                
            elif "status" in params:
                self.send_response(200)
                self.end_headers()
                response = "Demand Web Server running! (200)"
                bytesStr = response.encode('utf-8')
                self.wfile.write(bytesStr)
            else:
                self.send_response(403)
                self.end_headers()
                message = "403, could not find any params"
                bytesStr = message.encode('utf-8')
                self.wfile.write(bytesStr)

        else:
            #Send a 404 Error handling if the route does not exist
            self.send_response(404)
            self.end_headers()

            message = "Route does not exist"
            bytesStr = str(message).encode('utf-8')
            self.wfile.write(bytesStr)

# Execute the web server:
def main():
    #Server port
    port = 4112

    # Create http server
    httpServer = http.server.HTTPServer (('', port), DemandHTTPRequestHandler)
    print("Demand running on port", port)

    # Start server, use CTRL+C to close it.
    try:
        httpServer.serve_forever()
    except KeyboardInterrupt:
        httpServer.server_close()
        print ("Demand server closed!")

if __name__ == "__main__":
    main()
