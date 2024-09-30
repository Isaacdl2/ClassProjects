'''
    File: rhymes.py
    Author: Isaac Larson
    Course: CSC 120, Spring 2024
    Purpose: This program takes a input file of word pronunciations and a word, 
    and finds all the words from the word file that perfectly rhyme with the
    inputted word. 
'''

'''
    This function takes a file of a word and it's pronunciation on each line 
    and maps the word into a dictionary with the word as they key and a 2D list 
    of all the words pronunciations as the value. 

    Parameters: A file.

    Returns: A dictionary with strings as keys and a 2D list of string as values.
'''
def makeDict(filename):
    file = open(filename,"r")
    result = {}

    for line in file: 
        # Splits each phenome into a list and removes all the empty items in the list. 
        temp_list = line.split(" ")
        temp_list = ' '.join(temp_list).split()

        # Creates a ditionary with the word as the key and a list of lists as value. 
        # The lists in the value are all the pronunciations. 
        if temp_list[0] in result:
            result[temp_list[0]].append(temp_list[1:])
        else:
            result[temp_list[0]] = [temp_list[1:]]
    return result

'''
    This function finds the primary stressed pheonome given the pronunciation of the word. 

    Parameters: A list of all the phenomes in the word. 

    Returns: A string representing the primary stressed phenome. 
'''
def find_primary_stress(pronunciation): 
    for phenome in pronunciation:
        for char in phenome:
            if char == "1":
                return phenome
    return phenome
   
'''
    This functions finds all the words in the given file that rhyme with the inputted word. 

    Parameters: A dictionary with words as keys and a 2D list of pronunciations as values. 

    Returns: A list of all the words that rhyme with the inputted word. 
'''
def findRhymes(dictionary, inpWord): 
    rhymes_list = []

    # 2D list of all the pronunciations of the inputted word. 
    inp_pronunciations = dictionary[inpWord.upper()]

    # Loops through each pronunciation of the inputted word and find its primary stress.
    for inp_pronunciation in inp_pronunciations:
        
        inp_primary_stress = find_primary_stress(inp_pronunciation)
        dictionary_primary_stress = ""

        # Loops through each pronunciation in the dictionary and finds its primary stress. 
        for word, list2D in dictionary.items(): 
            for dict_pronunciation in list2D: 
                dict_primary_stress = find_primary_stress(dict_pronunciation)

                # Now have the primary stress of both the imputted word and current word in dict to compare 
                inp_primary_stress_index = inp_pronunciation.index(inp_primary_stress)
                dict_primary_stress_index = dict_pronunciation.index(dict_primary_stress)

                # Checks if the phenomes proceeding the primary stressed ones are equal.
                if inp_pronunciation[inp_primary_stress_index:] == dict_pronunciation[dict_primary_stress_index:]:
                    # Checks for the case where there is no element before the stressed phenome.
                    if inp_primary_stress_index == 0 and dict_primary_stress_index != 0:
                        rhymes_list.append(word)
                    elif inp_primary_stress_index != 0 and dict_primary_stress_index == 0:
                        rhymes_list.append(word)
                    # Checks to make sure the preceeding phenomes of the primary stressed one is equal. 
                    elif inp_pronunciation[inp_primary_stress_index-1] != dict_pronunciation[dict_primary_stress_index-1]: 
                        rhymes_list.append(word)

    return rhymes_list

def main():
    myDict = makeDict(input())
    word = input()
    rhymes = findRhymes(myDict, word)
    rhymes.sort()

    for word in rhymes: 
        print(word.upper())

main()
