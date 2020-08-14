def say(word, n):
    if n > 1:
        say(word, n-1)
    print("{} - {}".format(word, n))


say("goodbye fubar", 5)
