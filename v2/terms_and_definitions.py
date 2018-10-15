# import
import csv
from collections import namedtuple

# return lambda for readability
rtn = lambda : '\n'

# define function
def correct_and_incorrect_answers(a, b):
	if len(a) > 0:
		print(b.upper())
		for law in a:
			print(law)
	else:
		pass

# create dictionary to be populated by contents of csv
terms_and_definitions = {}

# import csv and turn the contents into a dictionary
with open('terms_and_definitions.csv') as f:
	f_csv = csv.reader(f)
	headings = next(f_csv)
	Row = namedtuple('Row', headings)
	terms_total = 0.0
	for r in f_csv:
		row = Row(*r)
		terms_and_definitions[row.term] = row.definition
		terms_total = terms_total + 1.0

# create lists to be populated later
corrects = []
incorrects = []

# loop through laws and check user input against definition in laws dictionary
for k, v in terms_and_definitions.iteritems():
	term = k+ ": "
	user_answer = raw_input(term)
	if user_answer == v:
		print("correct")
		corrects.append(k)
	else:
		print("work on that one")
		print("The correct answer is: %s") % (v)
		incorrects.append(k)

# return for readability
print(rtn())

print("performance".upper())
percentage_correct = float(len(corrects)) / float(terms_total)
print("You defined %s of the terms you attempted correctly.") % ("{0:.0%}".format(percentage_correct))

# return for readbility
print(rtn())

# call function
correct_and_incorrect_answers(corrects, "correct answers")

# return for readbility
print(rtn())

# call function
correct_and_incorrect_answers(incorrects, "incorrect answers")

# return for readbility
print(rtn())