import unittest
import lazy_typist

__author__ = 'Rachelle Tanase'

class find_effort_greedy_tests(unittest.TestCase):
    '''Perform unit tests for the find_effort_greedy function'''
    def test_empty_string(self):
        self.assertEqual(
            lazy_typist.find_effort_greedy(""), 
            "Total effort: 0")

    def test_string_len_1(self):
        self.assertEqual(
            lazy_typist.find_effort_greedy("a"), 
            "A: Use left hand\nTotal effort: 0")

    def test_string_len_2(self):
        self.assertEqual(
            lazy_typist.find_effort_greedy("ab"),
            "A: Use left hand\nB: Use right hand\nTotal effort: 0")

    def test_upper_case_letter(self):
        self.assertEqual(
            lazy_typist.find_effort_greedy("T"), 
            "Shift: Use left hand\nT: Use right hand\nTotal effort: 0")

    def test_sample_string_1(self):
        self.assertEqual(
            lazy_typist.find_effort_greedy("The quick brown Fox"),
            "Shift: Use left hand\nT: Use right hand\nH: Move right hand from T (effort: 2)\nE: Move left hand from Shift (effort: 4)\nSpace: Move right hand from H (effort: 2)\nQ: Move left hand from E (effort: 2)\nU: Move right hand from Space (effort: 4)\nI: Move right hand from U (effort: 1)\nC: Move left hand from Q (effort: 5)\nK: Move right hand from I (effort: 1)\nSpace: Move left hand from C (effort: 1)\nB: Move left hand from Space (effort: 3)\nR: Move left hand from B (effort: 4)\nO: Move right hand from K (effort: 2)\nW: Move left hand from R (effort: 2)\nN: Move right hand from O (effort: 4)\nSpace: Move right hand from N (effort: 1)\nShift: Move left hand from W (effort: 3)\nF: Move right hand from Space (effort: 5)\nO: Move right hand from F (effort: 6)\nX: Move left hand from Shift (effort: 2)\nTotal effort: 54")

    def test_sample_string_2(self):
        self.assertEqual(
            lazy_typist.find_effort_greedy("hello world"),
            "H: Use left hand\nE: Use right hand\nL: Move left hand from H (effort: 3)\nL: Use left hand again\nO: Move left hand from L (effort: 1)\nSpace: Move left hand from O (effort: 4)\nW: Move right hand from E (effort: 1)\nO: Move left hand from Space (effort: 4)\nR: Move right hand from W (effort: 2)\nL: Move left hand from O (effort: 1)\nD: Move right hand from R (effort: 2)\nTotal effort: 18")

    def test_sample_string_3(self):
        self.assertEqual(
            lazy_typist.find_effort_greedy("qpalzm woskxn"),
            "Q: Use left hand\nP: Use right hand\nA: Move left hand from Q (effort: 1)\nL: Move right hand from P (effort: 2)\nZ: Move left hand from A (effort: 2)\nM: Move right hand from L (effort: 2)\nSpace: Move right hand from M (effort: 1)\nW: Move left hand from Z (effort: 2)\nO: Move right hand from Space (effort: 4)\nS: Move left hand from W (effort: 1)\nK: Move right hand from O (effort: 2)\nX: Move left hand from S (effort: 2)\nN: Move right hand from K (effort: 2)\nTotal effort: 21")

    def test_sample_string_4(self):
        self.assertEqual(
            lazy_typist.find_effort_greedy("Hello there DailyProgrammers"),
            "Shift: Use left hand\nH: Use right hand\nE: Move left hand from Shift (effort: 4)\nL: Move right hand from H (effort: 3)\nL: Use right hand again\nO: Move right hand from L (effort: 1)\nSpace: Move left hand from E (effort: 4)\nT: Move left hand from Space (effort: 4)\nH: Move left hand from T (effort: 2)\nE: Move left hand from H (effort: 4)\nR: Move left hand from E (effort: 1)\nE: Move left hand from R (effort: 1)\nSpace: Move left hand from E (effort: 4)\nShift: Move right hand from O (effort: 3)\nD: Move left hand from Space (effort: 3)\nA: Move left hand from D (effort: 2)\nI: Move right hand from Shift (effort: 4)\nL: Move right hand from I (effort: 2)\nY: Move right hand from L (effort: 4)\nShift: Move left hand from A (effort: 1)\nP: Move right hand from Y (effort: 4)\nR: Move left hand from Shift (effort: 5)\nO: Move right hand from P (effort: 1)\nG: Move left hand from R (effort: 2)\nR: Move left hand from G (effort: 2)\nA: Move left hand from R (effort: 4)\nM: Move right hand from O (effort: 3)\nM: Use right hand again\nE: Move left hand from A (effort: 3)\nR: Move left hand from E (effort: 1)\nS: Move left hand from R (effort: 3)\nTotal effort: 75")

    def test_sample_string_5(self):
        self.assertEqual(
            lazy_typist.find_effort_greedy("Ty"), 
            "Shift: Use left hand\nT: Use right hand\nY: Move right hand from T (effort: 1)\nTotal effort: 1")


