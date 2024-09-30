'''
    File: fake_news.py
    Author: Isaac Larson
    Course: CSC 120, Spring 2024
    Purpose: This program will take an input file of 
    news titles and an input integer k and  print out the top k words present 
    in the file. 
'''

# -----------------------------------------------------------------------------

import string
import csv

class Node:
    '''
    This class produces Node objects to be used in the LinkedList
    '''
    def __init__(self, word):
        '''
        Initalizes a node with a given word

        Parameters: word (str) - word stored in node
        '''
        self._word = word
        self._count = 1 
        self._next = None

    def word(self):
        # Getter function for word attribute
        return self._word
    
    def count(self):
        # Getter function for count attribute
        return self._count

    def next(self):
        # Getter funtion for the next node
        return self._next
    
    def set_next(self, target):
        '''
        Setter method to set the next node
        '''
        self._next = target

    def incr(self):
        '''
        Incraments the count associated with the word stored in the node
        '''
        self._count += 1

    def __str__(self):
        '''
        Returns a string representation of the node
        '''
        return "Occurences of '" + self._word + "': " + str(self._count)
    
class LinkedList: 
    '''
    This class produces LinkedList objects
    '''
    def __init__(self):
        '''
        Initalizes an empty linked list
        '''
        self._head = None

    def is_empty(self):
        '''
        Checks if the linked list is empty

        Returns: True if if empty, False otherwise
        '''
        return self._head is None
    
    def head(self):
        # Getter function for head of LinkedList
        return self._head
    
    def update_count(self, word):
        '''
        Updates the count of a word in the linked list or adds it if it
        doesn't exist. 

        Parameters: word (str) - the word whose ocunt needs to be updated
        '''
        curr = self._head
        while curr:
            if curr.word() == word:
                curr.incr()
                return
            curr = curr.next()
        new_node = Node(word)
        new_node.set_next(self._head)
        self._head = new_node

    def rm_from_hd(self):
        '''
        Removes the head node from the linked list 

        Returns: The removed node or None if the list is empty
        '''
        if self.is_empty():
            print("Error list is empty")
            return
        
        removed_node = self._head
        self._head = self._next
        return removed_node
    
    def insert_after(self, node1, node2):
        '''
        Inserts node2 after node1 in the linked list
        ''' 
        node2.set_next(node1.next())
        node1.set_next(node2)
    
    def sort(self):
        '''
        Sorts the linked list based on counts in descending order
        '''
        curr = self._head
        while curr:
            runner = curr.next()
            while runner:
                if curr.count() < runner.count():
                    temp_word = curr.word()
                    temp_count = curr.count()
                    curr._word = runner.word()
                    curr._count = runner.count()
                    runner._word = temp_word
                    runner._count = temp_count
                runner = runner.next()
            curr = curr.next()
        
    def get_nth_highest_count(self, n):
        '''
        Gets the count of the nth highest count in the linked list

        Parameters: n (int) - the position of the highest count to retrieve

        Returns: The count of the nth highest count
        '''
        curr = self._head
        for i in range(n-1):
            curr = curr.next()
        return curr.count()
    
    def output_k_items(self, n):
        '''
        Outputs all items with a count greater than or equal to the
        kth highest count

        Parameters: n (int) the position of the highest count to consider
        as k 

        Returns: A string containinng the word and count of each item that
        meets the criteria
        '''
        curr = self._head
        result = []

        for i in range(n): 
            curr = curr.next() 
        k = curr.count()
        curr = self._head

        while curr:
            if curr.count() >= k:
                result.append(curr.word() + " : " + str(curr.count()))
            curr = curr.next()
        return "\n".join(result)
        

    def __str__(self):
        '''
        Returns a string representation of the linked list
        '''
        result = []
        curr = self._head

        while curr:
            result.append("Word: " + curr.word() + " | Count: "
                           + str(curr.count()))
            curr = curr.next()
        return "\n".join(result)
    
def filter_line(line):
    '''
    Processes a line of text from the CSV file to filter out unwanted 
    characters and words

    Parameters: line (list) a list representing a line of text from 
    the CSV file

    Returns: A list of filtered words extracted from the line
    '''
    punctuation_chars = string.punctuation
    title = line[4]
    filtered_words = []

    # Removes punctuation
    for char in punctuation_chars:
        title = title.replace(char, " ")
    title = title.split()

    # Removes words less then 2 chars
    for word in title: 
        word = word.lower()
        if len(word) > 2:
            filtered_words.append(word)
    
    return filtered_words


def main(): 
    '''
    Reads CSV file, processes its content, ipdates the linked list,
    sorts it, and outputs k items
    '''
    count = 0
    file = open(input(), "r")
    csvreader = csv.reader(file)
    linked_list = LinkedList()

    for line in csvreader:
        count += 1
        line = filter_line(line)
        for word in line: 
            linked_list.update_count(word)
        
    linked_list.sort()
    print(linked_list.output_k_items(int(input())))

main()
    