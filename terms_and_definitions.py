# import
import csv

# define function
def print_return():
	print("\n")

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
	print_return()
	prompt = "Term: %s\nDefinition: " % (terms[i])
	user_answer = raw_input(prompt) 
	if user_answer == definitions[i]:
		print("Correct!")
		corrects.append(terms[i])
	else:
		print("Incorrect")
		incorrects.append(terms[i])
	i = i + 1

# get length of each set of answers
num_correct = len(corrects)
num_inconnect = len(incorrects)

print_return()

# update user on their performance
print("%s %s") % ("Correct Answers:", num_correct)
for correct in corrects:
	print(correct)

print_return()

print("%s %s") % ("Incorrect Answers:", num_inconnect)
for incorrect in incorrects:
	print(incorrect)

print_return()