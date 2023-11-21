#12.2. Working With File Paths in Python
'''1. Create a new Path object to a file called my_file.txt in a folder called my_folder/ in your computer's home directory. 
Assign this Path object to the variable name file_path.'''
print("12.2 - 1")
from pathlib import Path
new_dir = Path.home() / "my_folder"
new_dir.mkdir(exist_ok=True)

file_path = Path.home() / "my_folder" / "my_file.txt"
file_path.touch()

'''2. Check whether or not the path assigned to file_path exists.'''
print("12.2 - 2")
print(file_path.exists())

'''3. Print the name of the path assigned to file_path. The output should be my_file.txt.'''
print("12.2 - 3")
print(file_path.name)

'''4. Print the name of the parent directory of the path assigned to file_path. The output should be my_folder.'''
print("12.2 - 4")
print(file_path.parent.name)

#12.3. Common File System Operations
'''1. Create a new directory in your home folder called my_folder/.'''
print("12.3 - 1")
new_dir = Path.home() / "my_folder"
new_dir.mkdir(exist_ok=True)
print(new_dir.exists())

'''2. Inside my_folder/ create three files: • file1.txt • file2.txt • image1.png'''
print("12.3 - 2")
file1 = new_dir / "file1.txt"
file1.touch()
file2 = new_dir / "file2.txt"
file2.touch()
image1 = new_dir / "image1.png"
image1.touch()

print(f"Does file {file1.name} exists? {file1.exists()}")
print(f"Does file {file2.name} exists? {file2.exists()}")
print(f"Does file {image1.name} exists? {image1.exists()}")

'''3. Move the file image1.png to a new directory called images/ inside of
the my_folder/ directory.'''
print("12.3 - 3")
(new_dir / "images").mkdir(exist_ok=True)
(image1).replace(new_dir / "images" / "image1.png")

'''4. Delete the file file1.txt'''
print("12.3 - 4")
file1.unlink()

'''5. Delete the my_folder/ directory.'''
print("12.3 - 5")
import shutil
shutil.rmtree(new_dir)


#12.4 Challenge: Move All Image Files To a New Directory
'''In the Chapter 12 Practice Files folder, there is a subfolder called documents/. The directory contains several files 
and subfolder. Some of the files are images ending with either the .png, .gif, or the .jpg file extension.
Create a new folder in the Practice Files folder called images/ and move all image files to that folder. 
When you are done, the new folder should have four files in it:
1. image1.png
2. image2.gif
3. image3.png
4. image4.jpg   '''
print("12.4 - Challenge")
path_12_4_challenge = Path.home() / "practice_files" / "documents"
(path_12_4_challenge / "images").mkdir(exist_ok=True)
list1 = [path.replace((path_12_4_challenge / "images" / path.name)) for path in path_12_4_challenge.rglob("*") if path.suffix in [".png", ".jpg", ".gif"]]

#for path in path_12_4_challenge.rglob("*"):
#    if path.suffix in [".png", ".jpg", ".gif"]:
#        path.replace((path_12_4_challenge / "images" / path.name))

#12.5. Reading and Writing Files
'''1. Write the following text to file called starships.txt in your home directory: Discovery Enterprise Defiant Voyager
Each word should be on a separate line.'''
print("12.5 - 1")
ships = ['Discovery\n', 'Enterprise\n', 'Defiant\n', 'Voyager\n']
(Path.home() / "python").mkdir(exist_ok=True)
path_12_5 = Path.home() / "python" / "starships.txt"
with open(path_12_5, "w") as file:
    file.writelines(ships)

'''2. Read the file starhips.txt you created in Exercise 1 and print each line of text in the file. 
The output should not have extra blank lines between each word.'''
print("12.5 - 2")
with open(path_12_5, "r") as file:
    for line in file.readlines():
        print(line, end="")

'''3. Read the file startships.txt and print the names of the starships that start with the letter D.'''
print("12.5 - 3")
with open(path_12_5, "r") as file:
    for line in file.readlines():
        if line.startswith("D"):
            print(line, end="")

            
#12.6. Read and Write CSV Data
'''1. Write a script that writes the following list of lists to a file called numbers.csv in your home directory:'''
print("12.6 - 1")
import csv
numbers = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
path_12_6 = Path.home() / "python" / "numbers.csv"
with open(path_12_6, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(numbers)

'''2. Write a script that reads the numbers in the numbers.csv file from Exercise 1 into a list of lists of integers 
called numbers. Print the list of lists. Your output should like the following:
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]'''
print("12.6 - 2")
numbers = []
with open(path_12_6, "r", encoding="utf-8") as file:
    for row in csv.reader(file):
        numbers.append([int(i) for i in row])
print(numbers)

'''3. Write a script that writes the following list of dictionaries to a file called favorite_colors.csv in your home directory. 
The output CSV file should have the following format:
name,favorite color
Joe,blue
Anne,green
Bailey,red'''
print("12.6 - 3")
favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"}, 
    {"name": "Anne", "favorite_color": "green"}, 
    {"name": "Bailey", "favorite_color": "red"} ]
path_12_6_3 = Path.home() / "python" / "favourite_colors.csv"
with open(path_12_6_3, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=favorite_colors[0].keys())
    writer.writeheader()
    writer.writerows(favorite_colors)

'''4. Write a script that reads the data from the favorite_colors.csv file from Exercise 3 into a list of dictionaries called 
favorite_colors. Print the list of dictionaries. The output should look something like this:
[{"name": "Joe", "favorite_color": "blue"},
{"name": "Anne", "favorite_color": "green"},
{"name": "Bailey", "favorite_color": "red"}]'''
print("12.6 - 4")
favorite_colors = []
with open(path_12_6_3, "r", encoding="utf-8") as file:
    for row in csv.DictReader(file): 
        favorite_colors.append(row)
for i in favorite_colors:
    print(i)


#12.7 Challenge: Create a High Scores List
'''In the Chapter 12 Practice Files folder, there is a CSV file called scores.csv containing data about game players 
and their scores. Write a script that reads the data from this CSV file and creates a new file called high_scores.csv 
where each row contains the player nameand their highest score. The output CSV file should look like this:
name,high_score
LLCoolDave,27
red,12
tom123,26
O_O,7
Misha46,25
Empiro,23
MaxxT,25
L33tH4x,42
johnsmith,30    '''
print("12.7 - Challenge")
scores = []
high_score = {}
file_path = Path.home() / "practice_files" / "scores.csv"

with open(file_path, "r", encoding="utf-8") as file:
    scores = [row for row in csv.DictReader(file)]
        
for result in scores:
    name = result['name']
    score = int(result['score'])
    if name not in high_score or score > high_score[name]:
        high_score[name] = score

highest_scores = [{'name': name, 'high_score': score} for name, score in high_score.items()]

file_path = Path.home() / "practice_files" / "high_scores.csv"
with open(file_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=highest_scores[0].keys())
    writer.writeheader()
    writer.writerows(highest_scores)