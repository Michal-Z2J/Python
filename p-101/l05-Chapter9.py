# 9.1 Tuples Are Immutable Sequences
'''1. Create a tuple literal named cardinal_numbers that holds the strings
"first", "second" and "third", in that order. '''
print("9.1 - 1 - - - - - - - -")
cardinal_numbers = ("first", "second", "third")
print(cardinal_numbers)

'''2. Using index notation and print(), display the string at index 1 in cardinal_numbers.'''
print("9.1 - 2 - - - - - - - -")
for word in cardinal_numbers:
    print(word[1])

'''3. Unpack the values in cardinal_numbers into three new strings
named position1, position2 and position3 in a single line of code,
then print each value on a separate line.'''
print("9.1 - 3 - - - - - - - -")
position1, position2, position3 = cardinal_numbers
print(position1, position2, position3, sep="\n")

'''4. Create a tuple called my_name that contains the letters of your name
by using tuple() and a string literal.'''
print("9.1 - 4 - - - - - - - -")
my_name = tuple("Michael")
print(my_name)

'''5. Check whether or not the character "x" is in my_name using the in keyword.'''
print("9.1 - 5 - - - - - - - -")
print("x" in my_name)

'''6. Create a new tuple containing all but the first letter in my_name using slicing notation.'''
print("9.1 - 6 - - - - - - - -")
new_name = tuple(my_name[1:])
print(new_name)

#9.2. Lists Are Mutable Sequences
'''1. Create a list named food with two elements "rice" and "beans".'''
print("9.2 - 1 - - - - - - - -")
food = ["rice", "beans"]
print(food)
'''2. Append the string "broccoli" to food using .append().'''
print("9.2 - 2 - - - - - - - -")
food.append("broccoli")
print(food)

'''3. Add the string "bread" and "pizza" to "food" using .extend().'''
print("9.2 - 3 - - - - - - - -")
food.extend(("bread", "pizza"))
print(food)

'''4. Print the first two items in the food list using print() and slicing notation.'''
print("9.2 - 4 - - - - - - - -")
print(food[0:2])

'''5. Print the last item in food using print() and index notation.'''
print("9.2 - 5 - - - - - - - -")
print(food[-1:])

'''6. Create a list called breakfast from the string "eggs, fruit, orange
juice" using the string .split() method.'''
print("9.2 - 6 - - - - - - - -")
breakfast = ("eggs, fruit, orange juice").split(", ")
print(breakfast)

'''7. Verify that breakfast has three items using len().'''
print("9.2 - 7 - - - - - - - -")
print(len(breakfast))

'''8. Create a new list called lengths using a list comprehension that contains
the lengths of each string in the breakfast list.'''
print("9.2 - 8 - - - - - - - -")
lengths = [len(length) for length in breakfast]
print(lengths)

# 9.3. Nesting, Copying, and Sorting Tuples and Lists
'''1. Create a tuple data with two values. The first value should be the
tuple (1, 2) and the second value should be the tuple (3, 4).'''
print("9.3 - 1 - - - - - - - -")
tuple_data = ((1, 2), (3, 4))
print(tuple_data)

'''2. Write a for loop that loops over data and prints the sum of each
nested tuple. The output should look like this:
Row 1 sum: 3
Row 2 sum: 7'''
print("9.3 - 2 - - - - - - - -")
num = 1
for nest_tuple in tuple_data:    
    print(f"Row {num} sum: {nest_tuple[0] + nest_tuple[1]}")
    num += 1

'''3. Create the following list [4, 3, 2, 1] and assign it to the variable numbers.'''
print("9.3 - 3 - - - - - - - -")
numbers = [4, 3, 2, 1]
print(numbers)
'''4. Create a copy of the numbers list using the [:] slicing notation.'''
print("9.3 - 4 - - - - - - - -")
copy_numbers = numbers[:]
print(copy_numbers)

'''5. Sort the numbers list in numerical order using the .sort() method.'''
print("9.3 - 5 - - - - - - - -")
numbers.sort()
print(numbers)

