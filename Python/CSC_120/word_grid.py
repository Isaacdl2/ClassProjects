'''
    File: word_grid.py
    Author: Isaac Larson
    Course: CSC 120, Spring 2024
    Purpose: This program gets an input of a grid size and random seed
             value to generate a grid of random letters based on the 
             inputted grid size and seed value.
'''
# -----------------------------------------------------------------------------
import random

def init():
    '''
    This function gets an input for grid size, a seed value, and initalizes
    a random number generator.

    Parameters: None
   
    Returns: Integer representing grid size. 
    '''

    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    return grid_size

def make_grid(grid_size):
    '''
    This function makes a grid of any size filled with random letters. 

    Parameters: grid_size is an integer representing both the width 
                and heightof the grid to be created. 

    Returns: A grid_size by grid_size grid filled with random letters.
    '''

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    grid = []

    for i in range(grid_size):
        temp_list = []
        for j in range(grid_size):
            random_num = random.randint(0, 25)
            random_letter = alphabet[random_num]
            temp_list.append(random_letter)
        grid.append(temp_list)
    return grid

def print_grid(grid):
    '''
    This function print a grid by seperating each row into a line
    and seperated by commas. 

    Parameters: A grid of any size. 

    Returns: None
    '''

    for row in grid:
        print(','.join(row))

def main():
    grid_size = init()
    grid = make_grid(grid_size)
    print_grid(grid)

main()
