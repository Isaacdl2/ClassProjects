'''
File: street.py
Author: Isaac Larson
Course: CSC 120, Spring 2024
Purpose: This program prompts the user for a one-line specification of a 
city street with parks, buildings, and empty lots, and then prints a simple 
ASCII rendering of it.

Building format: b:WIDTH,HEIGHT,BRICK    Ex) b:5,7,x
Park format: p:WIDTH,FOLIAGE             Ex) p:19,*
Empty lot format: e:WIDTH,TRASH          Ex) e:7,__~

Input example: p:19,* b:5,7,x e:7,__~
Input example: b:3,10,a e:10,+- p:13,* b:7,15,x b:17,4,% b:10,8,y e:5,_ 
'''
# -----------------------------------------------------------------------------


class Building:
    '''
    This class creates a Building object, initalized with width, an integer, 
    height, an integer, and brick, a one character string.
    '''

    def __init__(self, width, height, brick): 
        '''
        This init function initalizes the Building object.

        Parameters: A int, widthh, a int, height, a one character 
        string, brick. 
    '   '''
        
        self._width = width 
        self._height = height
        self._brick = brick 

    def print_building(self, curr_height = 1): 
        '''
        This function creates ASCII rendering of the building object.
        Not used in the program's main purpose and is used for testing.

        Parameters: None.

        Returns: A string rendering of the building.
        '''

        if curr_height == self._height:
            # Returns same as bottom but without a \n to mess up the 
            # rendering. 
            return self._brick * self._width
        else: 
            row = self._brick * self._width + "\n"
            return row + self.create_building(curr_height + 1)
    
    def make_line(self, line): 
        '''
        This function returns the inputted line of the ASCII 
        rendering of the building object.

        Parameters: An integer, line, representing which line to render. 

        Returns: A string.
        '''

        if self._height >= line:
            return self._brick * self._width
        else:
            return " " * self._width


