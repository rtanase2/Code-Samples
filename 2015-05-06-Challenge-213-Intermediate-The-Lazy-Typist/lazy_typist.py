__author__ = 'Rachelle Tanase'

def find_effort_greedy(s):
    """Return the moves and total effort for tying the string, s."""
    total_effort = 0
    if len(s) == 0:
        return "Total effort: 0"

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