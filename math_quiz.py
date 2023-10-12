# Import Statements
import random

def main():
    """
    The variables for the numbers we are multiplying are set to be a random integer from 0
    to 99 for the first and 0 to 9 for the second. This sets up the functions and their
    variables while also establishing how the solution will be calculated.
    """
    multiplicand = random.randint(0,99)
    multiplier = random.randint(0,9)

    display_problem(multiplicand, multiplier)
    solution = multiplicand * multiplier
    student_reply = get_answer()
    show_result(solution, student_reply)

def display_problem(multiplicand, multiplier):
    """
    This is the string formatting for the math problem. It calls the
    multiplicand and multiplier variables so that the random integers are displayed, as well
    as the unicode for the multiplication symbol.
    """
    print(f'\t\t {multiplicand:}')
    print(f'\t\t\u02df {multiplier:}')
    print('\t\t---')

def get_answer():
    """
    This function will prompt the student (user) to input an integer and then returns it.
    """
    student_reply = int(input('Enter product:  '))
    return student_reply

def show_result(solution, student_reply):
    """
    This function will see whether the user's integer is the same as the calculated solution
    for the generated math problem. If it is, it will congratulate the "student." If not,
    it will inform the user that they were incorrect and then print the solution.
    """
    if solution == student_reply:
        print('\nCorrect answer - Good Work!')
    else:
        print(f'Incorrect. The correct answer is: {solution}')


# Call the main function.  If this isn't in the file, the code won't run.
if __name__ == '__main__':
    main()
