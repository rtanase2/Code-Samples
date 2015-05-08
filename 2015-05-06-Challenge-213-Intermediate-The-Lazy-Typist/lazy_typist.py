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
        for c in s[start:len(s)]:
            # If it is upper, you need to use both hands
            if(c.isupper()):
                total_effort, result, left_pos, right_pos = upper_case_handler(c, total_effort, keyboard, result, left_pos, right_pos)
            # Else, you just need to move one hand
            else:
                char_pos = find_char_pos(c.upper(), keyboard)
                right_dist = find_dist(right_pos, char_pos)
                left_dist = find_dist(left_pos, char_pos)
                if (min(right_dist, left_dist) == right_dist):
                    result.append("{0}: Move right hand from {1} (effort: {2})"
                        .format(c.upper(), keyboard[right_pos[0]][right_pos[1]],
                            right_dist))
                    right_pos = char_pos
                    total_effort += right_dist
                else:
                    result.append("{0}: Move left hand from {1} (effort: {2})"
                        .format(c.upper(), keyboard[left_pos[0]][left_pos[1]],
                            left_dist))
                    left_pos = char_pos
                    total_effort += left_dist
        result.append("Total effort: {0}".format(total_effort, keyboard))
        return "\n".join(result)

def find_shift_dists(left_pos, right_pos):
    shift_positions = [(2, 0), (2, 9)]
    left_dist_to_shift = 99
    right_dist_to_shift = 99
    left_shift = (0, 0)
    right_shift = (0, 0)
    for shift_pos in shift_positions:
        left_dist = find_dist(left_pos, shift_pos)
        right_dist = find_dist(right_pos, shift_pos)
        if left_dist < left_dist_to_shift:
            left_dist_to_shift = left_dist
            left_shift = shift_pos
        if right_dist < right_dist_to_shift:
            right_dist_to_shift = right_dist
            right_shift = shift_pos
    return left_dist_to_shift, left_shift, right_dist_to_shift, right_shift

def upper_case_handler(c, total_effort, keyboard, result, left_pos, right_pos):
    left_dist_to_shift, left_shift, right_dist_to_shift, right_shift = find_shift_dists(left_pos, right_pos)
    if (min (left_dist_to_shift, right_dist_to_shift) == left_dist_to_shift):
        # Move left hand to shift and move right to letter
        result.append("Shift: Move left hand from {0} (effort: {1})"
            .format(name_of_pos(left_pos, keyboard), 
                left_dist_to_shift))
        left_pos = left_shift
        total_effort += left_dist_to_shift
        result.append("{0}: Move right hand from {1} (effort: {2})"
            .format(c.upper(), name_of_pos(right_pos, keyboard), 
                find_dist(right_pos, find_char_pos(c.upper(), keyboard))))
        total_effort += find_dist(right_pos, find_char_pos(c.upper(), keyboard))
        right_pos = find_char_pos(c.upper(), keyboard)
    else:
        # Move right hand to shift and move left hand to letter
        result.append("Shift: Move right hand from {0} (effort: {1})"
            .format(name_of_pos(right_pos, keyboard), 
                right_dist_to_shift))
        right_pos = right_shift
        total_effort += right_dist_to_shift
        result.append("{0}: Move left hand from {1} (effort: {2})"
            .format(c.upper(), name_of_pos(left_pos, keyboard), 
                find_dist(left_pos, find_char_pos(c.upper(), keyboard))))
        total_effort += find_dist(left_pos, find_char_pos(c.upper(), keyboard))
        left_pos = find_char_pos(c.upper(), keyboard)
    return total_effort, result, left_pos, right_pos

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