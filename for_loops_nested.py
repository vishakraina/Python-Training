# Topic 22 - Nested for Loops

# Example Scenario: Generating Rap Star Names

'''
First Names           Last Names
-----------           ----------
BlueRay               Zzz
Upchuck               Burp
Lojack                Dogbone
Gizmo                 Droop
Do-Rag

'''

# Using Nested for Loops

first_names = ["BlueRay", "Upchuck", "Lojack", "Gizmo", "Do-Rag"]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []

for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name + " " + a_last_name)


