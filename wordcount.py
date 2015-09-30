from sys import argv
from collections import Counter

script, file1 = argv

def word_count (filename):
    """reads in a file and counts how many times that word appears"""
    counter_dictionary = {}

    log_file = open(filename)

    for line in log_file:
        line = line.strip() #removing whitespace
        word_list = line.split(" ")

        for word in word_list:
            word = word.strip(", '. '?").lower() #removes punctuation
            if word in counter_dictionary:
                counter_dictionary[word] += 1
            else:
                counter_dictionary[word] = 1
    
    log_file.close()

    return counter_dictionary

print word_count(file1)
