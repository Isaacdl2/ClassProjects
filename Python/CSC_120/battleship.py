'''
File: battleship.py
Author: Isaac Larson
Course: CSC 120, Spring 2024
Purpose: This program prompts the user for a placement file of ships and 
a file of guesses to hit the ships. 

File 1 input example: 
A 0 7 4 7
P 4 2 5 2
D 7 5 7 3
B 2 2 2 5
S 9 9 9 7

File 2 input example:
1 7
0 7
4 3
9 4
2 7
97 63
2 3
'''
# -----------------------------------------------------------------------------

import sys

class GridPos: 
    '''
    This class creates GridPos objects that represent the current position
    on the board's grid
    '''
    def __init__(self,x,y):
        '''
        This init function initalized a GridPos object with a inputted
        x,y coordinate. Also has _ship attribute that has ship object if ship
        is at coordinate and None otherwise. Also has _guessed attribute 
        which is true if the spot has been guessed by the player and false 
        otherwise. 

        Parameters: x, a one character string, and y, a one character string
        '''

        self._x = x 
        self._y = y
        self._ship = None
        self._guessed = False

    def __str__(self):
        '''
        This str function prints the GridPos object. If part of a ship is at 
        the coordinate it prints "S" otherwise an empty spot will be a "*"

        Returns: A string, "S " or "* " 
        '''

        if self._ship is not None:
            return "S "
        else:
            return "* "

class Board: 
    '''
    This class creates a Board object that represents a 10x10 board with 
    ships on it
    '''
    def __init__(self): 
        '''
        This init function initalized a board. Has _grid attribute that is 
        a 10x10 grid of GridPos objects. Has a _ships attribute that is a 
        list of all the ships on the baord
        '''

        self._grid = make_grid()
        self._ships = []

    def shoot(self, x,y):
        '''
        This function takes a guess from the file of guesses and 
        takes a "shot" on the board. Will print hit, hit (again), 
        miss, miss (again), and game over if the all ships are sunk

        Parameters: board, a board object, x, an integer, and y, an integer
        '''

        grid_pos = self._grid[x][y]

        # If there's no ship at x, y
        if grid_pos._ship == None:
            # If x,y pos already guessed
            if grid_pos._guessed:
                print("miss (again)")

            # If first time x, y pos being guesed
            else:
                print("miss")
                grid_pos._guessed = True

        # If there is a ship at x, y
        else:
            # If x,y already gyessed
            if grid_pos._guessed:
                print("hit (again)")
            
            # If first time x,y guessed
            else:
                grid_pos._guessed = True
                grid_pos._ship._ship_left -= 1

                # If all parts of ship were hit
                if grid_pos._ship._ship_left == 0:
                    print(grid_pos._ship._type + " sunk")
                    self._ships.remove(grid_pos._ship)
                else:
                    print("hit")

        # Checks to see if list of ships is empty to confirm game over            
        if len(self._ships) == 0:
            print("all ships sunk: game over")
            sys.exit(0)

    def __str__(self):
        '''
        This str function prints a representation of the board. Will print 
        each row with a "S" if there is a ship at each position and a 
        "*" otherwise

        Returns: A string, board
        '''

        board = "" 
        for row in self._grid:
            for spot in row:
                board += str(spot)
            board += "\n"
        return board
   
class Ship:
    '''
    This class creates a ship object that represents a ship to be placed 
    on the board
    '''
    def __init__(self):
        '''
        This innit function initalizes a ship object. Has attributes _type,
        a one character string representing type of ship, _size, an integer 
        representing the length of the ship, _grid_positions, a list of 
        every [x,y] coordinate the ship is on, and _ship_left, an integer
        representing the amount of spots on the board left the ship hasn't 
        been hit
        '''

        self._type = None
        self._size = None
        self._grid_positions = []
        self._ship_left = None
    
    def __str__(self):
        '''
        This str function returns a string representation of the ship object. 
        
        Returns: A string as Size: "", Positions: [], " Ship left: ""
        '''

        positions = ""
        for position in self._grid_positions:
            positions += ("[" + str(position[0]) +  "," + 
            str(position[1]) + "]")

        return (self._type + ": Size: " + str(self._size) + ", Positions: " + 
                positions + ", Ship left: " + str(self._ship_left))

def make_grid():
    '''
    This function creates a 10x10 grid of GridPos objects and used in the 
    Board object.

    Returns: A 10x10 grid of GridPos objects
    '''

    grid = []
    for i in range(10):
        row = []
        for j in range(10):
            curr_grid_pos = GridPos(i,j)
            row.append(curr_grid_pos)
        grid.append(row)
    return grid

