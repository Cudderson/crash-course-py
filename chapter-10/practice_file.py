# 10-1
# practice different ways of reading file

text_file = 'practice_file' # text file in working directory
with open(text_file) as file:
    lines_in_file = file.read()
    print(lines_in_file)

with open(text_file) as file:
    lines_in_file = file.readlines()
    print(lines_in_file)

with open(text_file) as file:
    file_list = []
    lines_in_file = file.readlines()
    for line in lines_in_file:
        line = line.strip()
        line = line.title()
        file_list.append(line)

for statement in file_list:
    print(statement)



