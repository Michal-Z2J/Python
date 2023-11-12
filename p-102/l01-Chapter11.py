#11.1. Working With Modules
'''1. Create a module called greeter.py that contains a single function greet(). This function should accept a single string 
parameter name print the text Hello {name}! to the interactive window with {name} replaced with the function argument.'''

'''2. Create a module called main.py that imports the greet() function from greet.py and calls the 
function with the argument "Real Python".'''
print("11.1 - 2 - - - - - - - -")
from greeter import greet
greet("Real Python")

#11.2. Working With Packages
'''1. In a new project folder called package_exercises/, create a package called helpers with three modules: 
__init__.py, string.py, and math.py. In the string.py module, add a function called shout() that takes a single string parameter 
and returns a new string with all of the letters in uppercase. In the math.py module, as a function called area() that takes
two parameters called length and width and returns their product length * width. '''

'''2. In the root project folder, create a module called main.py that imports the shout() and area() functions. Use the shout() 
and area() functions to print the following output: 
THE AREA OF A 5-BY-8 RECTANGLE IS 40    '''
print("11.2 - 2 - - - - - - - -")
from helpers.string import shout
from helpers.math import area

print(shout(f"the area of 5-by-8 rectangle is {area(5, 8)}"))