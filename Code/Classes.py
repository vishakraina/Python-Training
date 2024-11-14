# Topic 53 - Classes

# Creating a Class

class Patient:
    # Initialization method to define initial attributes
    def __init__(self, name, age, medical_condition):
        self.name = name
        self.age = age
        self.medical_condition = medical_condition

    # Method to display patient's information
    def display_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Medical Condition: {self.medical_condition}")

# Creating an Instance of the Class

# Creating an instance of Patient
patient1 = Patient("Alice Smith", 29, "Hypertension")

# Using a method on the instance
patient1.display_info()
