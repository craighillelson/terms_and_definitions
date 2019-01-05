""" __doc__ """

# imports
import csv
import random

# define lambda
RTN = lambda: '\n'

# create lists to be populated later
TERMS = []
DEFINITIONS = []
CORRECTS = []
INCORRECTS = []

# import a csv with terms and definitions and populate lists of terms and definitions
with open('terms_and_definitions.csv') as f:
    F_CSV = csv.DictReader(f)
    for row in F_CSV:
        TERMS.append(row['term'])
        DEFINITIONS.append(row['definition'])

NUMBER_TO_DRILL = int(raw_input("How many terms would you like to drill? "))
RANDOM_NUMBERS = random.sample(range(0, len(TERMS)), NUMBER_TO_DRILL)

# for readability
print RTN()

# loop through terms, quiz user, and add correct and incorrect answers to respective lists
for i in RANDOM_NUMBERS:
    print RTN()
    prompt = "Term: %s\nDefinition: " % (TERMS[i])
    user_answer = raw_input(prompt)
    if user_answer == DEFINITIONS[i]:
        print "Correct!"
        CORRECTS.append(TERMS[i])
    else:
        print "Incorrect"
        print "%s"  % (DEFINITIONS[i])
        INCORRECTS.append(TERMS[i])

# update user on their performance
# get length of each set of answers
NUM_CORRECT = len(CORRECTS)
NUM_INCONNECT = len(INCORRECTS)

print RTN()

PERCENTAGE_CORRECT = float(len(CORRECTS)) / float(len(RANDOM_NUMBERS))
print "You defined %s of the terms you attempted correctly." % ("{0:.0%}".format
                                                                (PERCENTAGE_CORRECT))

print RTN()

print "%s %s" % ("Correct Answers:", NUM_CORRECT)
for correct in CORRECTS:
    print correct

print RTN()

print "%s %s" % ("Incorrect Answers:", NUM_INCONNECT)
print "Review the following:"
for incorrect in INCORRECTS:
    print incorrect

print RTN()