class Park:
    '''
    This class creates a Park object, initalized with its width,
    an integer, and its foliage, a single character string. 
    '''

    def __init__(self, width, foliage):
        '''
        This init function initalizes the Park object. 

        Parameters: Width, an integer, foliage, a one character string. 
        '''

        self._width = width
        self._foliage = foliage
        self._middle = (width // 2) + 1

    def print_park(self, curr_height = 1): 
        '''
        This function creates ASCII rendering of the aprk object. Not used
        in the program's main prupose and is used for testing. 

        Returns: A string rendering of the park. 
        '''

        if curr_height > 5:
            return ""
        elif curr_height == 1:
            line = (" " * (self._middle - 1)) + self._foliage + \
            ( " " * (self._middle - 1)) + "\n"
        elif curr_height == 2: 
            line = (" " * (self._middle - 2)) + \
            self._foliage * 3 + ( " " * (self._middle - 2)) + "\n"
        elif curr_height == 3: 
            line = (" " * (self._middle - 3)) + \
            self._foliage * 5 + ( " " * (self._middle - 3)) + "\n"
        elif curr_height == 4:
            line = (" " * (self._middle - 1)) + "|" + \
            ( " " * (self._middle - 1)) + "\n"
        elif curr_height == 5:
            line = (" " * (self._middle - 1)) + \
            "|" + ( " " * (self._middle - 1))
        
        return line + self.create_park(curr_height + 1)
    

    def make_line(self, line): 
        '''
        This function returns the inputted line of the ASCII 
        rendering of the park object.

        Parameters: An integer, line, representing which 
        line to render. 

        Returns: A string.
        '''

        if line == 5:
            return (" " * (self._middle - 1)) + self._foliage + \
            ( " " * (self._middle - 1))
        elif line == 4: 
            return (" " * (self._middle - 2)) + \
            self._foliage * 3 + ( " " * (self._middle - 2))
        elif line == 3: 
            return (" " * (self._middle - 3)) + \
            self._foliage * 5 + ( " " * (self._middle - 3))
        elif line == 2:
            return (" " * (self._middle - 1)) + \
            "|" + ( " " * (self._middle - 1))
        elif line == 1:
            return (" " * (self._middle - 1)) + \
            "|" + ( " " * (self._middle - 1))
        else:
            return " " * self._width

class EmptyLot: 
    '''
    This class creates a EmptyLot object, initalized with its width,
    an integer, and its trash, a single character string. 
    ''' 

    def __init__(self, width, trash): 
        '''
        This init function initalizes the EmptyLot object. 

        Parameters: Width, an integer, trash, a string. 
        '''
        self._width = width
        self._trash = self.convert_trash(trash)

    def get_trash(self):
        '''
        This function is a getter function to get the trash string. 

        Returns: A string representing the trash. 
        '''

        return self._trash

    def convert_trash(self, trash, index = 0): 
        '''
        This function converts all the underscores in the trash string 
        and converts them to spaces. 

        Parameters: A string, trash. 

        Returns: The trash string with underscores replaced as spaces. 
        '''

        if index == len(trash):
            return trash
        else: 
            if trash[index] == "_": 
                trash = trash[:index] + " " + trash[index+1:]
            return self.convert_trash(trash, index + 1)

    def make_line(self, line, index = 0): 
        '''
        This function returns the inputted line of the ASCII rendering 
        of the EmptyLot object.

        Parameters: An integer, line, representing which line to render. 

        Returns: A string.
        '''

        if line > 1:
            return " " * self._width
        elif index == self._width:
            return ""
        else: 
            return self._trash[index % len(self._trash)] + \
            self.make_line(line, index + 1)
        
 
def read_street(areas):
    '''
    This function reads the user inputted line and converts it into 
    a list of lists with each element being an area. 

    Parameter: A string areas of the areas. 

    Returns: A 2D list. 
    ''' 

    if len(areas) == 0: 
        return []
    else: 
        return [areas[0].split(",")] + read_street(areas[1:])
    
def find_street_height(areas, curr_max = None): 
    '''
    This function finds the height of the tallest area. 

    Parameters: A 2D list areas. 

    Returns: The height of the tallest area as an integer. 
    '''

    if not areas:
        return curr_max
    elif areas[0][0][0] == "b":
        if curr_max is None or int(areas[0][1]) > curr_max:
            curr_max = int(areas[0][1]) + 1
    elif areas[0][0][0] == "p":
        if curr_max is None or curr_max < 6:
            curr_max = 6
    elif areas[0][0][0] == "e":
        if curr_max is None or curr_max < 2:
            curr_max = 2

    return find_street_height(areas[1:], curr_max)

def find_street_width(areas, total = 0): 
    '''
    This function finds the width of the street to be represented. 

    Parameters: Areas, a 2D list. 

    Returns: An integer representing the wdith of the street.
    '''

    if len(areas) == 0:
        return total 
    else:
        total += int(areas[0][0][2:])
        return find_street_width(areas[1:], total)
    
def build_line(street, height):
    """
    This function creates a line of the street at a given height by
    combining the line strings created for every respective area.

    Parameters: A 2D list, street. An integer, height, representing 
    the height at which to build the line. 

    Returns: A string representing a line of the street. 
    """

    if len(street) == 0:
        return ""
    elif street[0][0][0] == "b":
        b_p_e = Building(int(street[0][0][2:]), int(street[0][1]), \
        street[0][2])
    elif street[0][0][0] == "p":
        b_p_e = Park(int(street[0][0][2:]), street[0][1])
    elif street[0][0][0] == "e": 
        b_p_e = EmptyLot(int(street[0][0][2:]), street[0][1])
    return b_p_e.make_line(height) + build_line(street[1:], height)

def build_street(street, height):
    '''
    This function builds and prints the street by recursivly 
    building each line with the build_line function. 

    Parameters: A 2D list, street, an integer, height, 
    representing the highest point of the street. 
    '''

    if height == 0:
        return
    else: 
        print("|" + build_line(street, height) + "|")
        return build_street(street, height - 1)

def main(): 
    street1 = input("Street: ").split()
    street1 = read_street(street1)

    street1_height = find_street_height(street1)
    street1_width = find_street_width(street1) 

    print("+" + ("-" * street1_width) + "+")
    build_street(street1, street1_height)
    print("+" + ("-" * street1_width) + "+")

    
main()
 



        
        