from supply_vehicle_generator import Vehicle_Generator
import supply_vehicle
from supply_vehicle import Vehicle_Type
from supply_vehicle import Vehicle_Color

print ("Creating vehicle generator")
generator = Vehicle_Generator()

print ("Creating vehicle")
test_vehicle = generator.generate_vehicle()

print ("Setting vehicle type")
test_vehicle.vehicle_type = "Bus"

print ("Setting vehicle color")
test_vehicle.vehicle_color = "White"

print ("Getting vehicle dictionary")
print (test_vehicle.dictionary)


print ("Setting vehicle type 2 ")
test_vehicle.vehicle_type = 1

print ("Setting vehicle color 2 ")
test_vehicle.vehicle_color = 1

print ("Getting vehicle dictionary")
print (test_vehicle.dictionary)

print ("Setting vehicle type 3 ")
test_vehicle.vehicle_type = Vehicle_Type.VAN

print ("Setting vehicle color 3 ")
test_vehicle.vehicle_color = Vehicle_Color.CAMO

print ("Getting vehicle dictionary")
print (test_vehicle.dictionary)

print ("Setting vehicle type 4 ")
#test_vehicle.vehicle_type = True

print ("Setting vehicle color 4 ")
#test_vehicle.vehicle_color = False

print ("Getting vehicle dictionary")
print (test_vehicle.dictionary)

##for i in range (10):
##    test_vehicle = generator.generate_vehicle()
##    print (test_vehicle.get_dictionary())


#new_vehicle = supply_vehicle.Vehicle("13rqwefasdfqefrqw", "Honda", "bus", "gray", True)
#print(new_vehicle.get_dictionary())
