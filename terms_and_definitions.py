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


# loop through laws and check user input against definition in laws dictionary
def quiz_user():
    """Quiz user."""
    lst = []
    print(RTN())
    for term, definition in sorted(TERMS_AND_DEFINITIONS.items(),
                                   key=lambda x: random.random()):
        print(term)
        user_answer = input('> ')
        random.choice(list(TERMS_AND_DEFINITIONS))
        if user_answer == definition:
            print('correct')
            lst.append((term, 'correct'))
            print(RTN())
        else:
            print('work on that one')
            print(f'The correct answer is: {definition}')
            lst.append((term, 'incorrect'))
            print(RTN())

    return lst


def count_results():
    """Count corrects."""
    lst = []
    for i in results:
        if i[1] == 'correct':
            lst.append('correct')
        else:
            pass

    return lst


def calc_perc(a, b):
    """ __doc__ """
    perc = len(a) / b
    perc_correct = '{0:.2f}%'.format(perc)
    print(f'percent correct: {perc_correct}')
    print(RTN())


TERMS_AND_DEFINITIONS = open_csv_populate_dct()
TERMS_TOTAL = len(TERMS_AND_DEFINITIONS)
results = quiz_user()
corrects = count_results()
calc_perc(corrects, TERMS_TOTAL)
