#pig latin
def pigler(piglatin):
    scrimput = piglatin.lower()
    first_letter = scrimput[0]
    restofword = scrimput[1:]
    output = restofword + first_letter + "ay"
    print output.lower()
    raw_input()
    print "Go again? 1 for yes, 2 for no"
    goagain = raw_input()
    if goagain == "1":
        start()
    elif goagain == "2":
        exit(0)
    else:
        print "ninja turds"
        raw_input()
        start()

def start():
    print "Please input a word"
    word = raw_input()
    if len(word) > 0 and word.isalpha():
    #    print "ok"
        pigler(word)
    else:
        print "please try again"
        start()

start()
