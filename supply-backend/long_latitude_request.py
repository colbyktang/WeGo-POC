import requests
import math
import json
import urllib.parse

accessToken = "pk.eyJ1Ijoid2lsbGx1b25nOTciLCJhIjoiY2s2bno3OTNvMGRnaTNqcGJzOG9jY2N2ZiJ9.HfvhKBvZreCaO8KFqlYkRw"

def get_address_lat_long(address):
    # parse the address into a url encoded form
    parsed_address = parse_address_into_url (address)
    
    # construct the url with the address and access token
    url = "https://api.mapbox.com/geocoding/v5/mapbox.places/"+ parsed_address + ".json?country=US&access_token=" + accessToken

    # GET Request to Mapbox for the latitude and long
    response = requests.get(url)
    response.close()
    json_object = response.json()
    # Grab the startpoint
    coordinates = json_object['features'][0]['geometry']['coordinates']
    #latitude = coordinate[0]
    #longtitude = coordinate[1]
    #location_ending = {"lat": latitude, "lon": longtitude}

    return coordinates

# return_eta ("3001 S Congress Ave, Austin, TX", "608 Victoria Drive, Cedar Park, Texas")
def return_eta(pickupLocation, dropoffLocation):
    #Extracting the pickup and dropoff long and lat
    pickup_coordinates = get_address_lat_long(pickupLocation)
    dropoff_coordinates = get_address_lat_long(dropoffLocation)
    print("Pickup location: " + str(pickup_coordinates))
    print("Dropoff location: " + str(dropoff_coordinates))
    
    url ='https://api.mapbox.com/directions/v5/mapbox/driving/' + str(pickup_coordinates[0]) + ',' + str(pickup_coordinates[1]) + ';' + str(dropoff_coordinates[0]) + ',' + str(dropoff_coordinates[1]) + '?access_token=' + accessToken

    response = requests.get(url)
    response.close()
    json_object = response.json()
    retETA = json_object["routes"][0]['duration']
    retETAInMinutes = math.ceil(retETA/60)
    retETAJSON = json.dumps({"eta": retETAInMinutes})
    print(str(retETAJSON))
    return retETAJSON

# get an array of coordinates from point A to point B
def get_route (point_a, point_b):
    url = 'https://api.mapbox.com/directions/v5/mapbox/driving/' + str(point_a[0]) + ',' + str(point_a[1]) + ';' + str(point_b[0]) + ',' + str(point_b[1]) + '?steps=true&geometries=geojson&access_token=' + accessToken;
    print (url)
    response = requests.get(url)
    response.close()
    dictionary = response.json()
    coordinates = dictionary["routes"][0]["geometry"]["coordinates"]
    return coordinates

# get an array of coordinates from address A to address B
def get_route_address (address_a, address_b):
    point_a = get_address_lat_long(address_a)
    point_b = get_address_lat_long(address_b)
    return get_route(point_a, point_b)

# turn an address string into a url encoded string for API calls
def parse_address_into_url (address):
    address = address.replace(',', '')
    return urllib.parse.quote(address)