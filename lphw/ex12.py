#Exercise 12, which is Exercise 11, rewritten with prompts in raw input.

age = int(raw_input("What is your age in years? "))
height = raw_input("What is your height in feet and inches? ")
weight = raw_input("What is your weight in lbs? ")

print """So you're %r years old, %r tall, and %r lbs heavy. \n
We could say more, but we're not a medical app, just a fun test object.
But wouldn't it be fun if we knew how to quantify your health and give you
insight from your health metrics?""" % (age, height, weight)
