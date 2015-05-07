__author__ = 'Rachelle Tanase'

def find_effort_greedy(s):
    """Return the moves and total effort for tying the string, s."""
    if len(s) == 0:
        return "Total effort: 0"
    else:
        result = []
        total_effort = 0
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        for c in s[placeHands(s, result):len(s)]:
            if(c.isupper()):
                nextChars = [c, "^"]
        result.append("Total effort: {0}".format(total_effort))
        return "\n".join(result)

def placeHands(s, r):
    """Places hands in first position"""
    if (s[0].isupper()):
        r.append("Shift: Use left hand")
        r.append("{0}: Use right hand".format(s[0].upper()))
        return 1
    elif (len(s) == 1):
        r.append("{0}: Use left hand".format(s[0].upper()))
        return 1
    else:
        r.append("{0}: Use left hand".format(s[0].upper()))
        r.append("{0}: Use right hand".format(s[1].upper()))
        return 2


def main():
    """Takes in user iput and returns the moves and total effort for each."""
    print ("Welcome to my Lazy Typist simulator!\n" + 
           "You can exit at any time by typing \"quit\".")
    while (True):
        s = raw_input("Please enter the string to type: ")
        if (s == "quit"):
            break
        print "The lazy way to type \"{0}\" using a greedy algorithm is:\n{1}"\
              .format(s, find_effort_greedy(s))


if __name__ == '__main__':
    main()