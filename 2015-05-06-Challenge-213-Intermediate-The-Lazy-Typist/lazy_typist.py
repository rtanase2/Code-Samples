__author__ = 'Rachelle Tanase'

def find_effort_greedy(s):
    """Return the moves and total effort for tying the string, s.
    
    Keyword arguments:
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
        shift_positions = [(2, 0), (2, 9)]
        for c in s[start:len(s)]:
            if(c.isupper()):
                left_dist_to_shift = 999999999999
                right_dist_to_shift = 999999999999
                for shift_pos in shift_positions:
                    left_dist = find_dist(left_pos, shift_pos)
                    right_dist = find_dist(right_pos, shift_pos)
                    if left_dist < left_dist_to_shift:
                        left_dist_to_shift = left_dist
                    if right_dist < right_dist_to_shift:
                        right_dist_to_shift = right_dist
                if (min (left_dist_to_shift, right_dist_to_shift) == left_dist_to_shift):
                    # Move left hand to shift and move right to letter
                    result.append("Shift: Move left hand from {0}".format(name_of_pos(left_pos, keyboard)))
                else:
                    # Move right hand to shift and move left hand to letter
                    pass
            else:
                pass
        result.append("Total effort: {0}".format(total_effort))
        return "\n".join(result)

def place_hands(s, r, kb):
    """Places hands in first position"""
    if (s[0].isupper()):
        r.append("Shift: Use left hand")
        r.append("{0}: Use right hand".format(s[0].upper()))
        return 1, (2, 0), find_char_pos(s[0], kb)
    elif (len(s) == 1):
        r.append("{0}: Use left hand".format(s[0].upper()))
        return 1, (0, 0), (0, 0)
    else:
        r.append("{0}: Use left hand".format(s[0].upper()))
        r.append("{0}: Use right hand".format(s[1].upper()))
        return 2, find_char_pos(s[0], kb), find_char_pos(s[1], kb)

def find_char_pos(c, kb):
    """Find returns tuple with hand position, given hand is over c on kb"""
    c = c.upper()
    for x in range(0, len(kb)):
        if c in kb[x]:
            return (x, kb[x].index(c))

def find_dist(coords1, coords2):
    """Returns the Manhattan distance between coords1 and coords2

    Keyword arguments:
    coords1 -- Tuple of starting position
    coords2 -- Tuple of ending position

    Precondition:
    Assert coords1 and coords2 are tuples

    Extra Info:
    Manhattan distance = abs(x1 - x2) + abs(y1 - y2)
    """
    x_diff = abs(coords1[0] - coords2[0])
    y_diff = abs(coords1[1] - coords2[1])
    return (x_diff + y_diff)

def name_of_pos(coord, kb):
    """Returns the correct name for the position of coord on kb, 
    especially for space and shift.
    """
    coord_char = kb[coord[0]][coord[1]]
    if coord_char == '^':
        return "Shift"
    elif coord_char == '#':
        return "Space"
    else:
        return coord_char

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