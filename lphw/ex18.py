#This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is pointless, we can just define how many parameters.
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#This is a one argument print function.
def print_one(arg1):
    print "arg1: %r" % arg1

#takes no arguments
def print_none():
    print "I got nothing."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
