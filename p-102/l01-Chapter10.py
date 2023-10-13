#10.2 Instantiate an Object
'''1. Modify the Dog class to include a third instance attribute called coat_color that stores the color of the dog's coat as a string. 
Store your new class in a script and test it out by adding the following code at the bottom of the script:
philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")
The output of your script should be:
Philo's coat is brown.'''
print("10.2 - 1 - - - - - - - -")
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")

'''2. Create a Car class with two instance attributes: .color, which stores the name of the car's color as a string, 
and .mileage, which stores the number of miles on the car as an integer. Then instantiate two Car objects—a blue car with 
20,000 miles, and a red car with 30,000 miles, and print out their colors and mileage. Your output should look like the following:
The blue car has 20,000 miles.
The red car has 30,000 miles.   '''
print("10.2 - 2 - - - - - - - -")
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:3,} miles."
    
    def drive(self, number):
        self.mileage += number

car1 = Car("blue", 20000)
car2 = Car("red", 30000)
print(car1)
print(car2)

'''3. Modify the Car class with an instance method called .drive() that takes a number as an argument and adds that number to the
.mileage attribute. Test that your solution works by instantiating a car with 0 miles, then call .drive(100) and print the .mileage
attribute to check that it is set to 100.   '''
print("10.2 - 3 - - - - - - - -")
car3 = Car("black", 0)
car3.drive(100)
print(car3.mileage)

#10.3 Inherit From Other Classes
'''1. Create a GoldenRetriever class that inherits from the Dog class. Give the sound argument of the GoldenRetriever.speak() 
method a default value of "Bark". Use the following code for your parent Dog class:
class Dog:
species = "Canis familiaris"
def __init__(self, name, age):
    self.name = name
    self.age = age
def __str__(self):
    return f"{self.name} is {self.age} years old"
def speak(self, sound):
    return f"{self.name} says {sound}"  '''
print("10.3 - 1 - - - - - - - -")
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return super().speak(sound)
    
golden = GoldenRetriever("Golden", 1)
print(golden.speak())

'''2. Write a Rectangle class that must be instantiated with two attributed: length and width. Add a .area() method to the class 
that returns the area (length * width) of the rectangle. Then write a Square class that inherits from the Rectangle class and 
that is instantiated with a single attribute called side_length. Test your Square class by instantiating a Square with 
a side_length of 4. Calling the .area() method should return 16.    '''
print("10.3 - 2 - - - - - - - -")
class Rectangle:    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

square = Square(4)
print(square.area())

#10.4 Challenge: Model a Farm
'''In this assignment, you'll create a simplified model of a farm. As you work through this assignment, keep in mind that 
there are a number of correct answers.
The focus of this assignment is less about the Python class syntax and more about software design in general, which is highly subjective.
This assignment is intentionally left open-ended to encourage you to think about how you would organize your code into classes.
Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes, attributes, and methods.
Think about inheritance. How can you prevent code duplication? Take the time to work through as many iterations as you feel are necessary.
The actual requirements are open to interpretation, but try to adhere to these guidelines:
1. You should have at least four classes: the parent Animal class, and then at least three child animal classes that inherit from Animal.
2. Each class should have a few attributes and at least one method that models some behavior appropriate for a specific animal or all
animals—such as walking, running, eating, sleeping, and so on. 
3. Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviors. '''
print("10.4 - Challenge - - - -")
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color  
        #self.legs = legs   
        #            
    def __str__(self):
        return f"This {self.__class__.__name__}'s name is {self.name} and it's {self.color}."
    
    def speak(self, sound):
        return f"{self.name} makes '{sound}' sound."

    def eat(self, food):
        return f"{self.name} favourite food is {food}."
    
    def walking(self, legs):
        return f"{self.name} uses {legs} legs for walking."
    
class Cow(Animal):
    def sound(self, sound="Moooo"):
        return super().speak(sound)

    def eat(self, food="grass"):
        return super().eat(food)
    
    def walking(self, legs=4):
        return super().walking(legs)
    
class Chicken(Animal):
    def sound(self, sound="buk, buk, ba-gawk"):
        return super().speak(sound)

    def eat(self, food="crop"):
        return super().eat(food)
    
    def walking(self, legs=2):
        return super().walking(legs)
    
class Pig(Animal):
    def sound(self, sound="oink, oink"):
        return super().speak(sound)

    def eat(self, food="apple"):
        return super().eat(food)
    
    def walking(self, legs=4):
        return super().walking(legs)
    
cow = Cow("Mućka", "black")
chicken = Chicken("Kurak", "brown")
pig = Pig("Piggy", "pink")
farm_animals = [cow, chicken, pig]

for animal in farm_animals:
    print(animal)
    print(animal.sound())
    print(animal.eat())
    print(animal.walking())
    print()