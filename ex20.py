# import argv module
from sys import argv

# unpack argv to script and input_file
script, input_file = argv

# function to print the whole file that is passed in
def print_all(f):
    # read the file then prints
    print(f.read())

# function change which line is read to the first line
def rewind(f):
    # set line read to the first line
    f.seek(0)

# function to print integer and current line of a file that is passed in
def print_a_line(line_count, f):
    # print int and line of a file
    print(line_count, f.readline())

# open file and set to variable
current_file = open(input_file)

# prints a string prompt
print("First let's print the whole file:\n")

# calls print_all function to print whole file
print_all(current_file)

# prints a string prompt
print("Now let's rewind, kind of like a tape.")

# call rewind function to set current read line to the first
rewind(current_file)

# prints a string prompt
print("Let's print three lines:")

# creates current_file variable set to 1
current_line = 1
# call print_a_line function to print the current value of current_line and
# line of file which is 1 and the first line
print_a_line(current_line, current_file)

# add one to current_line
current_line += 1
# call print_a_line function to print the current value of current_line and
# line of file which is 2 and the second line
print_a_line(current_line, current_file)

# add one to current_line
current_line += 1
# call print_a_line function to print the current value of current_line and
# line of file which is 3 and the thrid line
print_a_line(current_line, current_file)
