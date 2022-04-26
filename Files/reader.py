filename = 'f.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

string = ''
for line in lines:
    string += line.strip()

with open('new.txt', 'w') as new_file:
    new_file.write(string +'\n')


with open('new.txt', 'a') as file_object:
    file_object.write('I love programming\n')
    file_object.write('My stack is:\n')
    file_object.write('\t-Python\n')
    file_object.write('\t-JavaScript\n')
        
