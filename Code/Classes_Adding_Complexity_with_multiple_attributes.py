# Topic 57 - Classes Adding Complexity with Multiple Attributes

# Updating the Class with Multiple Attributes

class Patient:  
    def __init__(self, last_name, first_name, age):  
        self.last_name = last_name  
        self.first_name = first_name  
        self.age = age  

# Creating Instances with Multiple Attributes

pid4343 = Patient("Taleb", "Sue", 61)  
pid4344 = Patient("Anand", "Punya", 29)  
pid4345 = Patient("Oppenheimer", "Douglas", 15)  
pid4346 = Patient("Lin", "Lilly", 48)  
pid12902 = Patient("Nilsson", "Rhonda", 33)  
