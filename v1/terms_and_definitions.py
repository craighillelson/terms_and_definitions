# imports
import csv
import random

# define lambda
rtn = lambda : '\n'

# create lists to be populated later
terms = []
definitions = []
corrects = []
incorrects = []

# import a csv with terms and definitions and populate lists of terms and definitions
with open('terms_and_definitions.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		terms.append(row['term'])
		definitions.append(row['definition'])

number_to_drill = int(raw_input("How many terms would you like to drill? "))
random_numbers = random.sample(range(0, len(terms)), number_to_drill)

# for readability
print(rtn())

# loop through terms, quiz user, and add correct and incorrect answers to respective lists
for i in random_numbers:
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

# update user on their performance
# get length of each set of answers
num_correct = len(corrects)
num_inconnect = len(incorrects)

print(rtn())

percentage_correct = float(len(corrects)) / float(len(random_numbers))
print("You defined %s of the terms you attempted correctly.") % ("{0:.0%}".format(percentage_correct))

print(rtn())

print("%s %s") % ("Correct Answers:", num_correct)
for correct in corrects:
	print(correct)

print(rtn())

print("%s %s") % ("Incorrect Answers:", num_inconnect)
print("Review the following:")
for incorrect in incorrects:
	print(incorrect)

print(rtn())
