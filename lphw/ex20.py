from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

#need to pass the line count and file.
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file, 'r')

print "First, let's print the whole file: \n"
print_all(current_file)

print "Now, let's rewind."
rewind(current_file)

print ("let's print three lines:")
for i in range(1,4):
    print_a_line(i, current_file)

print ("Printing three lines with += notation on the backend.")
rewind(current_file)
current_line = 1
while current_line <= 3:
    print_a_line(current_line, current_file)
    current_line += 1

current_file.close()
