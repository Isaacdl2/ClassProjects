'''
Isaac Larson
CSC110
Project -4
This program has eight functions that makes a game of 1D Chess.
'''

def create_board():
    '''
    This function returns a list representing every space on the chess board.
    Args: None.
    '''
    return ["WKi", "WKn", "WKn",
             "EMPTY", "EMPTY", "EMPTY",
             "BKn","BKn","BKi"]

def printable_board(board):
    '''
    This function returns a representation of the board from the list in the create_board() function.
    Args:
        board: A list representing the chess board. 
    Returns:
        String representation of the board list.
    '''

    line_one = "+-----------------------------------------------------+\n"
    line_two = "| "

    for item in range(len(board)):
        if board[item] == "EMPTY":
            line_two += "   "
        else:   
            line_two += board[item]
        line_two += " | " 

    line_two += "\n"
    line_three = "+-----------------------------------------------------+"
    return line_one + line_two + line_three

def is_valid_move(board, position, player):
    '''
    This function determines if a move is allowed to be made.
    Args:
        board: List representing chess board.
        position: Index of piece trying to be moved.
        player: String representing player that is taking turn. "White" or "Black". 
    Returns:
        A boolean representing if the move is possible.
    '''

    if (position < 9 and position > -1):
        # if first letter of player == first letter of piece at position
        if player[0].lower() == (board[position][0]).lower():
            return True
    return False

def move_king(board, position, direction):
    '''
    This function updates the board list with the desired king move. The king can move right or left, and moves until it lands on another piece. 
    Args:
        board: List representing chess board.
        position: Index of king trying to be moved.
        direction: String representing direction trying to move. "LEFT" or "RIGHT". 
    Returns: Nothing.
    '''

    moving = True
    
    while moving == True: 
        if direction == "LEFT":
            if position == 0:
                return None

            # If the spot the king is moving has a piece, it replaces that piece and make the original spot empty. Returns None to exit the while loop.
            if board[position-1] != "EMPTY":
                board[position-1] = board[position]
                board[position] = "EMPTY"
                moving = False
            # When the spot king is moving to does not have piece, it replaces that spot with the king, and makes the oringal spot empty. Iterates until it takes a piece. 
            else:
                board[position-1] = board[position]
                board[position] = "EMPTY"
                position-=1

        if direction == "RIGHT":
            if position == 8:
                return None

            if board[position+1] != "EMPTY":
                board[position+1] = board[position]
                board[position] = "EMPTY"
                moving = False
            else:
                board[position+1] = board[position]
                board[position] = "EMPTY"
                position+=1

def move_knight(board, position, direction):
    '''
    This function updates the board list with the desired knight move. The knight can move right or left by 2 spaces. 
    Args:
        board: List representing chess board.
        position: Index of knight trying to be moved.
        direction: String representing direction trying to move. "LEFT" or "RIGHT". 
    Returns: Nothing.
    '''

    moving = True
       
    if direction == "LEFT":
        if position < 2:
            return None

        # Replaces the spot it is moving too with the knight and changes the original spot to be empty. 
        board[position-2] = board[position]
        board[position] = "EMPTY"

    if direction == "RIGHT":
        if position > 6:
            return None

        board[position+2] = board[position]
        board[position] = "EMPTY"

def move(board, position, direction):
    '''
    This function updates the board list with the desired knight or king move. This function figures out which piece is trying to be moved by itself. 
    Args:
        board: List representing chess board.
        position: Index of the piece trying to be moved.
        direction: String representing direction trying to move. "LEFT" or "RIGHT". 
    Returns: Nothing
    '''

    # Subscripts the second and third letter to check what type of pice it is. 
    if board[position][1:] == "Ki":
        move_king(board, position, direction)
    if board[position][1:] == "Kn":
        move_knight(board, position, direction)

def is_game_over(board):
    '''
    This function determines weather or not the game is over. The game is over one a king on either side is taken. 
    Args:
        board: List represting chess board. 
    Returns: Boolean representing wheter the game is over or not. True = game over, False = game not over. 
    '''

    count = 0

    for item in board:
        if item[1:] == "Ki":
            count+=1
    if count == 1:
        return True
    return False

def whos_the_winner(board):
    '''
    This function determines who is the winner of the game.
    Args:
        board: List represting chess board. 
    Returns: String represting the winner. "White" or "Black
    '''

    if is_game_over(board):
        for item in board:
            if item == "BKi":
                return "Black"
            if item == "WKi":
                return "White"
    return None

def main():
    board = create_board()
    print( printable_board(board) )

main()