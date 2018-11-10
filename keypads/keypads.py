from keypadsTest import keypadsTest
"""
Create an OBJECT that acts as the backend of the minigame 'On the Subject of Keypads'.
Reference the word document for a translation from symbols to numbers.
Reference http://www.bombmanual.com/manual/1/pdf/Bomb-Defusal-Manual_1.pdf for the game rules.

It must contain the following functions:
generate - no arguments, returns a list of 4 numbers representing the given buttons
solve - 1 argument, a list of the order of buttons pressed based on their position in the list returned by 'generate',
        returns True or False depending on whether the order was correct

Example:
'generate' returns [7,2,5,4]
passing 'solve' [1,3,2,0] returns True
[1,3,2,0] implies you pressed the buttons in the order of 2,4,5,7

The tester will generate an output as is seen below:
C [7, 6, 1, 4]: [2, 3, 1, 0] -> Correct
C [8, 20, 26, 25]: [0, 3, 1, 2] -> Correct
I [21, 17, 23, 18]: [1, 0, 3, 2] -> Correct
C [11, 7, 1, 10]: [2, 1, 3, 0] -> Correct
I [7, 3, 2, 4]: [1, 2, 0, 3] -> Incorrect

C/I - Whether the tester will press the correct or incorrect buttons
[#,#,#,#]: - The keypad that you generated for the tester
[#,#,#,#] -> - The buttons the tester pressed (may be correct or incorrect based on C/I)
Correct/Incorrect - If you returned the proper result, eg. False for incorrect presses or True for correct presses
"""

# The line below can be changed to determine the number of tests the tester will preform
TESTS = 25


class keypadsSolution:

    def __init__(self):
        pass

    def generate(self):
        pass

    def solve(self, solution):
        pass






if __name__ == '__main__':
    s = keypadsSolution()
    keypadsTest(s,TESTS)