##(Intermediate): The Lazy Typist##
We've all had a night where we're so lazy that we actively avoid moving our hands around on the keyboard. In today's challenge, we'll be given a sentence to type, and we'll work out a minimal-effort way of typing that string (ie. minimize how much the hand moves), using a basic QWERTY keyboard layout - the keys supported are the letters A to Z, shift, and space - in this arrangement:
```
qwertyuiop
asdfghjkl
^zxcvbnm^
   ##### 
```
The only letters that can be typed are upper-case and lower-case letters, and space. Our typist is quite inefficient: they move their fingers around the keyboard, hunting for keys one by one, so the user only uses one finger of each hand.
The user may start with both hands on any key, and may move either hand to the next key. The main important things to remember are:
The user may move to any of the five # (space) positions to type a space.
Two hands are required to type a capital letter - one must go to a shift key. Which hand goes to which key is up to your program to decide, but the same hand can't press both the shift key and the letter.
As a score of laziness, you'll also need to work out the total Manhattan distance (x + y) moved by the hands. We'll call this total distance the effort.

##Formal Inputs and Outputs##
###Input Description###
Enter a sentence, consisting of only upper-case, lower-case and spaces, like so:
```
The quick brown Fox
```
###Output Description###
Display all the key presses, along with the hand that presses the key, and the distance that the hand moves, for example:
```
Shift: Use left hand
T: Use right hand
H: Move right hand from T (effort: 2)
E: Move left hand from Shift (effort: 4)
Space: Move right hand from H (effort: 2)
Q: Move left hand from E (effort: 2)
U: Move right hand from Space (effort: 4)
I: Move right hand from U (effort: 1)
C: Move left hand from Q (effort: 5)
K: Move right hand from I (effort: 1)
Space: Move left hand from C (effort: 1)
B: Move left hand from Space (effort: 3)
R: Move left hand from B (effort: 4)
O: Move right hand from K (effort: 2)
W: Move left hand from R (effort: 2)
N: Move right hand from O (effort: 4)
Space: Move right hand from N (effort: 1)
Shift: Move left hand from W (effort: 3)
F: Move right hand from Space (effort: 5)
O: Move right hand from F (effort: 6)
X: Move left hand from Shift (effort: 2)
```
Finally, display the total effort:
```
Total effort: 54
```
You may be able to find a more efficient way of doing this - you only need to find a heuristic solution. If a hand is already over the key which it needs to press, the distance and effort is (obviously) zero. Shift: Use left hand Q: Use right hand Shift: Use left hand again P: Move right hand from Q (effort: 9) G: Move left hand from Shift (effort: 5) I: Move right hand from P (effort: 2) Z: Move left hand from G (effort: 4) M: Move right hand from I (effort: 2) Space: Move right hand from M (effort: 1) Shift: Move left hand from Z (effort: 1) Q: Move right hand from Space (effort: 10) Shift: Use left hand again F: Move right hand from Q (effort: 4) P: Move right hand from F (effort: 7) Shift: Use left hand again R: Move right hand from P (effort: 6) Shift: Use left hand again K: Move right hand from R (effort: 5) B: Move right hand from K (effort: 3) I: Move right hand from B (effort: 4) Space: Move right hand from I (effort: 3) Shift: Use left hand again Q: Move right hand from Space (effort: 10) Y: Move right hand from Q (effort: 5) C: Move left hand from Shift (effort: 3) N: Move left hand from C (effort: 3) Total effort: 87
