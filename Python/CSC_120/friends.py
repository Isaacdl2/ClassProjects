'''
    File: friends.py
    Author: Isaac Larson
    Course: CSC 120, Spring 2024
    Purpose: This program uses Nodes and LinkedLists from the linked_list.py 
    file to organize an input file where each line is in the format {X Y}, 
    X and Y being strings representing names, that says X is a friend of Y
    and useing the information to find mutual friends of any two inputted 
    names. 
'''

# -----------------------------------------------------------------------------
from linked_list import Node, LinkedList

'''
This function adds a friend node (name2) to the linked list attribute 
of the (name1) node. If the name1 node does not exist yet it creates one and 
adds the name2 friend to it's linked list attribute. 

Parameters: A linked list, people. A string name1. A string name2. 
'''
def add_friend(people, name1, name2): 
    if people.find_name(name1) != False:
        person_node = people.find_name(name1)
        person_like_node = Node(name2)
        person_node.add_friend(person_like_node)
    else:
        person_node = Node(name1)
        person_like_node = Node(name2)
        
        person_node.add_friend(person_like_node)
        people.add(person_node)


def main(): 
    people = LinkedList()

    file = open(input("Input file: "), "r")
    for line in file: 
        line = line.strip().split() 

        add_friend(people, line[0], line[1])
        add_friend(people, line[1], line[0])
        
    name1 = input("Name1: ").strip()
    name2 = input("Name2: ").strip()

    # Checks to see if read name is in people linked list
    if not people.find_name(name1):
        print("ERROR: Unknown person " + name1)
        return
    if not people.find_name(name2):
        print("ERROR: Unknown person " + name2)
        return
        
    # Finds the nodes of inputted name1 and name2
    curr_node = people._head
    while curr_node: 
        if curr_node.get_name() == name1: 
            name1_friends = curr_node.get_friends()
        if curr_node.get_name() == name2:
            name2_friends = curr_node.get_friends()
        curr_node = curr_node._next

    # Loops through friends 1 and checks every friend in friends 2 to see if they match 
    friends_in_common = False
    curr_node = name1_friends._head
    while curr_node:
        curr_node2 = name2_friends._head
        while curr_node2:
            if curr_node.get_name() == curr_node2.get_name():
                if not friends_in_common: 
                    print("Friends in common:")
                    friends_in_common = True
                print(curr_node.get_name())
            curr_node2 = curr_node2._next
        curr_node = curr_node._next

main()

