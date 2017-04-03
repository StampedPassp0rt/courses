name = "Zed A. Shaw"
age = 35
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

inches_to_cm = 2.54
lbs_to_kg = 0.453592

height_cm = inches_to_cm*height
weight_kg = weight * lbs_to_kg


print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "In metric, he's %.2f cm tall." % height_cm
print "In metric, he's %.2f kg heavy." % weight_kg
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d, I get %d, which is a number so fraught with \
meaningless as to be peak Python comedy." % (age, height, weight, age + height + weight)
