#  Topic 54 - Classes: Starting to Build the Structure

# Creating a Basic Class Structure

class Patient:  
    # Initialization method to define initial attributes  
    def __init__(self, last_name):  
        self.last_name = last_name  # Assigns the last_name attribute to each instance  

# Creating an Instance of the Class

# Creating an instance of Patient  
patient1 = Patient("Doe")  
print(patient1.last_name)  # Output: Doe  
