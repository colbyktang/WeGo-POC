class FleetManager:

    def __init__ (self, username, password, first_name, last_name, email, country, phone_number):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country
        self.phone_number = phone_number

    # getter method for fleet manager username
    def get_username(self):
        return self.username

    # getter method for fleet manager password
    def get_password(self):
        return self.password

    # getter method for fleet manager first name
    def get_first_name(self):
        return self.first_name

    # getter method for manager last name
    def get_last_name(self):
        return self.last_name

    # getter method for fleet manager email
    def get_email(self):
        return self.email

    # getter method for fleet manager country
    def get_country(self):
        return self.country

    # getter method for fleet manager phone number
    def get_phone_number(self):
        return self.phone_number

    # getter method for all values of fleet manager
    def get_dictionary(self):
        fleet_manager_dictionary = {
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "country": self.country,
            "phone_number": self.phone_number
        }
        return fleet_manager_dictionary

####################### testing methods ####################################
#new_fleet_manager = FleetManager("jquade", "admin", "Jeff", "Quade", "jquade@stedwards.edu", "USA", "5127364724")

#print(new_fleet_manager.get_username(),new_fleet_manager.get_password(), new_fleet_manager.get_first_name(),new_fleet_manager.get_last_name(),new_fleet_manager.get_email(),new_fleet_manager.get_country(),new_fleet_manager.get_phone_number())
#############################################################################
