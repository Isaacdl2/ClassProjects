
'''
Isaac Larson
CSC 110
Project -5
This program has x functions to implement a Benford's Law analysis. 
'''

'''
This function determines if a string is a integer by trying t oconvert the string to a integer. Returns True or False.
Args:
    A string.
Returns:
    A boolean. True if the string can be converted to a int. False otherwise. 
'''
def is_digit(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def is_float(string):
    '''
    This function determines if a string is a float by trying to convert the string to a float. Returns True or False. 
    Args:
        string: A string. 
    Returns:
        A boolean. True if the string can be converted to a float. False otherwise.
    '''

    # Made numbers starting with a decimal not count as a float for Benford Law purposes. 
    if string[0] == ".":
            return False
    try:
        float(string)
        return True
    except ValueError:
        return False

def csv_to_list(file_name):
    '''
    This function takes a csv file of items seperated by commas and collects all the integers/floats in a list.
    Args:
        file_name: String argument that leads to file. 
    Returns: 
        A list of number found in the file.   
    '''

    file = open(file_name, "r")
    file_numbers = []

    # Loops through line --> Split into list of words -> Determines if float/int --> Adds to list of numbers if so
    for line in file:
        line_items = line.strip().split(",")

        for i in range(len(line_items)):
            if is_digit(line_items[i]):
                file_numbers.append(line_items[i])
            elif is_float(line_items[i]):
                file_numbers.append(line_items[i])
    return file_numbers

def count_start_digits(numbers):
    '''
    This function takes a list of numbers and returns a dictionary keeping count of the number of times a number appears in the first digit. 
    Args:
        numbers: List of strings that represents numbers. 
    Returns:
        Dictionary of counts converted to integers. 
    '''

    # Added 0 to the dictionary to prevent error when the input list had numbers starting with 0. 
    first_digit_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for item in numbers:
            # Thought the csv_to_list function isolated all the numbers/floats but got an error saying a letter slipped through?
            # Ran is_digit again to fix the problem
            if(is_digit(item[0])):
                first_digit_count[int(item[0])] += 1
    
    del first_digit_count[0]
    return first_digit_count

def digit_percentages(counts):
    '''
    This function creates a new dictionary with the percentage for each digit. 
    Args:
        counts: Dictionary with digit counts. 
    Returns:
        A new dictionary with digit percentages. 
    '''

    count = 0
    percentages = {}

    for value in counts.values():
        count+=value

    for key, value in counts.items():
        percentages[key] = round((value / count) * 100, 2)

    return percentages

def check_benfords_law(percentage_dictionary):
    '''
    This function determines if the percentage dictionary qualifies for benfords law by checking the percentage range of each digit. 
    Args:
        percentage_dictionary: Dictionary with percentages per digit. 
    Returns: A boolean. True if it is Benfords law, false if not. 
    '''
    if not (25 <= percentage_dictionary[1] <= 40):
        return False
    if not (12 <= percentage_dictionary[2] <= 27):
        return False
    if not (7 <= percentage_dictionary[3] <= 22):
        return False
    if not (4 <= percentage_dictionary[4] <= 19):
        return False
    if not (2 <= percentage_dictionary[5] <= 17):
        return False
    if not (1 <= percentage_dictionary[6] <= 16):
        return False
    if not (0 <= percentage_dictionary[7] <= 15):
        return False
    if not (0 <= percentage_dictionary[8] <= 15):
        return False
    if not (0 <= percentage_dictionary[8] <= 14):
        return False
    return True