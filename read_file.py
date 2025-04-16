# The open() function opens a file, and returns it as a file object
# open(file,mode)

#file: The path and name of the file
#mode: A string, define which mode you want to open the file in:
#      'r': Read - default value. opens a file for reading, error if the file doesn't exist
#      'a': Append - Opens a file for appending, creates teh file if it doesn not exist
#      'w': Write - opens a file for writing, creates the file if it does not exist
#      'x': Create - creates the specified file, returns an error if the file exist
#      't': Text: default value. text mode
#      'b': Binary: Binary mode

import os
os.system("clear")

# with open('docs/text.txt','r') as f:
#     line = f.readline()
#     while line:
#         print(line)
#         line = f.readline()

counter_dict = {}
with open('docs/text.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = f.readline()        
print(counter_dict)        

counter_dict2 = {}
with open('docs/training.txt') as f:
    line = f.readline()
    while line:
        line = line[3:-26]
        if line in counter_dict2:
            counter_dict2[line] += 1
        else:
            counter_dict2[line] = 1    
        line = f.readline()
print(counter_dict2)        