import unittest
from lazy_typist import find_effort_greedy

__author__ = 'Rachelle Tanase'

class find_effort_tests(unittest.TestCase):
    '''Perform unit tests for the find_effort_greedy function'''
    def testEmptyString(self):
        self.assertEqual(
            find_effort_greedy(""), 
            "Total effort: 0")

    def testStringLen1(self):
        self.assertEqual(
            find_effort_greedy("a"), 
            "A: Use left hand\n\
            Total effort: 0")

    def testStringLen2(self):
        self.assertEqual(
            find_effort_greedy("ab"),
            "A: Use left hand\n\
            B: Use right hand\n\
            Total effort: 0")

    def testUpperCaseLetter(self):
        self.assertEqual(
            find_effort_greedy("T"), 
            "Shift: Use left hand\n\
            T: Use right hand\n\
            Total effort: 0")

    def testRegString1(self):
        self.assertEqual(
            find_effort_greedy("The quick brown Fox"),
            "Shift: Use left hand\n\
            T: Use right hand\n\
            H: Move right hand from T (effort: 2)\n\
            E: Move left hand from Shift (effort: 4)\n\
            Space: Move right hand from H (effort: 2)\n\
            Q: Move left hand from E (effort: 2)\n\
            U: Move right hand from Space (effort: 4)\n\
            I: Move right hand from U (effort: 1)\n\
            C: Move left hand from Q (effort: 5)\n\
            K: Move right hand from I (effort: 1)\n\
            Space: Move left hand from C (effort: 1)\n\
            B: Move left hand from Space (effort: 3)\n\
            R: Move left hand from B (effort: 4)\n\
            O: Move right hand from K (effort: 2)\n\
            W: Move left hand from R (effort: 2)\n\
            N: Move right hand from O (effort: 4)\n\
            Space: Move right hand from N (effort: 1)\n\
            Shift: Move left hand from W (effort: 3)\n\
            F: Move right hand from Space (effort: 5)\n\
            O: Move right hand from F (effort: 6)\n\
            X: Move left hand from Shift (effort: 2)\n\
            Total effort: 54")

    def testRegString2(self):
        self.assertEqual(
            find_effort_greedy("hello world"),
            "H: Use left hand\n\
            E: Use right hand\n\
            L: Move left hand from H (effort: 3)\n\
            L: Use left hand again\n\
            O: Move left hand from L (effort: 1)\n\
            Space: Move left hand from O (effort: 4)\n\
            W: Move right hand from E (effort: 1)\n\
            O: Move left hand from Space (effort: 4)\n\
            R: Move right hand from W (effort: 2)\n\
            L: Move left hand from O (effort: 1)\n\
            D: Move right hand from R (effort: 2)\n\
            Total effort: 18")

    def testRegString3(self):
        self.assertEqual(
            find_effort_greedy("qpalzm woskxn"),
            "Q: Use left hand\n\
            P: Use right hand\n\
            A: Move left hand from Q (effort: 1)\n\
            L: Move right hand from P (effort: 2)\n\
            Z: Move left hand from A (effort: 2)\n\
            M: Move right hand from L (effort: 2)\n\
            Space: Move right hand from M (effort: 1)\n\
            W: Move left hand from Z (effort: 2)\n\
            O: Move right hand from Space (effort: 4)\n\
            S: Move left hand from W (effort: 1)\n\
            K: Move right hand from O (effort: 2)\n\
            X: Move left hand from S (effort: 2)\n\
            N: Move right hand from K (effort: 2)\n\
            Total effort: 21")

    def testRegString4(self):
        self.assertEqual(
            find_effort_greedy("Hello there DailyProgrammers"),
            "Shift: Use left hand\n\
            H: Use right hand\n\
            E: Move left hand from Shift (effort: 4)\n\
            L: Move right hand from H (effort: 3)\n\
            L: Use right hand again\n\
            O: Move right hand from L (effort: 1)\n\
            Space: Move left hand from E (effort: 4)\n\
            T: Move left hand from Space (effort: 4)\n\
            H: Move left hand from T (effort: 2)\n\
            E: Move left hand from H (effort: 4)\n\
            R: Move left hand from E (effort: 1)\n\
            E: Move left hand from R (effort: 1)\n\
            Space: Move left hand from E (effort: 4)\n\
            Shift: Move right hand from O (effort: 3)\n\
            D: Move left hand from Space (effort: 3)\n\
            A: Move left hand from D (effort: 2)\n\
            I: Move right hand from Shift (effort: 4)\n\
            L: Move right hand from I (effort: 2)\n\
            Y: Move right hand from L (effort: 4)\n\
            Shift: Move left hand from A (effort: 1)\n\
            P: Move right hand from Y (effort: 4)\n\
            R: Move left hand from Shift (effort: 5)\n\
            O: Move right hand from P (effort: 1)\n\
            G: Move left hand from R (effort: 2)\n\
            R: Move left hand from G (effort: 2)\n\
            A: Move left hand from R (effort: 4)\n\
            M: Move right hand from O (effort: 3)\n\
            M: Use right hand again\n\
            E: Move left hand from A (effort: 3)\n\
            R: Move left hand from E (effort: 1)\n\
            S: Move left hand from R (effort: 3)\n\
            Total effort: 75")

    def testRegString5(self):
        self.assertEqual(
            find_effort_greedy("Ty"), 
            "Shift: Use left hand\n\
            T: Use right hand\n\
            Y: Move right hand from T (effort: 1)\n\
            Total effort: 1")

def main():
    unittest.main()

if __name__ == '__main__':
    main()