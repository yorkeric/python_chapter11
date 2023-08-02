# The Employee class holds general data about an employee

class Employee:
    
    # Initalize object with the attributes name and number
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
    
    # Set the name attribute
    def set_name(self, name):
        self.__name = name
    
    # Set the number attribute
    def set_number(self, number):
        self.__number = number
    
    # Get the name attribute
    def get_name(self):
        return self.__name
    
    # Get the number attribute
    def get_number(self):
        return self.__number
    
# The ProducerWorker class holds specific information about the role
class ProducerWorker:
    
    # Initalize object with the attributes name, number, shift number, and hourly pay rate
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        # Initalize the superclass with the name and number
        Employee.__init__(self, name, number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate
        
    # Set the shift number attribute
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    
    # Set the hourly pay rate attribute
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate
        
    # Get the shift number attribute
    def get_shift_number(self):
        return self.__shift_number
    
    # Get the hourly pay rate attribute
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate