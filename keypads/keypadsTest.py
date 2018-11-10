from random import sample, random
answers = [0,1,2,3]
symbols = [[1,2,3,4,5,6,7],[8,1,7,9,10,6,11],[12,13,9,14,15,3,10],[16,17,18,5,14,11,19],[20,19,18,21,17,22,23],[16,8,24,25,20,26,27]]

def _keypadsTest(keypad, testBool):
    pad = keypad.generate()
    tgt = False

    print('C ', end='') if testBool else print('I ', end='')
    print(pad,end=': ')

    # Ensure no duplicate values
    if len(set(pad)) != len(pad):
        print('Given Pad Contains Duplicates')
        return False

    # Find the proper solution column
    for i in symbols:
        correct = set(pad).issubset(i)
        if correct:
            # Ensures a solution column has not already been found
            if not tgt:
                tgt = i
            else:
                print('Given Pad Matches Multiple Solutions')
                return False

    # Ensures a solution column exists
    if tgt == -1:
        print('Unsolvable Pad')
        return False

    # Find the solution
    solution = []
    for i in tgt:
        if i in pad:
            solution.append(pad.index(i))

    # Find an incorrect solution
    incorrect = solution
    while incorrect == solution:
        incorrect = sample(answers,4)

    # Test the asked for solution
    if testBool:
        print(solution,end=' -> ')
        if keypad.solve(solution) == True:
            print('Correct')
            return True
        else:
            print('Incorrect')
            return False

    # Test the incorrect solution
    else:
        print(incorrect,end=' -> ')
        if keypad.solve(incorrect) == False:
            print('Correct')
            return True
        else:
            print('Incorrect')
            return False



def keypadsTest(keypad,tests):
    correct = 0
    corCount = 0
    incorrect = 0
    incCount = 0
    for i in range(tests):
        # Choose a good or bad guess
        guess = True if random() >= 0.5 else False
        if guess:
            corCount += 1
        else:
            incCount += 1

        # Check the solution
        if _keypadsTest(keypad,guess):
            if guess:
                correct += 1
            else:
                incorrect += 1

    print('\n\n')
    print(str(incorrect) + '/' + str(incCount) + ' Incorrect Answers Solved Correctly')
    print(str(correct) + '/' + str(corCount) + ' Correct Answers Solved Correctly')
    print('\nSolution Accuracy: ' + str(round((correct+incorrect)/(incCount+corCount),4)*100) + '%')