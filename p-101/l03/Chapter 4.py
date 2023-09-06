#4.1 What is a string
'''1. Print a string that uses double quotation marks inside the string.'''
print("4.1 - 1 - - - - - - - -")
print('"Hello World"')

'''2. Print a string that uses an apostrophe inside the string.'''
print("4.1 - 2 - - - - - - - -")
print("'Hello World'")

'''3. Print a string that spans multiple lines, with whitespace preserved.'''
print("4.1 - 3 - - - - - - - -")
print('''bardzo długi string
          trzeba podzielić 
      na trzy wiersze''')

'''4. Print a string that is coded on multiple lines but displays on a single line.'''
print("4.1 - 4 - - - - - - - -")
print("bardzo długi string trzeba \
podzielić na dwa wiersze w kodzie")

#4.2. Concatenation, Indexing, and Slicing
'''1. Create a string and print its length using the len() function.'''
print("4.2 - 1 - - - - - - - -")
string1 = "Hello world"
print(len(string1))

'''2. Create two strings, concatenate them, and print the resulting string.'''
print("4.2 - 2 - - - - - - - -")
string2 = "You too"
print(string1 + string2)

'''3. Create two strings and use concatenation to add a space inbetween them. Then print the result.'''
print("4.2 - 3 - - - - - - - -")
print(string1 + " " + string2)

'''4. Print the string "zing" by using slice notation on the string "bazinga" to specify the correct range of characters.'''
print("4.2 - 4 - - - - - - - -")
string3 = "Bazinga"
print(string3[2:6])

#4.3. Manipulate Strings With Methods
'''1. #Write a script that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honeybadger". Print each lowercase string on a separate line.'''
print("4.3 - 1 - - - - - - - -")
a1 = "Animals"
a2 = "Badger"
a3 = "Honey Bee"
a4 = "Honeybadger"
print(a1.lower())
print(a2.lower())
print(a3.lower())
print(a4.lower())

'''2. Repeat Exercise 1, but convert each string to uppercase instead of lowercase.'''
print("4.3 - 2 - - - - - - - -")
print(a1.upper())
print(a2.upper())
print(a3.upper())
print(a4.upper())

'''3. Write a script that removes whitespace from the following strings: string1 = " Filet Mignon", string2 = "Brisket ", string3 = " Cheeseburger ". Print out the strings with the whitespace removed.'''
print("4.3 - 3 - - - - - - - -")
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

'''4. Write a script that prints out the result of .startswith("be") on each of the following strings:'''
print("4.3 - 4 - - - - - - - -")
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

'''5. Using the same four strings from Exercise 4, write a script that uses string methods to alter each string so that .startswith("be") returns True for all of them.'''
print("4.3 - 5 - - - - - - - -")
print(string1.lower().startswith("be"))
print(string2.lower().startswith("be"))
print(string3.lower().startswith("be"))
print(string4.lower().strip().startswith("be"))

#4.4. Interact With User Input
'''1. Write a script that takes input from the user and displays that input back.'''
print("4.4 - 1 - - - - - - - -")
input441 = input("Wprowadż przykładowe dane: ")
print(input441)

'''2. Write a script that takes input from the user and displays the input in lowercase.'''
print("4.4 - 2 - - - - - - - -")
print(input441.lower())

'''3. Write a script that takes input from the user and displays the number of characters inputted.'''
print("4.4 - 3 - - - - - - - -")
print(len(input441))

#4.5. Challenge: Pick Apart Your User's Input
'''Write a script named first_letter.py that first prompts the user for
input by using the string "Tell me your password:" The script should
then determine the first letter of the user's input, convert that letter
to upper-case, and display it back.'''

user_input = input("Tell me your password: ")
print("The first letter you entered was: ", user_input.strip().upper()[0])

#4.6 Working With Strings and Numbers
'''1. Create a string containing an integer, then convert that string into an actual integer object using int(). 
Test that your new object is a number by multiplying it by another number and displaying the result.'''
print("4.6 - 1 - - - - - - - -")
string61 = "44"
print(int(string61) * 2)

'''2. Repeat the previous exercise, but use a floating-point number and float().'''
print("4.6 - 2 - - - - - - - -")
string62 = "55.2"
print(float(string62) * 2)

'''3. Create a string object and an integer object, then display them sideby-side with a single print statement by using the str() function.'''
print("4.6 - 3 - - - - - - - -")
int6 = 12
string63 = "hello"
print(string63 + str(int6))

'''4. Write a script that gets two numbers from the user using the input() function twice, multiplies the numbers together, and displays the result. 
If the user enters 2 and 4, your program should print the following text: "The product of 2 and 4 is 8.0."'''
print("4.6 - 4 - - - - - - - -")
n1 = input("Wprowadz pierwszą liczbę: ")
n2 = input("Wprowadz drugą liczbę: ")
print("The product of ", n1, " and ",  n2, " is ", float(n1) * float(n2))

# 4.7. Streamline Your Print Statements
'''1. Create a float object named weight with the value 0.2, and create a string object named animal with the value "newt". 
Then use these objects to print the following string using only string concatenation: 0.2 kg is the weight of the newt.'''
print("4.7 - 1 - - - - - - - -")
weight = 0.2
animal = "newt"
print(str(weight) + " is the weight of the " + animal)

'''2. Display the same string by using the .format() method and empty {} place-holders.'''
print("4.7 - 2 - - - - - - - -")
print("{} is the weight of the {}".format(str(weight), animal))

'''3. Display the same string using an f-string.'''
print("4.7 - 3 - - - - - - - -")
print(f"{str(weight)} is the weight of the {animal}")

# 4.8. Find a String in a String
'''1. In one line of code, display the result of trying to .find() the substring "a" in the string "AAA". The result should be -1.'''
print("4.8 - 1 - - - - - - - -")
string48 = "AAA"
print(string48.find("a"))

'''2. Replace every occurrence of the character "s" with "x" in the string "Somebody said something to Samantha.".'''
print("4.8 - 2 - - - - - - - -")
string482 = "Somebody said something to Samantha."
print(string482.replace("s", "x"))

'''3. Write and test a script that accepts user input using the input() function and displays the result of trying to .find() a particular letter in that input.'''
print("4.8 - 3 - - - - - - - -")
user_input = input("Wprowadź przykładowy string: ")
print("Pierwsze wystąpienie litery 'h' w podanym stringu to index: ", user_input.find("h"))

#4.9 Challenge: Turn Your User Into a L33t H4x0r
'''Write a script called translate.py that asks the user for some input
with the following prompt: Enter some text:. Then use the .replace()
method to convert the text entered by the user into “leetspeak” by making
the following changes to lower-case letters:
• The letter a becomes 4
• The letter b becomes 8
• The letter e becomes 3
• The letter l becomes 1
• The letter o becomes 0
• The letter s becomes 5
• The letter t becomes 7
Your program should then display the resulting string as output. Below
is a sample run of the program:
Enter some text: I like to eat eggs and spam.
I 1ik3 70 347 3gg5 4nd 5p4m.'''

prompt = "Enter some text: "
user_input = input(prompt)
user_input = user_input.replace("a", "4").replace("b", "8").replace("e", "3").replace("l", "1").replace("o", "0").replace("s", "5").replace("t", "7")
print(user_input)