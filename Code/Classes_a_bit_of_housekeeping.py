# Topic 55 - Classes A Bit of Housekeeping

# Creating the Class with Attribute Assignment

class Patient:  
    # Initialization method to define attributes  
    def __init__(self, last_name):  
        self.last_name = last_name  # Assigns the last_name attribute to each instance  


# Creating an Instance and Accessing Attributes

# Creating an instance of Patient  
patient1 = Patient("Smith")  
print(patient1.last_name)  # Output: Smith  
