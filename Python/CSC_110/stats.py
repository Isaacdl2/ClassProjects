'''
Isaac Larson
CSC110
Project 3
This program has 4 functions to run descriptive statistics on lists.
'''

def mean(numbers):
    '''
    This function returns the mean of a list of numbers rounded to 2 decimals by:
    1. Adding up all items in the list.
    2. Dividing the total by the number of items in the list.
    Args:
        numbers: A list of numbers.
    Returns:
        The mean of the list of numbers. Returns 0 if list is empty. 
    '''
    if len(numbers) < 1:
        return 0

    i = 0
    total = 0

    # Loops through every item in the list.
    while i < len(numbers):
        total = total + numbers[i]
        i+=1
    return round((total / (len(numbers))),2)

def variance(numbers):
    '''
    This function return the variance of a list of numbers rounded to 2 decimals by:
    1. Calculating the mean.
    2. Summing the squares of the difference between each value in numbers and the mean.
    Args:
        numbers: A list of numbers.
    Returns:
        The variance of the list of numbers. Returns 0 if list is empty. 
    '''
    if len(numbers) < 1:
        return 0

    i = 0
    total = 0
    the_mean = mean(numbers)

    # Loops through every item in list.
    while i < len(numbers):
        # Adds the square of the difference of the current list item and the list mean to the total.
        total = total + ((numbers[i] - the_mean)**2)
        i+=1
    return round((total / (len(numbers) - 1)),2)

def sd(numbers):
    '''
    This function return the standard deviation of a list of numbers rounded to 2 decimals by:
    1. Calculating the variance.
    2. Taking the square root of the variance.
    Args:
        numbers: A list of numbers.
    Returns:
        The standard deviation of the list of numbers. Returns 0 if list is empty.
    '''
    the_variance = variance(numbers)
    return round((the_variance**(1/2)),2)

def list_range(numbers):
    '''
    This function return the range of a list of numbers rounded to 2 decimals by:
    1. Finding the highest and lowest numbers in a list.
    2. Subtracting the lowest number from the highest number.
    Args:
        numbers: A list of numbers.
    Returns:
        The range of the list of numbers. Returns 0 if list is empty.
    '''
    if len(numbers) < 1:
       return 0

    i = 0
    highest_number = numbers[0]
    lowest_number = numbers[0]

    # Loops through the list and sets the low and high variables to the lowest and highest numbers in the list.
    while i < len(numbers):
        if numbers[i] <= lowest_number:
            lowest_number = numbers[i]
        if numbers[i] >= highest_number:
            highest_number = numbers[i]
        i+=1

    return round((highest_number - lowest_number),2)