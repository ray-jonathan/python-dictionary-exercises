# Given a histogram tally (one returned from either letter_histogram or 
# word_summary), print the top 3 words or letters.

# $ python word_histogram_tally.py

# Please enter a sentence: To be or not to be do be do be do
# The top three words are:
# be: 4
# do: 3
# to: 2

user_sent = input("Please enter a sentence: ").lower()
user_list = user_sent.split()
silly_dict = {}

for words in user_list:
    silly_dict[words] = 0
for letters_b in user_list:
    for words in silly_dict.keys():
        if letters_b == words:
            silly_dict[words] += 1

destructo_dict = silly_dict

def get_top_dawg(dict):
    top_word = max(dict, key=dict.get)
    top_count = dict[top_word]
    return ("%s: %d" % (top_word, top_count))
    del destructo_dict[top_word]

return ("Top three words are:")
get_top_dawg(destructo_dict)
get_top_dawg(destructo_dict)
get_top_dawg(destructo_dict)
