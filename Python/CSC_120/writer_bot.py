'''
File: writer_bot.py
Author: Isaac Larson
Course: CSC 120, Spring 2024
Purpose: This program prompts the user for an input file, prefix size, and
number of words to generate a sequence of random words using Markov's 
chain algorithm. 
'''
# -----------------------------------------------------------------------------

import random
SEED = 8
random.seed(SEED)

NONWORD = " "
def read_text(file_name):
    '''
    This function opens a file, reads it, and closes it

    Parameters: A file name 

    Returns: A string, text. 
    '''
    
    file = open(file_name, 'r')
    text = file.read()
    file.close()
    return text

def build_markov_chain(text, prefix_size):
    '''
    This function builds the markov chain using the markov chain algorithm. 

    Parameters: text, a string, and prefix_sie, an integer 
    '''

    words = text.split()
    markov_chain = {}
    prefix = tuple([NONWORD] * prefix_size)
    
    for word in words:
        if prefix in markov_chain:
            markov_chain[prefix] += [word]
        else:
            markov_chain[prefix] = [word]
        prefix = tuple(list(prefix[1:]) + [word])
        
    return markov_chain

def generate_text(markov_chain, prefix_size, num_words, text):
    '''
    This function generates random english using markov's algorithm 

    Parameters: markov_chain, a dictionary, prefix_size, an integer, 
    num_words, and integer, test, a string

    Returns: A list of the randomly generated words
    '''

    tlist = []
    text = text.strip().split()

    # Makes tuple of first prefix_size words of the text
    prefix = text[:prefix_size]
    tlist.extend(prefix)

    while len(tlist) < num_words:
        # Checks if the current prefix exists in the Markov chain
        if tuple(prefix) in markov_chain:
            next_word_options = markov_chain[tuple(prefix)]
            random_index = random.randint(0, len(next_word_options)-1)
            next_word = next_word_options[random_index]
            tlist.append(next_word)
        else:
            # If prefix is not found end loop
            break

        # Removes first word and adds next work
        prefix = tlist[-prefix_size:]

    return tlist

def print_generated_text(generated_text):
    '''
    This function prints a list of words with 10 words on each line 
    and the remainder on the final line

    Parameters: generated_text, a list of strings
    '''
    count = 0
    for word in generated_text:
        count += 1
        if count == 10: 
            print(word + " ")
            count = 0
        else:
            print(word + " ",end="")

def main(): 
    text = read_text(input())
    prefix_size = int(input())
    num_words = int(input())

    markov_chain = build_markov_chain(text, prefix_size)
    generated_text = generate_text(markov_chain, prefix_size, num_words, text)
    print_generated_text(generated_text)

main()

