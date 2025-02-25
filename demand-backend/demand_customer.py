class Customer:

    def __init__ (self, username, password, first_name, last_name, email, country, phone_number):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country
        self.phone_number = phone_number

    # getter method for customer username
    def get_username(self):
        return self.username

    # getter method for customer password
    def get_password(self):
        return self.password

    # getter method for customer first name
    def get_first_name(self):
        return self.first_name

    # getter method for customer last name
    def get_last_name(self):
        return self.last_name

    # getter method for customer email
    def get_email(self):
        return self.email

    # getter method for customer country
    def get_country(self):
        return self.country

    # getter method for customer phone number
    def get_phone_number(self):
        return self.phone_number

    # getter method for all values of fleet manager
    def get_dictionary(self):
        customer_dictionary = {
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "country": self.country,
            "phone_number": self.phone_number
        }
        return customer_dictionary

####################### testing methods ####################################
#new_customer = Customer("jquade", "admin", "Jeff", "Quade", "jquade@stedwards.edu", "USA", "5127364724")

#print(new_customer.get_username(), new_customer.get_password(), new_customer.get_first_name(), new_customer.get_last_name(), new_customer.get_email(), new_customer.get_country(), new_customer.get_phone_number())
#############################################################################
