""" __doc__ """

# import
import csv
from collections import namedtuple

# return lambda for readability
RTN = lambda: '\n'

# define function
def correct_and_incorrect_answers(a, b):
    """ print list of incorrect answers """
    # if len(a) > 0:
    if a:
        print b.upper()
        for law in a:
            print law
    else:
        pass

# create dictionary to be populated by contents of csv
TERMS_AND_DEFINITIONS = {}

# import csv and turn the contents into a dictionary
with open('terms_and_definitions.csv') as f:
    F_CSV = csv.reader(f)
    HEADINGS = next(F_CSV)
    Row = namedtuple('Row', HEADINGS)
    TERMS_TOTAL = 0.0
    for r in F_CSV:
        row = Row(*r)
        TERMS_AND_DEFINITIONS[row.term] = row.definition
        TERMS_TOTAL = TERMS_TOTAL + 1.0

# create lists to be populated later
CORRECTS = []
INCORRECTS = []

# loop through laws and check user input against definition in laws dictionary
for k, v in TERMS_AND_DEFINITIONS.iteritems():
    term = k+ ": "
    user_answer = raw_input(term)
    if user_answer == v:
        print "correct"
        CORRECTS.append(k)
        print RTN()
    else:
        print "work on that one"
        print "The correct answer is: %s" % (v)
        INCORRECTS.append(k)
        print RTN()

# return for readability
print RTN()

print "performance".upper()
PERCENTAGE_CORRECT = float(len(CORRECTS)) / float(TERMS_TOTAL)
print "You defined %s of the terms you attempted correctly." % ("{0:.0%}".
                                                                format(PERCENTAGE_CORRECT))

# return for readbility
print RTN()

# call function
correct_and_incorrect_answers(CORRECTS, "correct answers")

# return for readbility
print RTN()

# call function
correct_and_incorrect_answers(INCORRECTS, "incorrect answers")

# return for readbility
print RTN()
