import os
os.chdir('C:/Users/wrwsc/Desktop/Skillbox/skillBoxTaks/module-9/task-6')


def collect_stats(file_name):
    result = {}
    with open(file_name, 'r') as file:
        for i_line in file:
            for j_char in i_line: 
                if j_char.isalpha():
                    if(j_char not in result):
                        result[j_char] = 0
                else:
                    continue
                result[j_char] += 1
    return result


print(collect_stats('voina_i_mir.txt'))