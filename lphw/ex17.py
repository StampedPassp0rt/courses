from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

indata = open(from_file).read()

if exists(to_file):
    question = raw_input("Do you want to overwrite the file? Y or N")
    if question == "Y":
        out_file = open(to_file, 'w')
        out_file.write(indata)
        out_file.close()
    else:
        print "Did not overwrite file. Done."
else:
    out_file = open(to_file, 'w')
    out_file.write(indata)
    out_file.close()
