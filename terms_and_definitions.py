"""Quizzes user on terms and definitions."""

import csv
import random
from collections import namedtuple

RTN = lambda: '\n'


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
    """Count correct answers."""
    lst = []
    for i in results:
        if i[1] == 'correct':
            lst.append('correct')
        else:
            pass

    return lst


def calc_perc(correct_answers, total):
    """Calculate percentage of correct answers."""
    perc = len(correct_answers) / total * 100
    perc_correct = '{0:.2f}%'.format(perc)
    print(f'percent correct: {perc_correct}\n')


TERMS_AND_DEFINITIONS = open_csv_populate_dct()
TERMS_TOTAL = len(TERMS_AND_DEFINITIONS)
results = quiz_user()
corrects = count_results()
calc_perc(corrects, TERMS_TOTAL)
