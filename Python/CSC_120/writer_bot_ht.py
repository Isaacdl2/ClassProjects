'''
File: writer_bot_ht.py
Author: Isaac Larson
Course: CSC 120, Spring 2024
Purpose: This program prompts the user for an input file, hash table size,
prefix size, and number of words to generate a sequence of random words 
using Markov's chain algorithm. 
'''

# -----------------------------------------------------------------------------
import random
import sys

SEED = 8
random.seed(SEED)
NONWORD = '@'

class Hashtable:
    '''
    An object of this class is a hashtable that uses linear probing to 
    handle collisions.
    '''
    def __init__(self, size):
        '''
        Initializes a new Hashtable object with a given size.

        Parameters: size (integer)
        '''

        self._size = size
        self._pairs = [None] * size

    def _hash(self, key):
        '''
        Calculates the index in the hash table's underlying list where the 
        key-value pair should be stored.

        Parameters: key (hashable object)

        Returns: An integer representing index in the hash table's 
        underlying list.
        '''

        p = 0
        for c in key:
            p = 31 * p + ord(c)
        return p % self._size
    
    def put(self, key, value):
        '''
        Inserts a key-value pair into the hash table.

        Parameters: key (hashable object), value (any object)
        '''

        index = self._hash(key)
        while self._pairs[index] is not None:
            index = (index-1) % self._size
        self._pairs[index] = (key, value)

    def get(self, key):
        '''
        Retrieves the value associated with a given key from the hash table.

        Parameters: key (hashable object)
        
        Returns: Value associated with key, or None.
        '''

        index = self._hash(key)
        start_index = index
        while self._pairs[index] is not None:
            if self._pairs[index][0] == key:
                return self._pairs[index][1]
            index = (index - 1) % self._size
            if index == start_index:
                return None
        return None
    
    def __contains__(self, key):
        '''
        Checks if a given key exists in the hash table.

        Parameters: key (hashable object)
        
        Returns: True if key exists, false otherwise.
        '''

        index = self._hash(key)
        start_index = index
        while self._pairs[index] is not None:
            if self._pairs[index][0] == key:
                return True
            index = (index - 1) % self._size
            if index == start_index:
                return False
        return False
    
    def __str__(self):
        '''
        Returns a string representation of the Hashtable object.
        '''

        pairs_list = []
        for pair in self._pairs:
            if pair is not None:
                pairs_list.append(f"({pair[0]}, {pair[1]})")
            else:
                pairs_list.append("None")
        pairs_str = ", ".join(pairs_list)
        return f"Hashtable({self._size}): [{pairs_str}]"
    

class MarkovChain:
    '''
    An object of this class is a MarkovChain that follows Markov's
    Chain Algorithm. 
    '''
    def __init__(self, prefix_size, hash_size):
        '''
        Initializes a MarkovChain object with the specified prefix size
        and hash table size.

        Parameters, prefix_size (integer), hash_size (integer)
        '''

        self._prefix_size = prefix_size
        self._table = Hashtable(hash_size) 

    def generate_prefixes_and_suffixes(self, words):
        '''
        Generates prefixes and their corresponding suffixes from the given 
        list of words and populates the hash table.

        Parameters: words (a list)
        '''

        words = [NONWORD] * self._prefix_size + words  
        # Add NONEWORD to beginning of word list
        for i in range(len(words) - self._prefix_size):
            prefix = " ".join(words[i:i + self._prefix_size])
            suffix = words[i + self._prefix_size]
            if prefix not in self._table:
                self._table.put(prefix, [suffix])
                # Makes key value pair, with suffix as a list
            else:
                self._table.get(prefix).append(suffix)
                # Gets value at prefix key and adds the suffix to the value

    def generate_chain(self, text):
        '''
        Generates the Markov chain by splitting the input text into words
        and calling generate_prefixes_and_suffixes() 

        Parameters: text (a string)
        '''

        words = text.split()  
        self.generate_prefixes_and_suffixes(words)

    def generate_text(self, num_words, input_text):
        '''
        Generates text of a specified length using the Markov chain
        previously generated.

        Parameters: num_words (integer), input_text (string)

        Returns: List of generated words
        '''

        text = []
        input_text = input_text.strip().split()
        text.extend(input_text[:self._prefix_size])
        # Adds first n amount of words to the randomly generated text list

        for i in range(num_words - self._prefix_size):
            prefix = " ".join(text[-self._prefix_size:])
            # Joins last n amount of words in text into a string
            suffixes = self._table.get(prefix)

            if len(suffixes) > 1:
                random_index = random.randint(0, len(suffixes) - 1)
                next_word = suffixes[random_index]
            else:
                next_word = suffixes[0]
            text.append(next_word)

        return text

    def __str__(self):
        '''
        Returns a string representation of the Markov chain, including
        its prefixes and corresponding suffixes.

        Returns: String representation of chain.
        '''

        chain_str = "Markov Chain:\n"
        for pair_index in range(self._table._size):
            pair = self._table._pairs[pair_index]
            if pair is not None: 
                prefix, suffixes = pair
                suffixes_str = ", ".join(suffixes)
                chain_str += f"Prefix: {prefix} | Suffixes: {suffixes_str}\n"
        return chain_str

def main():

    file = open(input(), "r")
    hashtable_size = int(input())
    prefix_size = int(input())
    num_words = int(input())

    if prefix_size < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)
        
    input_text= ""
    for word in file:
        input_text += word + " "

    markov_chain = MarkovChain(prefix_size, hashtable_size)
    markov_chain.generate_chain(input_text)

    generated_text = markov_chain.generate_text(num_words, input_text)

    for i in range(0, len(generated_text), 10):
        print(" ".join(generated_text[i:i+10]))

    
main()
