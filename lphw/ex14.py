from sys import argv

script, user_name = argv

prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script) #Funny, that's how all the chatbots start to flirt.

print "I'd like to ask you a few questions."

print "Do you like me %s?" % user_name

likes = raw_input(prompt)

print "Where do you live %s" % user_name

lives = raw_input(prompt)

print "What type of computer do you have?"
computer = raw_input(prompt)

print """
Alright. So you said %r about liking me. Fair enough, since I'm not even a chatbot yet.
You live in %r. Not an intelligent chatbot, so no clue where that is.
And you have a %r computer. Good on you.""" % (likes, lives, computer)
