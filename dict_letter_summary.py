# Write a letter_histogram program that asks the user for input, 
# and prints a dictionary containing the tally of 
# how many times each letter in the alphabet was used in the word. 
# For example:

# $ python letter_histogram.py
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}

user_word = input("What would you like to count the letters of? ")
silly_dict = {}

for letters in user_word:
    silly_dict[letters] = 0
for letters_b in user_word:
    for letters in silly_dict.keys():
        if letters_b == letters:
            silly_dict[letters] += 1

return (silly_dict)
