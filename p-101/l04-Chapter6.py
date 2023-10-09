# 6.2 Write Your Own Functions
'''1. Write a function called cube() with one number parameter and returns the value of that number raised to the third
power. Test the function by displaying the result of calling your cube() function on a few different numbers.'''
print("6.2 - 1 - - - - - - - -")
def cube(x):
    return x**3
print(cube(1))
print(cube(44))
print(cube(-2.63))
print(cube(-37))


'''2. Write a function called greet() that takes one string parameter called name and displays the text "Hello <name>!",
where <name> is replaced with the value of the name parameter.'''
print("6.2 - 2 - - - - - - - -")
def greet(name):
    print(f"Hello {name}")
greet("Andrzej")

# 6.3 Challenge: Convert Temperatures
'''Write a script called temperature.py that defines two functions:
1. convert_cel_to_far() which takes one float parameter representing degrees Celsius and returns a float
representing the same temperature in degrees Fahrenheit using the following formula:
F = C * 9/5 + 32
2. convert_far_to_cel() which take one float parameter representing degrees Fahrenheit and returns a float
representing the same temperature in degrees Celsius using the following formula:
C = (F - 32) * 5/9
The script should first prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature
converted to Celsius. Then prompt the user to enter a temperature in degrees Celsius and display the temperature
converted to Fahrenheit. All converted temperatures should be rounded to 2 decimal places.
Here's a sample run of the program:
Enter a temperature in degrees F: 72
72 degrees F = 22.22 degrees C
Enter a temperature in degrees C: 37
37 degrees C = 98.60 degrees F'''
print("6.3 - Challenge")
def convert_cel_to_far(celcius):
    fahrenheit = celcius * 9/5 + 32
    print(f"{celcius} degrees C = {fahrenheit:.02f} degrees F")

def convert_far_to_cel(fahrenheit):
    celcius = (fahrenheit -32) * 5/9
    print(f"{fahrenheit} degrees F = {celcius:.02f} degrees C")

user_input = float(input("Enter a temperature in degrees C: "))
convert_cel_to_far(user_input)
user_input = float(input("Enter a temperature in degrees F: "))
convert_far_to_cel(user_input)

# 6.4 Run in Circles
'''1. Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function.'''
print("6.4 - 1 - - - - - - - -")
for i in range(2, 11):
    print(i)

'''2. Use a while loop that prints out the integers 2 through 10 (Hint: You'll need to create a new integer first.)'''
print("6.4 - 2 - - - - - - - -")
new_int = 2
while new_int < 11:
    print(new_int)
    new_int += 1
'''3. Write a function called doubles() that takes one number as its input and doubles that number. Then use the
doubles() function in a loop to double the number 2 three times, displaying each result on a separate line.
Here is some sample output:
4
8
16'''
print("6.4 - 3 - - - - - - - -")
def doubles(num):
    return num * 2
n = 2
for i in range(3):
    n = doubles(n)
    print(n)

# 6.5 Challenge: Track Your Investments
'''In this challenge, you will write a program called invest.py that tracks the growing amount of an investment over time.
An initial deposit, called the principal amount, is made. Each year, the amount increases by a fixed percentage,
called the annual rate of return.
For example, a principal amount of $100 with an annual rate of return of 5% increases the first year by $5. The second
year, the increase is 5% of the new amount $105, which is $5.25. Write a function called invest with three parameters:
the principal amount, the annual rate of return, and the number of years to calculate. The function signature might
look something like this:
def invest(amount, rate, years):
The function then prints out the amount of the investment, rounded to 2 decimal places, at the end of each year for
the specified number of years.
For example, calling invest(100, .05, 4) should print the following:
year 1: $105.00
year 2: $110.25
year 3: $115.76
year 4: $121.55
To finish the program, prompt the user to enter an initial amount, an annual percentage rate, and a number of years.
Then call invest() to display the calculations for the values entered by the user.'''
print("6.5 - Challenge")
def invest(amount, rate, years):
    for year in range(1, years+1):
        amount += amount*rate
        print(f"Year {year}: ${amount:.02f}")

initial_amount = float(input("Please insert initial amount of money to inwest: "))
rate_of_return = float(input("Please insert an annual percentage rate (decimal format, for example: 0.05): "))
years_of_investment = int(input("Please insert number of years of investment: "))
invest(initial_amount, rate_of_return, years_of_investment)