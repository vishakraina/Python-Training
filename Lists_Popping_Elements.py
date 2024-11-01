# Topic 19 - Lists: Popping Elements

tasks = ["email Frank", "call Sarah", "meet with Zach"]

# Popping an Element by Index and Storing It in a Variable

latest_task_accomplished = tasks.pop(1)  
# Result: tasks = ["email Frank", "meet with Zach"]
# latest_task_accomplished = "call Sarah"

# Syntax of the pop() Method

latest_task_accomplished = tasks.pop(1)

# Transferring a Popped Element to Another List

tasks_accomplished = []
tasks_accomplished.append(tasks.pop(1))  
# Result: tasks = ["email Frank", "meet with Zach"]
# tasks_accomplished = ["call Sarah"]

# Popping an Element and Inserting It into a Specific Position in Another List

tasks_accomplished.insert(1, tasks.pop(1))  
# Result: tasks = ["email Frank", "meet with Zach"]
# tasks_accomplished = [existing elements, "call Sarah"]

#  Popping the Last Element of a List Automatically

latest_task_accomplished = tasks.pop()  
# This pops "meet with Zach" if it’s the last item in the list


# Popping and Storing in a Variable:

latest_task_accomplished = tasks.pop(0)
# Now tasks = ["call Sarah", "meet with Zach"]
# latest_task_accomplished = "email Frank"

# Popping and Appending to Another List:

tasks_accomplished = []
tasks_accomplished.append(tasks.pop(1))
# Result: tasks = ["email Frank", "meet with Zach"]
# tasks_accomplished = ["call Sarah"]

# Popping the Last Item:

last_task = tasks.pop()
# Removes the last task and assigns it to last_task


# Popping and Inserting in Another List:

tasks_accomplished = ["initial task"]
tasks_accomplished.insert(1, tasks.pop(0))
# Moves "email Frank" to tasks_accomplished at position 1