def make_board(file):
    '''
    This function creates a board object and accounts for the primary errors
    while doing so

    Parameters: A file with ship positions

    Returns: A board with all the ships on it
    '''

    board = Board()

    for line in file:
        line_parts = line.strip().split()

        # Checks for ship position where 0 <= x,y <= 9
        if check_not_inbounds(line_parts):
            print("ERROR: ship out-of-bounds: " + line, end = "")
            sys.exit(0)
        
        # Checks to make sure ship is either horizontal or vertical
        if check_not_h_or_v(line_parts):
            print("ERROR: ship not horizontal or vertical: " + line, end = "")
            sys.exit(0)
        
        # Creates ship object from line
        ship = make_ship(line_parts)

        # Checks to see if new ship object overlaps with existing ship objects
        if check_ship_overlap(ship, board._ships):
            print("ERROR: overlapping ship: " + line, end = "")
            sys.exit(0)
        
        # Checks to see if new ship object is the right size for the ship type
        if check_wrong_ship_size(ship):
            print("ERROR: incorrect ship size: " + line, end = "")
            sys.exit(0)

        # If all checks are passed ship is added to board
        board._ships.append(ship)

        # Add the ship to respective GridPos objects
        for pos in ship._grid_positions:
            x, y = pos
            board._grid[x][y]._ship = ship

    # Checks for invald fleet comp
    if check_fleet_comp(board._ships):
        print("ERROR: fleet composition incorrect")
        sys.exit(0)
    return board

# ship_info is a valid line from the file
def make_ship(ship_info):
    '''
    This function makes a ship object and determines its size and all 
    the coordinates the ship is one. 

    Parameters: A list, ship_info

    Returns: A ship object
    '''

    ship = Ship()

    ship._type = ship_info[0]
    x1 = int(ship_info[1])
    y1 = int(ship_info[2])
    x2 = int(ship_info[3])
    y2 = int(ship_info[4])

    # If ship is horizontal, finds all positions of ship on x axis
    if x1 == x2:
        ship._size = abs(y1 - y2) + 1
        ship._ship_left = ship._size
        for i in range(ship._size):
            ship._grid_positions.append([x1, i + min(y1,y2)])

    # If ship is vertical, finds all positions of ship on y axis
    elif y1 == y2:
        ship._size = abs(x1 - x2) + 1
        ship._ship_left = ship._size
        for i in range(ship._size):
            ship._grid_positions.append([i + min(x1,x2), y1])

    return ship

def check_fleet_comp(ships):
    '''
    This function confirms a given list of ships is a valid fleet
    by confirming there are only 5 ships aswell as only 1 of each 
    type of ship

    Parameters: ships, a list of ship objects

    Returns: True if not valid, False if it is valid
    '''

    ship_types = ["A","B","S","D","P"]

    if len(ships) > 5:
        return True
    for ship in ships:
        if ship._type in ship_types:
            ship_types.remove(ship._type)
    if len(ship_types) > 0:
        return True
    return False

def check_not_inbounds(line_parts):
    '''
    This function checks to see if a ship from the input file 
    is in the 10x10 bounds of the grid

    Parameters: line_parts, a list

    Returns: True if ship is no inbounds, False otherwise 
    '''

    for num in line_parts[1:]:
        if int(num) > 9 or int(num) < 0:
            return True
    return False

def check_not_h_or_v(line_parts):
    '''
    This function confirms if a ship is either horizontal or 
    vertical 

    Parameters: line_parts, a list

    Returns: True is ship is not horizontal or vertical, 
    False otherwise
    '''

    x1 = line_parts[1]
    y1 = line_parts[2]
    x2 = line_parts[3]
    y2 = line_parts[4]

    if x1 == x2:
        return False
    if y1 == y2:
        return False
    return True

def check_ship_overlap(ship, all_ships):
    '''
    This function checks if a ship overlaps with the other 
    ships on a board. 

    Parameters: ship, a ship object and all_ships, a list of ship objects

    Returns: True if ship overlaps another ship, False otherwise
    '''

    for other_ship in all_ships:
        if other_ship != ship:
            for position in ship._grid_positions:
                if position in other_ship._grid_positions:
                    return True
    return False

def check_wrong_ship_size(ship):
    '''
    This function checks if a ship is the correct size according to 
    its type. 

    Parameters: ship, a ship object

    Returns: True if ship is wrong size, False otherwise
    '''

    if ship._type == "A" and ship._size != 5:
        return True
    elif ship._type == "B" and ship._size != 4:
        return True
    elif ship._type == "S" and ship._size != 3:
        return True
    elif ship._type == "D" and ship._size != 3:
        return True
    elif ship._type == "P" and ship._size != 2:
        return True
    return False

def is_valid_guess(x,y):
    '''
    This function checks to see if a given x,y is a valid guess

    Parameters: x, a one character string and y, another one 
    character string

    Returns: True if it's a valid guess, False otherwise
    '''

    if int(x) > 9 or int(x) < 0:
        return False
    if int(y) > 9 or int(y) < 0:
        return False
    return True

def main(): 
    file = open(input(), "r")
    board = make_board(file)
    file.close()

    file = open(input(), "r")
    for line in file:
        line = line.strip().split()

        if not is_valid_guess(line[0], line[1]):
            print("illegal guess")
        else:
            board.shoot(int(line[0]), int(line[1]))
    file.close()
  
main()