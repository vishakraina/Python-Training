# Topic 60 - Classes: Coding a Method

# Define a Method Inside a Class

class Patient:  
    def __init__(self, last_name, first_name, age):  
        self.last_name = last_name  
        self.first_name = first_name  
        self.age = age  

    # Method to check if patient is a minor  
    def say_if_minor(self):  
        if self.age < 21:  
            print(self.first_name + " " + self.last_name + " is a minor")  

# Call a Method on an Instance

pid4343 = Patient("Taleb", "Sue", 61)  
pid4343.say_if_minor()  # Output: No output, as Sue is not a minor  

pid1234 = Patient("Doe", "John", 19)  
pid1234.say_if_minor()  # Output: "John Doe is a minor"  
