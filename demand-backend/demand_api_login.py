import json

from demand_order import Order
from demand_order import Order_Status
from demand_database_utils import Demand_Database_Utils

def demand_login(self):
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

    # Grab the username and password from the dictionary and check them
    username = dictionary["username"]
    password = dictionary["password"]

    # Creating database utils object to interact with the database
    database_utils = Demand_Database_Utils()

    doCredentialsMatch = database_utils.does_credentials_exist(username, password)
    print("doCredentialsMatch: ", doCredentialsMatch)

    response = ''

    #if username and password pair is found:
    if doCredentialsMatch:
        names_dictionary = database_utils.get_names_from_username(username)
        json_object = json.dumps(names_dictionary)

        #Request status check
        #If the status of the request was fine and went well, send a 200
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')

        #Signify that you are done sending the headers:
        self.end_headers()

        #Formatting the JSON in a string form:
        response = 'Found credentials! Code 200'
        #converting a the response string to bytes because the body only recieves
        # bytes.
        self.wfile.write(json_object.encode(encoding='utf_8'))

    #if an error occurs
    else:
        self.send_response(403)
        self.end_headers()
        response = '403: Credentials were not found!'
        bytesStr = response.encode('utf-8')
        self.wfile.write(bytesStr)