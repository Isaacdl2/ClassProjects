'''
File: huffman.py
Author: Isaac Larson
Course: CSC 120, Spring 2024
Purpose: This program prompts the user for an input file, builds
a decoding tree using the given traversals, and decodes a sequence
of bits to retrieve the value of their respective nodes. 

Input example: 
9 0 6 3 2 8 4 // Pre order traversal of tree
6 0 2 3 8 9 4 // In order traversal of tree
0001011011100011 // Sequence of bits to be decoded using the tree

'''
# -----------------------------------------------------------------------------

class TreeNode:
    '''
    This class creates a TreeNode object, initalized with data, an integer
    '''
    def __init__(self, data):
        '''
        This init function initalizes constructs a TreeNode object with the
        input data, a reference to the right node, and a reference to 
        the left node

        Parameters: Data, an integer 
        '''
        self._data = data
        self._right = None
        self._left = None 

def buildTree(inorder, preorder):
    '''
    This function builds a decoding tree given lists of the inorder 
    and preorder traversals. 

    Parameters: inorder, a list and preorder, a list 

    Returns: A tree constructed according to the preorder and 
    inorder traversal 
    '''
    if not inorder or not preorder:
        return None

    # Find index of current root in inorder list and constructs it
    index = inorder.index(preorder[0])
    root = TreeNode(preorder.pop(0))

    # Builds left and right subtrees
    root._left = buildTree(inorder[:index], preorder)
    root._right = buildTree(inorder[index + 1:], preorder)

    return root

def print_postorder(root):
    '''
    This function recursively prints out the postorder of the inputted tree

    Parameters: root, a tree 
    '''
    if root is None:
        return
    
    print_postorder(root._left)
    print_postorder(root._right)
    print(root._data, end=" ")

def decode(tree, encoded):
    '''
    This function decodes a string of bits using the decoding tree 
    built above. 

    Parameters: tree, a decoding tree, encoded, a string of bits

    Returns: A string of data that was extracted from the respective
    nodes represented by the string of bits
    '''
    result = ""
    curr = tree

    for bit in encoded:
        if bit == '0':
            curr = curr._left
        elif bit == '1':
            curr = curr._right

        # If curr exists and is a leaf node
        if curr is not None and curr._left is None and curr._right is None: 
            result += curr._data
            # Once reach leaf node back to top of tree
            curr = tree 

    return result

        
def main():
    # Opens inputted file
    file = open(input(), "r" )

    # Puts the file's preorder and inorder into lists 
    preorder = file.readline().strip().split()
    inorder = file.readline().strip().split()
    encoded = file.readline().strip()

    # Builds tree, prints postorder, and decodes 
    root = buildTree(inorder, preorder)
    print("Input file: ", end = "")
    print_postorder(root)
    print("\n" + decode(root, encoded))

    file.close()
    
main()





