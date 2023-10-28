import os
os.chdir('C:/Users/wrwsc/Desktop/Skillbox/skillBoxTaks/task_1')

with open("numbers.txt", "r") as input_file:
    total_sum = 0
    for line in input_file:
        numbers = line.split()
        for number in numbers:
            total_sum += int(number)

with open("answer.txt", "w") as output_file:
    output_file.write(str(total_sum))
