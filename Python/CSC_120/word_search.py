'''
    File: word_search.py
    Author: Isaac Larson
    Course: CSC 120, Spring 2024
    Purpose: This program [FINISH LATER]
'''
# -----------------------------------------------------------------------------

def get_word_list(filename):
    '''
    This function takes a file of words and puts all the words seperated 
    into a list.

    Parameters: A file containing one word on each line. 

    Returns: A list of all the words in the file. 
    '''

    word_list = []
    file = open(filename,"r")

    for line in file:
        word_list.append(line.strip().lower())
    return word_list

def read_letters_files(filename):
    '''
    This function takes a file with a grid representation on it and converts
    it into an actual grid. 

    Parameters: A file with letters formatted like a grid. 

    Returns: A grid. 
    '''

    grid = []
    file = open(filename,"r")

    for line in file:
        grid.append(line.split())
    return grid

def occurs_in(substr, word_list):
    return (substr in word_list)

def column2list(grid, n):
    '''
    This function converts column n of grid, grid into a list. 

    Paraments: A grid 'grid' and a column 'n'.
    
    Returns: A list of all the items in nth column. 
    '''

    result = []
    
    for row in grid: 
        result.append(row[n])
    return result

def search_horizontal_right(grid, word_list):
    '''
    This function searches for words atleast 3 letter long, 
    left to right in each row.

    Paremeters: A grid, 'grid'. A list of words 'word_list'.

    Returns: A list of all the words found in the grid. 
    '''

    words = []

    # Loops through each row in grid
    for row in grid: 
        i = 0
        
        # Loops through each letter with atleast 2 more letter proceeding it
        while i <= len(row) - 3:
            word = ""
            j = 0

            # Takes the current letter i, checks to see if it's a valid word,
            # sticks on the proceeding letter of the row and keep repeating
            # this process until the end of the row is reached. Subtracting
            # len(row) by i counteracts the incrament of i to prevent going
            # out of bounds. 
            while j < len(row)-i:
                word += row[i + j] 
                j += 1


                if (occurs_in(word,word_list) and (len(word) >= 3)):
                    words.append(word)
            i += 1
    return words

def search_horizontal_left(grid, word_list): 
    '''
    This function searches for words atleast 3 letters wrong from right to 
    left by reversing each roch and using the search right function above.

    Paremeters: A grid, 'grid'. A list of words 'word_list'.

    Returns: A list of words found from right to left in the grid. 
    '''

    reversed_grid = []
    
    for row in grid:
        row_reversed = row[::-1]
        reversed_grid.append(row_reversed)
    return search_horizontal_right(reversed_grid, word_list)

def search_vertically_down(grid, word_list):
    '''
    This function searches for words up to down in a grid by a process similar
    to rotating the grid 90 degrees counter-clockwise making allowing us to 
    run the search horizontal right function above. 

    Paremeters: A grid, 'grid'. A list of words 'word_list'.

    Returns: A list of words found searching up to down. 
    '''

    column_grid = []
    for column in range(len(grid)):
        column_grid.append(column2list(grid,column))
    return search_horizontal_right(column_grid, word_list)

def search_vertically_up(grid, word_list):
    '''
    This function searched for words up to down in a grid by converting the 
    columns into lists, reversing the lists, and running it through the 
    search  horizontal right function above. 

    Paremeters: A grid, 'grid'. A list of words 'word_list'.

    Returns: A list of words found serching down to up. 
    '''
    column_grid_reversed = []

    for column in range(len(grid)):
        column_list = column2list(grid,column)
        column_list_reversed = column_list[::-1]
        column_grid_reversed.append(column_list_reversed)
    return search_horizontal_right(column_grid_reversed, word_list)

def search_diagonally_UL_LR(grid, word_list):
    '''
    This function searches for word diagnolly upper left to lower 
    right in a grid. 

    Paremeters: A grid, 'grid'. A list of words 'word_list'. 

    Returns: A list of words found diagnolly in the grid. 
    '''
    words = []
    num_diagnols = (len(grid) * 2) - 1
    num_rows = len(grid)
    
    # This loop runs the amount of times as there are diagnols 
    # in the grid. 
    for offset in range((-num_rows) + 1,num_rows):
        word = ""
        diagnol = ""

        # Finds words in positive offsets.
        if offset >= 0:
            row = 0
            column = offset
            word = ""
             
            for i in range(len(grid) - offset):
                word += grid[row][column]
                row += 1
                column += 1
                
                if len(word) == (len(grid) - offset):
                    diagnol = word

                    for i in range(len(diagnol)):
                        for j in range(len(diagnol)):
                            if i == 0 and j == 0:
                                word = diagnol
                            else:
                                word = diagnol[i:j]

                            if (occurs_in(word,word_list) and (len(word) >= 3)):
                                words.append(word)

        # Finds words in negative offsets. 
        if offset < 0:
            row = abs(offset)
            column = 0
            word = ""

            for i in range(len(grid) - abs(offset)):
                word += grid[row][column]
                row += 1
                column += 1

                if len(word) == len(grid) - abs(offset):
                    diagnol = word

                    for i in range(len(diagnol)):
                        for j in range(len(diagnol)):
                            if i == 0 and j == 0:
                                word = diagnol
                            else:
                                word = diagnol[i:j]

                            if (occurs_in(word,word_list) and (len(word) >= 3)):
                                words.append(word)
    return words
            
def output_words(words):
    '''
    This function takes a list of words, alphabetizes them, and 
    prints out each word to its own line.

    Parameter: A list of strings. 

    Returns: None.
    '''
    words = list(set(words))
    words.sort()
    for word in words:
        print(word,end="\n")
    

def main():
    word_list = get_word_list(input())
    grid = read_letters_files(input())

    listLR = search_horizontal_right(grid, word_list)
    listRL = search_horizontal_left(grid, word_list)
    listUP = search_vertically_down(grid, word_list)
    listDU = search_vertically_up(grid, word_list)
    listUL_LR = search_diagonally_UL_LR(grid, word_list)
 
    words = listLR + listRL + listUP + listDU + listUL_LR
    output_words(words)

main()