# 9.4 Challenge: List of lists
'''Write a program that contains the following lists of lists:
universities = [['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]  ]
Define a function, enrollment_stats(), that takes, as an input, a list of
lists where each individual list contains three elements: (a) the name
of a university, (b) the total number of enrolled students, and (c) the
annual tuition fees.
enrollment_stats() should return two lists: the first containing all of
the student enrollment values and the second containing all of the
tuition fees.
Next, define a mean() and a median() function. Both functions should
take a single list as an argument and return the mean and median of
the values in each list.
Using universities, enrollment_stats(), mean(), and median(), calculate
the total number of students, the total tuition, the mean and median
of the number of students, and the mean and median tuition values.
Finally, output all values, and format the output so that it looks like this:
******************************
Total students: 77,285
Total tuition: $ 271,905
Student mean: 11,040.71
Student median: 10,566
Tuition mean: $ 38,843.57
Tuition median: $ 39,849
******************************      '''
print("9.4 - Challenge")
universities = [['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]]

def enrollment_stats(universities_list):
    students = [students for name, students, fee in universities_list]    
    fees = [fee for name, students, fee in universities_list]
    return students, fees

def mean(mean_list):
    average = 0
    for value in mean_list:
        average += value
    return average / len(mean_list)

def median(median_list):    
    median_list.sort()    
    return median_list[3]
        
number_of_students, tuition_values = enrollment_stats(universities)

print(f"Total students: {sum(number_of_students)}")

print(f"Total tuition: {sum(tuition_values)}")

students_mean = mean(number_of_students)
print(f"Student mean: {students_mean:.02f}")

students_median = median(number_of_students)
print(f"Student median: {students_median}")

tuition_mean = mean(tuition_values)
print(f"Tuition mean: {tuition_mean:.02f}")

tuition_median = median(tuition_values)
print(f"Tuition median: {tuition_median}")

# 9.5 Challenge: Wax Poetic
'''Create five lists for different word types:
• Nouns: ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]
• Verbs: ["kicks", "jingles", "bounces", "slurps", "meows",
"explodes", "curdles"]
• Adjectives: ["furry", "balding", "incredulous", "fragrant",
"exuberant", "glistening"]
• Prepositions: ["against", "after", "into", "beneath", "upon",
"for", "in", "like", "over", "within"]
• Adverbs: ["curiously", "extravagantly", "tantalizingly",
"furiously", "sensuously"]
Randomly select the following number of elements from each list:
• 3 nouns
• 3 verbs
• 3 adjectives
• 2 prepositions
• 1 adverb
You can do this with the choice() function in the random module. This
function takes a list as input and returns a randomly selected element
of the list.
For example, here's how you use random.choice() to get random element
from the list ["a", "b", "c"]:
import random
random_element = random.choice(["a", "b", "c"])
Using the randomly selected words, generate and display a poem with
the following structure inspired by Clifford Pickover:
{A/An} {adj1} {noun1}
{A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}
Here, adj stands for adjective and prep for preposition.
Here's an example of the kind of poem your program might generate:
A furry horse
A furry horse curdles within the fragrant mango
extravagantly, the horse slurps
the mango meows beneath a balding extrovert
Every time your program runs, it should generate a new poem.    '''
print("9.5 - Challenge")
import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"] 
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

universities = [['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]]

def randomize(list):  
    return random.choice(list)

def make_poem():
    l_adjectives = list(adjectives)
    l_nouns = list(nouns)
    l_verbs = list(verbs)
    l_prepositions = list(prepositions)

    adj1 = randomize(l_adjectives)
    l_adjectives.remove(adj1)
    adj2 = randomize(l_adjectives)
    l_adjectives.remove(adj2)
    adj3 = randomize(l_adjectives)

    noun1 = randomize(l_nouns)
    l_nouns.remove(noun1)
    noun2 = randomize(l_nouns)
    l_nouns.remove(noun2)
    noun3 = randomize(l_nouns)

    verb1 = randomize(l_verbs)
    l_verbs.remove(verb1)
    verb2 = randomize(l_verbs)
    l_verbs.remove(verb2)
    verb3 = randomize(l_verbs)

    prep1 = randomize(l_prepositions)
    l_prepositions.remove(prep1)
    prep2 = randomize(l_prepositions)

    adverb1 = randomize(adverbs)
 
    if "aeiou".find(adj1[0]) != -1:
        article = "An"
    else:
        article = "A"
      
    print(f"{article} {adj1} {noun1}")
    print(f"{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}")
    print(f"{adverb1}, the {noun1} {verb2}")
    print(f"the {noun2} {verb3} {prep2} a {adj3} {noun3}")

make_poem()

#9.6. Store Relationships in Dictionaries
'''1. Create an empty dictionary named captains.'''
print("9.6 - 1 - - - - - - - -")
captains = {}

'''2. Using the square bracket notation, enter the following data into the dictionary, one item at a time:
'Enterprise': 'Picard', 'Voyager': 'Janeway', 'Defiant': 'Sisko'  '''
print("9.6 - 2 - - - - - - - -")
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

'''3. Write two if statements that check if "Enterprise" and "Discovery" exist as keys in 
the dictionary. Set their values to "unknown" if the key does not exist.'''
print("9.6 - 3 - - - - - - - -")
if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

'''4. Write a for loop to display the ship and captain names contained
in the dictionary. For example, the output should look something
like this:
The Enterprise is captained by Picard.  '''
print("9.6 - 4 - - - - - - - -")
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}")

'''5. Delete "Discovery" from the dictionary.'''
print("9.6 - 5 - - - - - - - -")
del captains["Discovery"]

'''6. Bonus: Make the same dictionary by using dict() and passing in 
the initial values when you first create the dictionary.'''
print("9.6 - 6 - - - - - - - -")
captains = dict([("Enterprise", "Picard"), ("Voyager", "Janeway"), ("Defiant", "Sisko"),])

# 9.7 Challenge: Capital City Loop
'''First, finish filling out the following dictionary with the remaining
states and their associated capitals in a file called capitals.py.
capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',   }
Next, pick a random state name from the dictionary, and assign both
the state and it's capital to two variables. You'll need to import the
random module at the top of your program.
Then display the name of the state to the user and ask them to enter
the capital. If the user answers, incorrectly, repeatedly ask them for
the capital name until they either enter the correct answer or type the
word “exit”.
If the user answers correctly, display "Correct" and end the program.
However, if the user exits without guessing correctly, display the correct
answer and the word "Goodbye".
Note: Make sure the user is not punished for case sensitivity. In other
words, a guess of "Denver" is the same as "denver". Do the same
for exiting—"EXIT" and "Exit" should work the same as "exit". '''
print("9.7 - Challenge")
import random
capitals_dict = {
    "Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock",
    "California": "Sacramento", "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover",
    "Florida": "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise",
    "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines",
    "Kansas": "Topeka", "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta",
    "Maryland": "Annapolis", "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "St. Paul",
    "Mississippi": "Jackson", "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln",
    "Nevada": "Carson City", "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe",
    "New York": "Albany", "North Carolina": "Raleigh", "North Dakota": "Bismarck", "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence",
    "South Carolina": "Columbia", "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin",
    "Utah": "Salt Lake City", "Vermont": "Montpelier", "Virginia": "Richmond", "Washington": "Olympia",
    "West Virginia": "Charleston", "Wisconsin": "Madison", "Wyoming": "Cheyenne"
}
random_state = random.choice(list(capitals_dict))
while True:    
    answer = input(f"Enter capital of {random_state} (enter 'exit' to close program): ")
    if answer.lower() == capitals_dict[random_state].lower():
        print("Correct")
        break
    elif answer.lower() == "exit":
        print("Goodbye")
        break

# 9.9 Challenge: Cats With Hats
'''You have 100 cats.
One day you decide to arrange all your cats in a giant circle. Initially,
none of your cats have any hats on. You walk around the circle 100
times, always starting at the same spot, with the first cat (cat # 1). Every
time you stop at a cat, you either put a hat on it if it doesn't have
one on, or you take its hat off if it has one on.
1. The first round, you stop at every cat, placing a hat on each one.
2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
3. The third round, you only stop at every third cat (#3, #6, #9, #12, etc.).
4. You continue this process until you've made 100 rounds around
the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.'''
print("9.9 - Challenge")
cat_dict = {f'Cat {i}': False for i in range(1, 101)}

for round in range(1, 101):
    for cat in list(cat_dict):
        if (list(cat_dict).index(cat)+1) % round == 0:
            cat_dict[cat] = not cat_dict[cat]

cats_with_hats = [kitty for kitty, hat in cat_dict.items() if hat == True]

print(f"There are {len(cats_with_hats)} cats with hats and they are: {cats_with_hats}")