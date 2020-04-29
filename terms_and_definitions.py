"""Quizzes user on terms and definitions."""

# import
import csv
import random
from collections import namedtuple

# return lambda for readability
RTN = lambda: '\n'


def correct_and_incorrect_answers(lst, answers):
    """Print list of incorrect answers."""
    if lst:
        print(answers.upper())
        for term in lst:
            print(term)
    else:
        pass
    print(RTN())


def open_csv_populate_dct():
    """Import a csv and populate a dictionary with its contents."""
    dct = {}
    with open('terms_and_definitions.csv') as f:
        F_CSV = csv.reader(f)
        ROW = namedtuple('Row', next(F_CSV))
        for r in F_CSV:
            row = ROW(*r)
            dct[row.term] = row.definition

    return dct


def output_results():
    """Calculate percentage answered correct and output results."""
    print('performance'.upper())
    PERCENTAGE_CORRECT = '{0:.0%}'.format(float(len(CORRECTS)) / \
                         float(TERMS_TOTAL))
    print(f'You defined {PERCENTAGE_CORRECT} of the terms you attempted '
          f'correctly.')
    print(RTN())


TERMS_AND_DEFINITIONS = open_csv_populate_dct()
TERMS_TOTAL = len(TERMS_AND_DEFINITIONS)

# create lists to be populated later
CORRECTS = []
INCORRECTS = []

# loop through laws and check user input against definition in laws dictionary
for term, definition in sorted(TERMS_AND_DEFINITIONS.items(),
                               key=lambda x: random.random()):
    user_prompt = term+ ': '
    user_answer = input(user_prompt)
    random.choice(list(TERMS_AND_DEFINITIONS))
    if user_answer == definition:
        print('correct')
        CORRECTS.append(term)
        print(RTN())
    else:
        print('work on that one')
        print(f'The correct answer is: {definition}')
        INCORRECTS.append(term)
        print(RTN())

# call functions
output_results()
correct_and_incorrect_answers(CORRECTS, 'correct answers')
correct_and_incorrect_answers(INCORRECTS, 'incorrect answers')
