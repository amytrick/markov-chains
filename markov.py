"""Generate Markov text from text files."""
import random

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_file = open(file_path).read()
    # for line in text_file:
    #     print(line)

    # print(text_file)

    return text_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    words = text_string.split()

    chains = {}
    # value = []
    index = 0

    for word in words:

        if index < (len(words) - 2):
            second_word = words[index + 1]
            third_word = words[index + 2]
            keys = (word, second_word)  # TUPLE
            if keys in chains:
                chains[(keys)].append(third_word)
                index += 1
            else:
                chains[(keys)] = [third_word]
                index += 1

    # print(chains[(keys)])
    return chains


def make_text(chains):
    """Return text from chains."""
    # print(chains[0])

    words = []
    random_key = random.choice(list(chains.keys()))
    random_key_word = random.choice(random_key)
    print(random_key)
    print(random_key_word)
    # your code goes here
    # link is a tuple/ key form our dictionary
    # the link also includes a random word from the value of that key (rnaomd single value)
    # Iterate over

    # for key, value in chains.items():
    # print(key, value)
    # first_key = random.choice(chains.keys())
    # first_value = random.choice(chains[key])
    # print(first_key)
    # words.append(first_key)
    # words.append(first_value)
    # break
    # print(first_key)
    # print(words)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print(input_text)
# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print(random_text)
