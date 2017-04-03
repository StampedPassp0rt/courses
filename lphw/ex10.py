#Playing around with backslash to escape characters.

#Tabs in the string.
tabby_cat = "\tI'm tabbed in."
#new line
persian_cat = "I'm split\non a line."

#keeps the backslash.
backslash_cat = "I'm \\ a \\ cat."

#Silly way to do a list with last line. Easier on the eyes to not do the \n\t.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Not much that I can tell!
print "Hello world. What does \\a do? Let's see: \a Ta Ra Ra Bam Da Day."

#Inserted it into the string. Unreliable. Interpretted in the command line as a backspace, but not in Hydrogen (iPython powered).
print "Let's see what \\b does. Hello \bme."