class place_hands_tests(unittest.TestCase):
    '''Perform unit tests for the place_hands function'''
    def test_string_len_1_lower_case(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        r = []
        lazy_typist.place_hands("a", r, keyboard)
        self.assertEqual(r, ["A: Use left hand"])

    def test_string_len_1_upper_case(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        r = []
        lazy_typist.place_hands("A", r, keyboard)
        self.assertEqual(r, ["Shift: Use left hand", 
                             "A: Use right hand"])

    def test_string_len_2_lower_case(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        r = []
        lazy_typist.place_hands("ab", r, keyboard)
        self.assertEqual(r, ["A: Use left hand", 
                             "B: Use right hand"])


class find_char_pos_tests(unittest.TestCase):
    '''Perform unit tests for the find_char_pos function'''
    def test_shift(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        self.assertEqual(lazy_typist.find_char_pos('^', keyboard), (2, 0))

    def test_space(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        self.assertEqual(lazy_typist.find_char_pos('#', keyboard), (3, 3))

    def test_a(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        self.assertEqual(lazy_typist.find_char_pos('a', keyboard), (1, 0))

    def test_v(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        self.assertEqual(lazy_typist.find_char_pos('v', keyboard), (2, 4))

class find_dist_tests(unittest.TestCase):
    '''Perform unit tests for the find_dist function'''
    def test_same_coords(self):
        self.assertEqual(lazy_typist.find_dist((0, 0), (0, 0)), 0)

    def test_case_1(self):
        self.assertEqual(lazy_typist.find_dist((0, 0), (1, 1)), 2)

    def test_case_2(self):
        self.assertEqual(lazy_typist.find_dist((2, 3), (-6, -1)), 12)

class name_of_pos_tests(unittest.TestCase):
    '''Perform unit tests for the name_of_pos function'''
    def test_space(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        self.assertEqual(lazy_typist.name_of_pos((3, 3), keyboard), "Space")

    def test_shift(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        self.assertEqual(lazy_typist.name_of_pos((2, 0), keyboard), "Shift")

    def test_char(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        self.assertEqual(lazy_typist.name_of_pos((2, 6), keyboard), "N")

class find_best_dists_tests(unittest.TestCase):
    '''Perform unit tests for the find_best_dists function'''
    def test_1(self):
        lds, ls, rds, rs = lazy_typist.find_best_dists((0, 0), (3, 4), [(2, 0), (2, 9)])
        self.assertEqual(lds, 2)
        self.assertEqual(ls, (2, 0))
        self.assertEqual(rds, 5)
        self.assertEqual(rs, (2, 0))

    def test_2(self):
        lds, ls, rds, rs = lazy_typist.find_best_dists((2, 1), (1, 6), [(2, 0), (2, 9)])
        self.assertEqual(lds, 1)
        self.assertEqual(ls, (2, 0))
        self.assertEqual(rds, 4)
        self.assertEqual(rs, (2, 9))

    def test_3(self):
        lds, ls, rds, rs = lazy_typist.find_best_dists((3, 7), (1, 4), [(2, 0), (2, 9)])
        self.assertEqual(lds, 3)
        self.assertEqual(ls, (2, 9))
        self.assertEqual(rds, 5)
        self.assertEqual(rs, (2, 0))

class upper_case_handler_tests(unittest.TestCase):
    '''Perform unit tests for the upper_case_handler function'''
    def test_1(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        r = []
        effort = 0
        effort, r, lp, rp = lazy_typist.upper_case_handler('C', effort, keyboard, r, (0, 0), (0, 9))
        self.assertEqual(effort, 10)
        self.assertEqual(lp, (2, 0))
        self.assertEqual(rp, (2, 3))
        self.assertEqual(r, ["Shift: Move left hand from Q (effort: 2)",
                             "C: Move right hand from P (effort: 8)"])

    def test_2(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        r = []
        effort = 0
        effort, r, lp, rp = lazy_typist.upper_case_handler('A', effort, keyboard, r, (2 , 4), (1, 4))
        self.assertEqual(effort, 8)
        self.assertEqual(lp, (2, 0))
        self.assertEqual(rp, (1, 0))
        self.assertEqual(r, ["Shift: Move left hand from V (effort: 4)",
                             "A: Move right hand from G (effort: 4)"])

    def test_3(self):
        keyboard = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
                    ['^', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '^'],
                    ['-', '-', '-', '#', '#', '#', '#', '#', '-', '-']]
        r = []
        effort = 0
        effort, r, lp, rp = lazy_typist.upper_case_handler('B', effort, keyboard, r, (2, 2), (2, 8))
        self.assertEqual(effort, 4)
        self.assertEqual(lp, (2, 5))
        self.assertEqual(rp, (2, 9))
        self.assertEqual(r, ["Shift: Move right hand from - (effort: 1)",
                             "B: Move left hand from X (effort: 3)"])

class append_move_tests(unittest.TestCase):
    '''Perform unit tests for the append_move function'''
    def test_dist_not_zero(self):
        r = []
        r = lazy_typist.append_move(r, "left", "A", "B", 5)
        self.assertEqual(r, ["A: Move left hand from B (effort: 5)"])

    def test_dist_is_zero(self):
        r = []
        r = lazy_typist.append_move(r, "right", "A", "A", 0)
        self.assertEqual(r, ["A: Use right hand again"])

class mangle_name_tests(unittest.TestCase):
    '''Perform unit tests for the mangle_name function'''
    def test_shift(self):
        self.assertEqual(lazy_typist.mangle_name('^'), "Shift")

    def test_space(self):
        self.assertEqual(lazy_typist.mangle_name('#'), "Space")

    def test_letter(self):
        self.assertEqual(lazy_typist.mangle_name('z'), "Z")

def main():
    """Runs all test cases"""
    # Contains all names of test categories (classes) in string form
    test_class_names = ["find_effort_greedy_tests", "place_hands_tests", 
                        "find_char_pos_tests", "find_dist_tests", 
                        "name_of_pos_tests", "find_best_dists_tests",
                        "upper_case_handler_tests", "append_move_tests",
                        "mangle_name_tests"]
    # Contains all classes with test cases
    tests = [find_effort_greedy_tests, place_hands_tests, find_char_pos_tests,
             find_dist_tests, name_of_pos_tests, find_best_dists_tests,
             upper_case_handler_tests, append_move_tests, mangle_name_tests]
    # Parses through all test classes and and prints them out
    for index in range(0, len(tests)):
        print "\n\n###### Running {0} ######\n".format(test_class_names[index])
        suite = unittest.TestLoader().loadTestsFromTestCase(tests[index])
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()