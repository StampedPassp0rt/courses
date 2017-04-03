#Exercise 13. A simple program where I test out processing arguments from the command line.

from sys import argv
import re

#what we expect in the CL. The script name, and then three variables.
script, first_name, last_name = argv

print "The script is called: ", script
print "Your name is: %s %s" % (first_name, last_name)

mentor = raw_input("Who is your role model? Someone you look up to? ")
reasons = raw_input("Why is that person a great role model? ")

question = raw_input("Wouldn't it be fun if we could do basic sentiment analysis on your mentor reflections? On why you think your mentor is great? ")

#If I was making this a more interesting program, I would:
#1) Implement regex to parse out Yes or No from the question.
#2) Do sentiment analysis on the reasons.

#Just a little fun with if/else.
if (question == "Yes") | (question == 'yes') | (question == 'y') | (question == 'Y'):
    print "This program can not do that at present. Feel free to let the developer know."
else:
    print "I guess you already know how highly you esteem your mentor, and do not need NLP to double check that for you."
