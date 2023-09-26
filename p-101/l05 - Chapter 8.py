# 8.1. Compare Values
'''1. For each of the following conditional expressions, guess whether they evaluate to True or False. 
Then type them into the interactive window to check your answers:
1 <= 1 True
1 != 1 False
1 != 2 F
"good" != "bad" T
"good" != "Good" T
123 == "123" F  '''
print("8.1 - 1 - - - - - - - -")
'''2. For each of the following expressions, fill in the blank (indicated by __) with an appropriate 
boolean comparator so that the expression evaluates to True:
3 < 4
10 > 5
"jack" != "jill"
42 != "42"  '''
print("8.1 - 2 - - - - - - - -")

# 8.2. Add Some Logic
'''1. Figure out what the result will be (True or False) when evaluating the following expressions, 
then type them into the interactive window to check your answers:
(1 <= 1) and (1 != 1) F
not (1 != 2) F
("good" != "bad") or False T
("good" != "Good") and not (1 == 1)  F'''
print("8.2 - 1 - - - - - - - -")
'''2. Add parentheses where necessary so that each of the following expressions evaluates to True:
False == (not True)
(True and False) == (True and False)
not (True and "A") == "B"  '''
print("8.2 - 2 - - - - - - - -")

# 8.3. Control the Flow of Your Program
'''1. Write a script that prompts the user to enter a word using the input() function, 
stores that input in a variable, and then displays whether the length of that string 
is less than 5 characters, greater than 5 characters, or equal to 5 characters by 
using a set of if, elif and else statements.'''
print("8.3 - 1 - - - - - - - -")
word = input("Enter a word: ")
if len(word) > 5:
    print(f"Length of the word '{word}' is greater then 5 characters.")
elif len(word) == 5:
    print(f"Length of the word '{word}' is greater equal to 5 characters.")
else:
    print(f"Length of the word '{word}' is less then 5 characters.")

# 8.4 Challenge: Find the Factors of a Number
'''A factor of a positive integer n is any positive integer less than or equal to n that 
divides n with no remainder. For example, 3 is a factor of 12 because 12 divided by 
3 is 4, with no remainder. However, 5 is not a factor of 12 because 5 goes into 12 twice
with a remainder of 2.
Write a script factors.py that asks the user to input a positive integer and then prints 
out the factors of that number. Here's a sample run of the program with output:
Enter a positive integer: 12
1 is a factor of 12
2 is a factor of 12
3 is a factor of 12
4 is a factor of 12
6 is a factor of 12
12 is a factor of 12
Hint: Recall from Chapter 5 that you can use the % operator to get the
remainder of dividing one number by another.'''
print("8.4 - Challenge")
def factor(number):
    for i in range(1, number+1):
        if number % i == 0:
            print(f"{i} is a factor of {number}")
            
user_input = int(input("Enter positive integer: "))
factor(user_input)

# 8.5. Break Out of the Pattern
'''1. Using break, write a program that repeatedly asks the user for some
input and only quits if the user enters "q" or "Q".'''
print("8.5 - 1 - - - - - - - -")
while True:
    input_851 = input("Enter some input (enter q or Q to exit): ")
    if input_851 == "q" or "Q":
        break

'''2. Using continue, write a program that loops over the numbers 1 to 
50 and prints all numbers that are not multiples of 3.'''
print("8.5 - 2 - - - - - - - -")
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)

# 8.6. Recover From Errors
'''1. Write a script that repeatedly asks the user to input an integer, displaying a message 
to “try again” by catching the ValueError that is raised if the user did not enter an integer.
Once the user enters an integer, the program should display the number back to the user 
and end without crashing.'''
print("8.6 - 1 - - - - - - - -")
while True:
    try:
        input_861 = int(input("Enter an integer: "))
        print(f"Integer you entered is: {input_861}")
        break
    except ValueError:
        print("Try again")

'''2. Write a program that asks the user to input a string and an integer n. 
Then display the character at index n in the string. Use error handling to make sure the 
program doesn't crash if the user does not enter an integer or the index is out of bounds.
The program should display a different message depending on what error occurs.'''
print("8.6 - 2 - - - - - - - -")
try:
    input_862_str = input("Enter a string: ")
    input_862_int = int(input("Enter an integer: "))
    print(input_862_str[input_862_int])
except ValueError:
    print("Try again. You must enter an integer.")
except IndexError:
    print("Try again. String is too short or number is too high.")

# 8.7. Simulate Events and Calculate Probabilities
'''1. Write a function called roll() that uses the randint() function to simulate rolling 
a fair die by returning a random integer between 1 and 6.'''
print("8.7 - 1 - - - - - - - -")
import random
def roll():
    return random.randint(1, 6)
print(f"Random number between 1 and 6 is: {roll()}")

'''2. Write a script that simulates 10,000 rolls of a fair die and displays the average 
number rolled.'''
print("8.7 - 2 - - - - - - - -")
import random
total_rolls = 0
for i in range(10000):
    total_rolls += roll()    
average_roll = total_rolls / 10000
print(f"The average value of 10,000 rolls of die is {average_roll:.02f}")

# 8.8 Challenge: Simulate a Coin Toss Experiment
'''Suppose you flip a fair coin repeatedly until it lands on both heads and tails at 
least once each. In other words, after the first flip, you continue to flip the coin 
until it lands on something different. Doing this generates a sequence of heads and 
tails. For example, the first time you do this experiment, the sequence might be 
heads, heads, then tails. On average, how many flips are needed for the sequence 
to contain both heads and tails? Write a simulation that runs 10,000 trials of the 
experiment and prints the average number of flips per trial.'''
print("8.8 - Challenge")
import random
def toss_a_coin_to_your_witcher():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

NUMBER_OF_EXPERIMENTS = 10000
average = flip_count = 0
for trial in range(NUMBER_OF_EXPERIMENTS):
    if toss_a_coin_to_your_witcher() == "heads":
        flip_count += 1
    while toss_a_coin_to_your_witcher() == "heads":
        flip_count += 1
    flip_count += 1

average = flip_count/NUMBER_OF_EXPERIMENTS
print(f"The average number of flips needed for both heads and tails is {average}")

# 8.9 Challenge: Simulate an Election
'''With some help from the random module and a little condition logic, you can 
simulate an election between two candidates. Suppose two candidates, Candidate 
A and Candidate B, are running for mayor in a city with three voting regions. 
The most recent polls show that Candidate A has the following chances for 
winning in each region:
• Region 1: 87% chance of winning
• Region 2: 65% chance of winning
• Region 3: 17% chance of winning
Write a program that simulates the election 10,000 times and prints the percentage 
of where Candidate A wins. To keep things simple, assume that a candidate wins the 
election is they win in at least two of the three regions.'''
print("8.9 - Challenge")
import random
NUMBER_OF_ELECTIONS = 10000
CHANCE_CANDIDATE_A_WINS_IN_REGION_1_2_3 = [0.87, 0.65, 0.17]
REGIONS_NEEDED_TO_WIN_ELECTIONS = int(2)
A_wins = B_wins = 0

def simulation_of_elections(probability_A_wins):
    if random.random() < probability_A_wins:
        return "candidate_A"
    else:
        return "candidate_B"

for election in range(NUMBER_OF_ELECTIONS):    
    for region in CHANCE_CANDIDATE_A_WINS_IN_REGION_1_2_3:
        if simulation_of_elections(region) == "candidate_A":
            A_wins += 1
        else:
            B_wins += 1

print(f"Chance of Candidate A winnig is: {A_wins/30000*100:.02f}%")   