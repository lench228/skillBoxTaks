import os
print (os.getcwd())
with open("task_1/numbers.txt", "r") as input_file:
    total_sum = 0
    for line in input_file:
        numbers = line.split()
        for number in numbers:
            total_sum += int(number)

with open("task_1/answer.txt", "w") as output_file:
    output_file.write(str(total_sum))
