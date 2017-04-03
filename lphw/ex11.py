#Simple input output exercise.

print "How old are you?"
age = raw_input()
print "How tall are you? Please enter in feet and inch nomenclature, or metric nomenclature."
height = raw_input()
print "How much do you weigh? Please note whether lbs or kg. I.e. 145 lbs."
weight = raw_input()

print "So you're %r years old, %r tall, and %r heavy." % (age, height, weight)
