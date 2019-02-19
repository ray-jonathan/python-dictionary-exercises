# Write a word_histogram program that asks the user for a sentence 
# as its input, and prints a dictionary containing the tally of how many 
# times each word in the alphabet was used in the text. For example:

# $ python word_histogram.py
# Please enter a sentence: To be or not to be
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}

user_sent = input("What would you like to count the words of? ").lower()
user_list = user_sent.split()
silly_dict = {}

for words in user_list:
    silly_dict[words] = 0
for letters_b in user_list:
    for words in silly_dict.keys():
        if letters_b == words:
            silly_dict[words] += 1

return (silly_dict)
