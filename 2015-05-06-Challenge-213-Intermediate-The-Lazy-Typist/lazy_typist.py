__author__ = 'Rachelle Tanase'

def find_effort_greedy(s):
    """Return the moves and total effort for tying the string, s.
    
    Keyword arguements:
    s -- string to type

    Precondition:
    Assert s is a string
    """
    if len(s) == 0:
        return "Total effort: 0"
    else:
        result = []
        total_effort = 0
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        start, left_pos, right_pos = place_hands(s, result, keyboard)
        for c in s[start:len(s)]:
            if(c.isupper()):
                pass
        result.append("Total effort: {0}".format(total_effort))
        return "\n".join(result)

def place_hands(s, r, kb):
    """Places hands in first position"""
    if (s[0].isupper()):
        r.append("Shift: Use left hand")
        r.append("{0}: Use right hand".format(s[0].upper()))
        return 1, (2, 0), find_hand_pos(s[0], kb)
    elif (len(s) == 1):
        r.append("{0}: Use left hand".format(s[0].upper()))
        return 1, (0, 0), (0, 0)
    else:
        r.append("{0}: Use left hand".format(s[0].upper()))
        r.append("{0}: Use right hand".format(s[1].upper()))
        return 2, find_hand_pos(s[0], kb), find_hand_pos(s[1], kb)

def find_hand_pos(c, kb):
    """Find returns tuple with hand position, given hand is over c on kb"""
    c = c.upper()
    for x in range(0, len(kb)):
        if c in kb[x]:
            return (x, kb[x].index(c))

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