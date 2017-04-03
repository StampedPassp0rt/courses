#The binary joke file.


x = "There are %d types of people in the world." % 10 #I like the "in the world" addition.
binary = "binary" #string.
do_not = "don't"
#Printing two strings in a string.
y = "Those who know %s and those who %s." % (binary, do_not) #And no, I do not think in binary yet. Makes things like >> annoying.

print x
print y
#Printing the joke precursor string
print "I said: %r" % x
#Printing the punch line string.
print "I also said: '%s'." % y

hilarious_out = False
hilarious_in_group = "Yes, by George it is!"

joke_evaluation = "Isn't that joke so funny?! %r"

#print joke_evaluation % hilarious_in_group
print joke_evaluation % hilarious_out

w = "This is the left side of..."
e = "a string with a right side."

print w + e
