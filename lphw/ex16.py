'''Exercise 16 of LPHW. Before I begin, a few comments:

1) close. Apparently like the 'Save' command for a file. Closes the file.

2) read. Reads the contents of a file, can be assigned to a variable. Probably built
into pandas and other Python libraries with methods performing this, like requests.

3) readline. Reads one line of a file.

4) truncate. Emptys the file. Kind of like 'Select All' and 'Clear'. Probably best deployed sparingly.

5) write('stuff'). Writes the string 'stuff' to a file (so still a string command).

'''

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#w and w+ automatically truncate the file if it exists. a+ does not. For appending to existing file.
target = open(filename, 'w')

print "Truncating the file. Clears out the file. Goodbye!"
#target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file."

target.write(line1+"\n"+line2+"\n"+line3+"\n")

print "And finally, we close it."
target.close()
