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
    with open('csvs/terms_and_definitions.csv') as f:
        F_CSV = csv.reader(f)
        ROW = namedtuple('Row', next(F_CSV))
        for r in F_CSV:
            row = ROW(*r)
            dct[row.term] = row.definition

    return dct


def append_lst(lst):
    """Append result in response to term prompt to list."""
    lst.append(term)
    print(RTN())


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
print(RTN())
for term, definition in sorted(TERMS_AND_DEFINITIONS.items(),
                               key=lambda x: random.random()):
    print(term)
    user_answer = input('> ')
    random.choice(list(TERMS_AND_DEFINITIONS))
    if user_answer == definition:
        print('correct')
        append_lst(CORRECTS)
    else:
        print('work on that one')
        print(f'The correct answer is: {definition}')
        append_lst(INCORRECTS)

# call functions
output_results()
correct_and_incorrect_answers(CORRECTS, 'correct answers')
correct_and_incorrect_answers(INCORRECTS, 'incorrect answers')
