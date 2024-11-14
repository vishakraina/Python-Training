# Topic 59 - Classes Adding Methods to Classes

# Defining a Method in a Class

class Patient:  
    def __init__(self, last_name, first_name, age):  
        self.last_name = last_name  
        self.first_name = first_name  
        self.age = age  

    # Method to check if patient is a minor  
    def say_if_minor(self):  
        if self.age < 21:  
            print(self.first_name + " " + self.last_name + " is a minor")  

# Calling a Method on an Instance

pid4343 = Patient("Taleb", "Sue", 61)  
pid4343.say_if_minor()  

# Adding Arguments to Methods

def say_if_minor(self, month, insured=False):  
    if self.age < 21:  
        print(f"{self.first_name} {self.last_name} is a minor as of {month}.")  
        if insured:  
            print("Patient is insured.")  
