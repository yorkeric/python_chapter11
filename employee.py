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
    
# The ProductionWorker class holds specific information about the role
class ProductionWorker(Employee):
    
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
    
class ShiftSupervisor(Employee):
        
    # Initalize object with the attributes name, number, annual salary, and annual production bonus
    def __init__(self, name, number, annual_salary, annual_production_bonus):
        # Initalize the superclass with the name and number            
        Employee.__init__(self, name, number)
        self.__annual_salary = annual_salary
        self.__annual_production_bonus = annual_production_bonus
        
    # Set the annual salary attribute
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary
        
    # Set the annual production bonus attribute
    def set_annual_production_bonus(self, annual_production_bonus):
        self.__annual_production_bonus = annual_production_bonus
        
    # Get the annual salary attribute
    def get_annual_salary(self):
        return self.__annual_salary

    # Get the annual production bonus attribute
    def get_annual_production_bonus(self):
        return self.__annual_production_bonus
        
    # String method to print the labels and attributes
    def __str__(self):
        return "Name: " + super().get_name() + "\nNumber: " + super().get_number() + "\nAnnual Salary: $" + self.__annual_salary + "\nAnnual Production Bonus: $" + self.__annual_production_bonus        
        