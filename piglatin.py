#pig latin
def pigler(piglatin):
    scrimput = piglatin.lower()
    first_letter = scrimput[0]
    restofword = scrimput[1:]
    output = restofword + first_letter + "ay"
    word = output.lower()
    return str(word)

def pigger(sentence):
    words = sentence.split()
    output = ""
    for word in words:
        cry = pigler(word) + " "
        output = str(output) + cry
    return output


def start():
    print "Please input a word"
    word = raw_input()
    if len(word) > 0 and word.isalpha():
        print pigler(word)
        raw_input()
        print "Go again? 1 for yes, 2 for no, 3 for a sentence"
        goagain = raw_input()
        if goagain == "1":
            start()
        elif goagain == "2":
            exit(0)
        elif goagain == "3":
            print pigger(raw_input())
        else:
            raw_input("Try again")
            start()
    else:
        print "please try again"
        start()

start()

#pigger("This is a test")
