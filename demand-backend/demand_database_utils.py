# Team 12
# Written by Will
# Changed by Colby Tang

import pymongo 
from pymongo import MongoClient
from bson.objectid import ObjectId

class Demand_Database_Utils:

    def __init__(self, uri="mongodb://team12:password@localhost:6012/admin"): 
        # Making a connection to a database with MongoClient from pymongo
        self.uri = uri
        self.client = MongoClient(uri)
        self.client.close()
        self.db = self.client.demanddb

    # Open a connection with the database
    def open_database(self):
        self.client = MongoClient(self.uri)

    # Close the connection to the database
    def close_database(self):
        self.client.close()

    # Retrieving a collection called users in the database
    def get_users_collection(self):
        return self.db.users

    # Retrieving a collection called orders in the database
    def get_orders_collection(self):
        return self.db.orders

    # Upload user dictionary to mongodb
    def register_user(self, user_dictionary):
        self.open_database()
        collection = self.get_users_collection()

        # Check if username is already in the database, if so return None, otherwise return the insert result
        doesUsernameAlreadyExist = self.is_username_in_db(user_dictionary['username'])
        if doesUsernameAlreadyExist:
            retValue = None
        else:
            retValue = collection.insert_one(user_dictionary)

        self.close_database()
        return retValue

    # take the order object and insert its dictionary into the database
    def insert_order(self, order_object):
        self.open_database()
        order_dictionary = order_object.dictionary
        order_collection = self.get_orders_collection()
        order_insert = order_collection.insert_one(order_dictionary)
        self.close_database()
        return order_insert

    # find the order using order id and update it with the new order object
    def update_order (self, order_object):
        self.open_database()
        order_dictionary = order_object.dictionary
        order_collection = self.get_orders_collection()

        order_id = order_object.id

        query = {"_id": ObjectId(order_id)}
        new_values = {"$set": {
            "username": order_dictionary["username"],
            "pickup_address": order_dictionary["pickup_address"],
            "dropoff_address": order_dictionary["dropoff_address"],
            "vehicle_type": order_dictionary["vehicle_type"],
            "vehicle_eta": order_dictionary["vehicle_eta"], 
            "vehicle_vin": order_dictionary["vehicle_vin"], 
            "order_status": order_dictionary["order_status"],
            "timestamp": order_dictionary["timestamp"]
            }
        }

        # Change the order in the db
        order_update = order_collection.update_one(query, new_values)

        self.close_database()
        return order_update

    # Is username in database? If so return true, else false
    def is_username_in_db(self, username):
        self.open_database()
        users_collection = self.get_users_collection()

        find_one_result = users_collection.find_one({'username': username}, {'username': 1})

        self.close_database()

        if find_one_result != None:
            return True
        else:
            return False

    # Does the username and password pair match in the database?
    def does_credentials_exist(self, username, password):
        self.open_database()
        users_collection = self.get_users_collection()

        find_one_result = users_collection.find_one({'username': username, 'password': password}, {'password': 1})

        self.close_database()
        if find_one_result != None:
            return True
        else:
            return False
    
    # Returns all information of user
    # May need to surpress password later for security purposes
    def get_user_from_username(self, username):
        self.open_database()
        users_collection = self.get_users_collection()

        entry = users_collection.find_one({'username': username})
        entry['_id'] = str(entry['_id'])

        self.close_database()
        return entry

    # Returns the first and last name of the username
    def get_names_from_username(self, username):
        self.open_database()
        users_collection = self.get_users_collection()

        entry = users_collection.find_one({'username': username}, {'_id': 0, 'first_name': 1, 'last_name':1})

        self.close_database()
        return entry