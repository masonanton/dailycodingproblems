# Given a string and a list of words (dictionary), return all anagrams of the string that are present in the dictionary.
# An anagram is any word with exactly the same characters as the input string, in any order.
#
# Example:
#   Input:
#       s = "race"
#       dictionary = ["bat", "acer", "caer", "apple"]
#   Output:
#       ["acer", "caer"]
#
# Implement the following function:

from collections import defaultdict
def find_anagrams(s, dictionary):
    sorted_word_dict = defaultdict(list)

    for word in dictionary:
        sorted_word_dict[''.join(sorted(word))].append(word)
    
    result = sorted_word_dict[''.join(sorted(s))]

    print(result)
    return result

find_anagrams("race", ["bat", "acer", "caer", "apple"])
