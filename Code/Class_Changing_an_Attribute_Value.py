# Topic 61 - Classes: Changing an Attribute's Value

# Direct Attribute Update

pid4343.last_name = "Ortega"  


# Using a Method to Change an Attribute

class Patient:  
    def __init__(self, last_name, first_name, age):  
        self.last_name = last_name  
        self.first_name = first_name  
        self.age = age  

    # Method to update the last name  
    def change_last_name(self, new_last_name):  
        self.last_name = new_last_name  

# Call the Method to Change the Last Name

pid4343 = Patient("Taleb", "Sue", 61)  
pid4343.change_last_name("Ortega")  
