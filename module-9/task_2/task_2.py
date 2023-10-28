import os
os.chdir('C:/Users/wrwsc/Desktop/Skillbox/skillBoxTaks/task_2')

with open("zen.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip()) 
