def say(word, n):
    if n > 0:
        say(word, n-1)
    print("{} - {}".format(word, n))


say("goodbye", 5)
