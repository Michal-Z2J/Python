#5.1. Integers and Floating-Point Numbers
'''1. Write a script that creates the two variables, num1 and num2. Both num1 and num2 should be assigned the integer 
literal 25,000,000, one written with underscored and one without. Print num1 and num2 on two separate lines.'''
print("5.1 - 1 - - - - - - - -")
num1 = 25000000
num2 = 25_000_000
print(num1)
print(num2)

'''2. Write a script that assigns the floating-point literal 175000.0 to the variable num using exponential notation, 
and then prints num in the interactive window.'''
print("5.1 - 2 - - - - - - - -")
num = 1.75e5
print(num)

'''3. In IDLE's interactive window, try and find the smallest exponent N so that 2e<N>, where <N> is replaced 
with your number, returns inf.'''
print("5.1 - 3 - - - - - - - -")
N = 2e307
print(float(N))

 #5.3 Challenge: Perform Calculations on User Input
'''Write a script called exponent.py that receives two numbers from the user and displays the first 
number raised to the power of the second number. A sample run of the program should look like this 
(with example input that has been provided by the user included below):
    Enter a base: 1.2
    Enter an exponent: 3
    1.2 to the power of 3 = 1.7279999999999998
Keep the following in mind:
1. Before you can do anything with the user's input, you will have to
assign both calls to input() to new variables.
2. The input() function returns a string, so you'll need to convert the
user's input into numbers in order to do arithmetic.
3. You can use an f-string to print the result.
4. You can assume that the user will enter actual numbers as input.'''
print("5.3 - challenge - - ")
num1 = float(input("Enter a base: "))
num2 = float(input("Enter a exponent: "))
print(f"{num1} to the power of {num2} = {num1 ** num2}")

# 5.5. Math Functions and Number Methods
'''1. Write a script that asks the user to input a number and then displays that number rounded to two decimal places. 
When run, your program should look like this: 
Enter a number: 5.432 
5.432 rounded to 2 decimal places is 5.43'''
print("5.5 - 1 - - - - - - - -")
num = float(input("Enter a number: "))
print(f"{num} rounded to 2 decimal places is {num:.02f}")

'''2. Write a script that asks the user to input a number and then displays the absolute value of that number. 
When run, your program should look like this:
Enter a number: -10
The absolute value of -10 is 10.0'''
print("5.5 - 2 - - - - - - - -")
num2 = float(input("Enter a number: "))
print(f"The absolute value of {num2} is {abs(num2)}")

'''3. Write a script that asks the user to input two numbers by using the input() function twice, then display whether 
or not the difference between those two number is an integer. 
When run, your program should look like this:
Enter a number: 1.5
Enter another number: .5
The difference between 1.5 and .5 is an integer? True!
If the user inputs two numbers whose difference is not integral, the output should look like this:
Enter a number: 1.5
Enter another number: 1.0
The difference between 1.5 and 1.0 is an integer? False!'''
print("5.5 - 3 - - - - - - - -")
num3 = float(input("Enter a number: "))
num4 = float(input("Enter another number: "))
diff = abs(num3 - num4)
print(f"The difference between {num3} and {num4} is an integer? {diff.is_integer()}")

# 5.6. Print Numbers in Style
'''1. Print the result of the calculation 3 ** .125 as a fixed-point number with three decimal places.'''
print("5.6 - 1 - - - - - - - -")
print(f"{3 ** 0.125:.03f}")

'''2. Print the number 150000 as currency, with the thousands grouped with commas. 
Currency should be displayed with two decimal places.'''
print("5.6 - 2 - - - - - - - -")
print(f"{150000:,.02f}")

'''3. Print the result of 2 / 10 as a percentage with no decimal places. The output should look like 20%.'''
print("5.6 - 3 - - - - - - - -")
print(f"{2 / 10:.0%}")