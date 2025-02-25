import json

from demand_database_utils import Demand_Database_Utils

def demand_register(self):
    # Displaying the headers of the path being sent in

    print('Headers:"', self.headers, '"')

    #Displaying the type of the content of the request
    print('Content-Type:', self.headers['content-type'])

    #Displaying the body of the POST request:

    #Collecting the length of the body read the characters
    #that are contained in the body.
    length = int(self.headers['content-length'])
    body = self.rfile.read(length)

    #Printing out the body of the request for debugging purposes
    #The body would be in bytes
    print('Body:', body)

    #Converting bytes to string using .decode()
    print("Body (String): ", body.decode())

    #converting the body into a dictionary
    dictionary = json.loads(body)

    # Creating database utils object to interact with the database
    database_utils = Demand_Database_Utils()

    # insert dictionary into db
    result = database_utils.register_user(dictionary)

    # if the insertion was successful return 200
    if result != None:
        print ("User " + dictionary['username'] + " entered into database!")
        self.send_response(200)
        self.end_headers()
        res = '200'
        bytesStr = res.encode('utf-8')
        self.wfile.write(bytesStr)

    # if user already exists return 403
    else:
        print ("User " + dictionary['username'] + " already exists in the database!")
        self.send_response(403)
        self.end_headers()
        res = 'Username already exists! Code 403'
        bytesStr = res.encode('utf-8')
        self.wfile.write(bytesStr)