""" __doc__ """

# import
import csv
import random
from collections import namedtuple

# return lambda for readability
RTN = lambda: "\n"

# define function
def correct_and_incorrect_answers(lst, answers):
    """ print list of incorrect answers """
    if lst:
        print(answers.upper())
        for term in lst:
            print(term)
    else:
        pass
    print(RTN())


# create dictionary to be populated by contents of csv
TERMS_AND_DEFINITIONS = {}

with open('terms_and_definitions.csv') as f:
    F_CSV = csv.reader(f)
    ROW = namedtuple('Row', next(F_CSV))
    for r in F_CSV:
        row = ROW(*r)
        TERMS_AND_DEFINITIONS[row.term] = row.definition

TERMS_TOTAL = len(TERMS_AND_DEFINITIONS)

# create lists to be populated later
CORRECTS = []
INCORRECTS = []

# loop through laws and check user input against definition in laws dictionary
for k, v in sorted(TERMS_AND_DEFINITIONS.items(),
                   key=lambda x: random.random()):
    prompt = k+ ": "
    user_answer = input(prompt)
    random.choice(list(TERMS_AND_DEFINITIONS))
    if user_answer == v:
        print("correct")
        CORRECTS.append(k)
        print(RTN())
    else:
        print("work on that one")
        print(f"The correct answer is: {v}") # % (v)
        INCORRECTS.append(k)
        print(RTN())

print("performance".upper())
print(RTN())
PERCENTAGE_CORRECT = "{0:.0%}".format(float(len(CORRECTS)) / float(TERMS_TOTAL))
print(f"You defined {PERCENTAGE_CORRECT} of the terms you attempted correctly.")
print(RTN())

# call function
correct_and_incorrect_answers(CORRECTS, "correct answers")
correct_and_incorrect_answers(INCORRECTS, "incorrect answers")
