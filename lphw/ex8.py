#Exercise 8

#variable that force prints four inputs with %r, kind of a debugger too.
formatter = "%r %r %r %r"

#printing out 1 through 4
print formatter % (1,2,3,4)
#printing out one through four as strings.
print formatter % ("one", "two", "three", "four")
#forcing the print of Boolean values
print formatter % (True, False, True, False)

# Will just print the string with the %r's.
print formatter % (formatter, formatter, formatter, formatter)

print formatter % ("I had this thing.", "That you could type up right.",\
"But it didn't sing.", "So I said goodnight.")
