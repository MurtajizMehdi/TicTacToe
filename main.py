# Murtajiz Mehdi
# December 14, 2021
# This is my Tic Tac Toe program,
# you should already know how to play bro.


# ---------- Global Variables Start ----------

# If you plan on adjusting these variables within a function,
# use the global keyword and then enter the variable name.

# Create the board
MyBoard = ['-', '-', '-',
           '-', '-', '-',
           '-', '-', '-']

# If game is still going
game_still_going = True

# Who won or who tied
winner = None

# Whose turn is it
current_player = "X"

# ---------- Global Variables End ----------

# This is the function that will display the board
def display_board():
    print(MyBoard[0] + ' | ' + MyBoard[1] + ' | ' + MyBoard[2])
    print(MyBoard[3] + ' | ' + MyBoard[4] + ' | ' + MyBoard[5])
    print(MyBoard[6] + ' | ' + MyBoard[7] + ' | ' + MyBoard[8])


# Main function. This is where everything will be compiled into
def play_game():
    # Displays original board
    display_board()

    # While the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')


# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(f"It is {player}'s turn.")
    position = input('Choose a position from 1-9: ')

    valid = False
    while not valid:

        while position not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            position = input('Invalid input. Choose a position from 1-9: ')

        position = int(position) - 1

        if MyBoard[position] == "-":
            valid = True
        else:
            print("You can't go there. Try again.")

    MyBoard[position] = player
    display_board()



def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # Set up global variables
    global winner

    # Check Rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

def check_rows():
    # Set up the global variable so it can run properly in this function
    global game_still_going
    # Check if any one of the rows have all the same values and aren't empty
    row_1 = MyBoard[0] == MyBoard[1] == MyBoard[2] != '-'
    row_2 = MyBoard[3] == MyBoard[4] == MyBoard[5] != '-'
    row_3 = MyBoard[6] == MyBoard[7] == MyBoard[8] != '-'
    # If any row has a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner (X or O)
    if row_1:
        return MyBoard[0]
    elif row_2:
        return MyBoard[3]
    elif row_3:
        return MyBoard[6]
    return


def check_columns():
    # Set up the global variable so it can run properly in this function
    global game_still_going
    # Check if any one of the columns have all the same values and aren't empty
    column_1 = MyBoard[0] == MyBoard[3] == MyBoard[6] != '-'
    column_2 = MyBoard[1] == MyBoard[4] == MyBoard[7] != '-'
    column_3 = MyBoard[2] == MyBoard[5] == MyBoard[8] != '-'
    # If any column has a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner (X or O)
    if column_1:
        return MyBoard[0]
    elif column_2:
        return MyBoard[1]
    elif column_3:
        return MyBoard[2]
    return


def check_diagonals():
    # Set up the global variable so it can run properly in this function
    global game_still_going
    # Check if any one of the diagonals have all the same value and isn't empty
    diagonal_1 = MyBoard[0] == MyBoard[4] == MyBoard[8] != '-'
    diagonal_2 = MyBoard[6] == MyBoard[4] == MyBoard[2] != '-'
    # If any diagonal has a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonal_1:
        return MyBoard[0]
    elif diagonal_2:
        return MyBoard[6]
    return


def check_if_tie():
    global game_still_going
    if '-' not in MyBoard:
        game_still_going = False
    return


def flip_player():
    # Global variable must be initialized in order to be mutable
    global current_player
    # Alternates players, if X went then O will go next turn
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return




play_game()