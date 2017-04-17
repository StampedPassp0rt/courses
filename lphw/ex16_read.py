from sys import argv

script, filename = argv

f = open(filename, 'r')

#print the file prettily.
print f.read()

question = raw_input("Are you done reading the file?")
if (question == 'Y') | (question == 'y') | (question == 'Yes') | (question == 'yes') | (question == 'YES'):
    f.close()
    print "Done! File closed."
else:
    print "Sorry, but you actually are done. You just don't realize that yet.\nFile Closed!"
    f.close()
