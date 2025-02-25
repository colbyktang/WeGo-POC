# Team 12
# Written by Will
# Changed by Colby Tang, Erik Hernandez

import pymongo 
from pymongo import MongoClient
from bson.objectid import ObjectId

class Supply_Database_Utils:
    # Making a connection to a database with MongoClient from pymongo
    def __init__(self, uri="mongodb://team12:password@localhost:6012/admin"): 
        self.uri = uri
        self.client = MongoClient(uri)
        self.client.close()
        self.db = self.client.supplydb

    # Open a connection with the database
    def open_database(self):
        self.client = MongoClient(self.uri)

    # Close the connection to the database
    def close_database(self):
        self.client.close()

    # Retrieving a collection called fm in the database
    def get_fm_collection(self):
        return self.db.fm

    # Retrieving a collection called vehicles in the database
    def get_vehicles_collection(self):
        return self.db.vehicles
   
    # Retrieving a collection called dispatches in the database
    def get_dispatches_collection(self):
        return self.db.dispatches

    # Is vehicle in database? Use vin to match
    def does_vin_exist(self, vehicle_vin):
        self.open_database()
        collection = self.get_vehicles_collection()

        find_one_result = collection.find_one({'vin': vehicle_vin}, {'vin': 1})

        self.close_database()
        if find_one_result != None:
            return True
        else:
            return False

    # Is username in database?
    def does_username_exist(self, username):
        self.open_database()
        collection = self.get_fm_collection()

        find_one_result = collection.find_one({'username': username}, {'username': 1})

        self.close_database()
        if find_one_result != None:
            return True
        else:
            return False

    # Does the username and password pair match in the database?
    def does_credentials_exist(self, username, password):
        self.open_database()
        collection = self.get_fm_collection()

        find_one_result = collection.find_one({'username': username, 'password': password}, {'password': 1})

        self.close_database()
        if find_one_result != None:
            return True
        else:
            return False

    # insert vehicle into database
    def insert_vehicle(self, vehicle):
        self.open_database()
        collection = self.get_vehicles_collection()
        vehicle_dictionary = vehicle.dictionary

        is_matching = self.does_vin_exist (vehicle_dictionary['vin'])
        if is_matching:
            insert_one_result = None
        else:
            insert_one_result = collection.insert_one(vehicle_dictionary)

        self.close_database()
        return insert_one_result

    # insert vehicle into database
    def delete_vehicle_using_vin(self, vin):
        self.open_database()
        collection = self.get_vehicles_collection()

        if self.does_vin_exist (vin):
            result = collection.delete_one({"vin": vin})
        else:
            result = None

        self.close_database()
        return result
    
    # checks if vehicle has a dispatch assigned to it
    # returns a find_one object, None if none found
    def get_vehicle_dispatch(self, vid):
        self.open_database()
        collection = self.get_dispatches_collection()
        
        entry = collection.find_one({'vehicle_id': vid})
        self.close_database()
        return entry

    # insert fm into database
    def insert_fm(self, fm):
        self.open_database()
        collection = self.get_fm_collection()
        fm_dictionary = fm.get_dictionary()

        insert_one_result = collection.insert_one(fm_dictionary)

        self.close_database()
        return insert_one_result

    # insert dispatch into database
    def insert_dispatch(self, dispatch):
        self.open_database()
        collection = self.get_dispatches_collection()
        dispatch_dictionary = dispatch.dictionary
        insert_one_result = collection.insert_one(dispatch_dictionary)

        # if insertion is successful, take the dispatch id and insert it into the object
        if insert_one_result.acknowledged:
            dispatch.id = str(insert_one_result.inserted_id)

        self.close_database()
        return insert_one_result

    def update_dispatch(self, dispatch):
        self.open_database()
        dispatch_dictionary = dispatch.dictionary
        collection = self.get_dispatches_collection()

        dispatch_id = dispatch.id

        query = {"_id": ObjectId(dispatch_id)}
        new_values = { "$set": 
            {
            "vehicle_id": dispatch_dictionary["vehicle_id"], 
            "end_timestamp": dispatch_dictionary["end_timestamp"], 
            "route": dispatch_dictionary["route"],
            "dispatch_status": dispatch_dictionary["dispatch_status"]
            }
        }
        dispatch_update = collection.update_one(query, new_values)

        self.close_database()
        return dispatch_update

    # retrieve dispatch from database
    def get_dispatch_from_id(self, id):
        self.open_database()
        collection = self.get_dispatches_collection()

        entry = collection.find_one({'_id': id})

        self.close_database()
        return entry

    # Returns all information of user
    # May need to suppress password later for security purposes
    def get_fm_from_username(self, username):
        self.open_database()
        collection = self.get_fm_collection()

        entry = collection.find_one({'username': username})
        entry['_id'] = str(entry['_id'])

        self.close_database()
        return entry

    # Returns the first and last name of the username
    def get_names_from_username(self, username):
        self.open_database()
        collection = self.get_fm_collection()

        entry = collection.find_one({'username': username}, {'_id': 0, 'first_name': 1, 'last_name':1})

        self.close_database()
        return entry

    # grab all vehicle info from finding the name
    # returns an array of dictionaries or None
    def get_all_vehicles(self):
        self.open_database()
        collection = self.get_vehicles_collection()

        cursor = collection.find()

        self.close_database()
        if cursor != None:
            result = []
            for entry in cursor:
                entry['_id'] = str(entry['_id'])
                result.append(entry)
            return result
        else:
            return None

    # grab all vehicle info from finding the name
    def get_vehicle_from_name(self, name):
        self.open_database()
        collection = self.get_vehicles_collection()

        result = collection.find_one({'vehicle_name':name})

        self.close_database()
        if result != None:
            result['_id'] = str(result['_id'])
            return result
        else:
            return None

    # grab all vehicle info from finding the type
    def get_vehicle_from_type(self, vehicle_type):
        self.open_database()
        collection = self.get_vehicles_collection()

        result = collection.find_one({'vehicle_type':vehicle_type.upper()})

        self.close_database()
        if result != None:
            result['_id'] = str(result['_id'])
            return result
        else:
            return None

    # grab all vehicle info from finding the type and availability
    def get_available_vehicle_from_type(self, vehicle_type):
        self.open_database()
        collection = self.get_vehicles_collection()

        result = collection.find_one({'vehicle_type':vehicle_type.upper(), 'is_available': True})
        self.close_database()
        if result != None:
            result['_id'] = str(result['_id'])
            return result
        else:
            return None
    
    # Take the vehicle object and update its entry in the database
    def update_vehicle(self, vehicle):
        self.open_database()
        vehicle_dictionary = vehicle.dictionary
        collection = self.get_vehicles_collection()

        vehicle_id = vehicle.id

        query = {"_id": ObjectId(vehicle_id)}
        new_values = { "$set": 
            {
            "vin": vehicle_dictionary["vin"],
            "vehicle_name": vehicle_dictionary["vehicle_name"],
            "vehicle_type": vehicle_dictionary["vehicle_type"],
            "vehicle_color": vehicle_dictionary["vehicle_color"],
            "is_available": vehicle_dictionary["is_available"],
            "vehicle_position": vehicle_dictionary["vehicle_position"]
            }
        }
        update = collection.update_one(query, new_values)

        self.close_database()
        return update

    # Take the vehicle id and update its vehicle status and position in the database
    def update_vehicle_status_position(self, vid, status, position):
        self.open_database()
        collection = self.get_vehicles_collection()
        
        query = {"_id": ObjectId(vid)}
        new_values = { "$set": 
            {
            "vehicle_position": position,
            "vehicle_status": status
            }
        }
        update = collection.update_one(query, new_values)

        self.close_database()
        return update