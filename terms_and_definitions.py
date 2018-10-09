# import
import csv

rtn = lambda : '\n'
print(rtn())

# create lists to be populated later
terms = []
definitions = []
corrects = []
incorrects = []

# import a csv with terms and definitions and populate lists of terms and definitions
with open('terms.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		terms.append(row['term'])
		definitions.append(row['definition'])

# set i to 0
i = 0

# loop through terms, quiz user, and add correct and incorrect answers to respective lists
for term in terms:
	print(rtn())
	prompt = "Term: %s\nDefinition: " % (terms[i])
	user_answer = raw_input(prompt) 
	if user_answer == definitions[i]:
		print("Correct!")
		corrects.append(terms[i])
	else:
		print("Incorrect")
		print("%s") % (definitions[i])
		incorrects.append(terms[i])
	i = i + 1

# get length of each set of answers
num_correct = len(corrects)
num_inconnect = len(incorrects)

print(rtn())

# update user on their performance
print("%s %s") % ("Correct Answers:", num_correct)
for correct in corrects:
	print(correct)

print(rtn())

print("%s %s") % ("Incorrect Answers:", num_inconnect)
for incorrect in incorrects:
	print(incorrect)

print(rtn())