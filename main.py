import random
import copy


def print_board(game_board: [[int, ], ]) -> None:
    """
    Print a formatted version of the game board.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    """
    for row in game_board:
        print("+----+" * 4)
        print(''.join(f"|{cell if cell else '':^4}|" for cell in row))
        print("+----+" * 4)


def generate_piece(game_board: [[int, ], ], user_input=False) -> {str: int, }:
    """
    Generates a value and coordinates for the next number to be placed on the board.
    Will raise error if the provided board is full.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :param user_input: specifies type of piece generation: random or user-specified
    :return: dictionary with the following keys: {'row': int, 'column': int, 'value': int}
    """
    empty_cells = [(y, x) for y, row in enumerate(game_board) for x, cell in enumerate(row) if not cell]
    if not empty_cells:
        raise Exception("Board Full")
    if user_input:
        return dict(zip(('column', 'row',  'value'), (int(i) for i in input("column,row,value:").split(','))))
    return dict(
        zip(('row', 'column', 'value'), (*random.choice(empty_cells), (2 if random.random() * 100 < 90 else 4))))


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    new_piece = generate_piece(game_board)
    game_board[new_piece['row']][new_piece['column']] = new_piece['value']
    new_piece = generate_piece(game_board)
    game_board[new_piece['row']][new_piece['column']] = new_piece['value']
    # TODO: generate a random piece and location using the generate_piece function
    # TODO: place the piece at the specified location
    
    # Game Loop
    while not game_over(game_board):
        print_board(game_board)
        move_input = input().lower()
        prev_board = copy.deepcopy(game_board)
        if move_input == 'q':
            break
        if move_input in ['w', 'a', 's', 'd']:
            if move_input == 'w':
                shift_up(game_board)
            elif move_input == 'a':
                shift_left(game_board)
            elif move_input == 's':
                shift_down(game_board)
            elif move_input == 'd':
                shift_right(game_board)
            if prev_board != game_board:
                new_piece = generate_piece(game_board)
                game_board[new_piece['row']][new_piece['column']] = new_piece['value']
        # TODO: UPDATE/ADD PIECE TO BOARD
        # place a random piece on the board
        # check to see if the game is over using the game_over function

        # TODO: Show updated board using the print_board function

        # TODO: GET AND EXECUTE USER MOVE
        # Take input until the user's move is a valid key
        # if the user quits the game, print Goodbye and stop the Game Loop
        # User's Move Loop:
            # Execute the user's move
            # Compare board before user's move & after user's move
                # get and execute another move if board has not changed

        # Check if the user wins
    if game_over(game_board):
        print_board(game_board)
    print("Goodbye")    
    return game_board
def shift_left(game_board):
    for row in game_board:
        shifted_row = []
        for x in row:
            if x != 0:
                shifted_row.append(x)
        for i in range(len(shifted_row) - 1):
            if shifted_row[i] == shifted_row[i + 1]:
                shifted_row[i] *= 2
                shifted_row[i + 1] = 0
        final_row = []
        for y in shifted_row:
            if y != 0:
                final_row.append(y)
        for z in range(len(row)-len(final_row)):
            final_row.append(0)
        row[:] = final_row
def shift_right(game_board):
    for row in game_board:
        shifted_row = []
        for x in row:
            if x != 0:
                shifted_row.append(x)
        for i in range(len(shifted_row) - 1, 0, -1):
            if shifted_row[i] == shifted_row[i - 1]:
                shifted_row[i] *= 2
                shifted_row[i - 1] = 0
        final_row = []
        for y in shifted_row:
            if y != 0:
                final_row.append(y)
        for z in range(len(row)-len(final_row)):
            final_row.insert(0, 0)
        row[:] = final_row
def shift_up(game_board):
    for i in range(len(game_board[0])):
        column = []
        for row in game_board:
            column.append(row[i])
        shifted_column = []
        for x in column:
            if x != 0:
                shifted_column.append(x)
        for j in range(len(shifted_column) - 1):
            if shifted_column[j] == shifted_column[j + 1]:
                shifted_column[j] *= 2
                shifted_column[j + 1] = 0
        final_column = []
        for y in shifted_column:
            if y != 0:
                final_column.append(y)
        for z in range(len(column)-len(final_column)):
            final_column.append(0)
        for row_value in range(len(game_board)):
            game_board[row_value][i] = final_column[row_value]
def shift_down(game_board):
    for i in range(len(game_board[0])):
        column = []
        for row in game_board:
            column.append(row[i])
        shifted_column = []
        for x in column:
            if x != 0:
                shifted_column.append(x)
        for j in range(len(shifted_column) - 1, 0, -1):
            if shifted_column[j] == shifted_column[j - 1]:
                shifted_column[j] *= 2
                shifted_column[j - 1] = 0
        final_column = []
        for y in shifted_column:
            if y != 0:
                final_column.append(y)
        for z in range(len(column)-len(final_column)):
            final_column.insert(0, 0)
        for row_value in range(len(game_board)):
            game_board[row_value][i] = final_column[row_value]

def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0:
                return False
            if (i < (len(game_board)-1)) and game_board[i][j] == game_board[i+1][j]:
                return False
            if (j < (len(game_board)-1)) and game_board[i][j] == game_board[i][j+1]:
                return False
            if (i > 0) and game_board[i][j] == game_board[i-1][j]:
                return False
            if (j > 0) and game_board[i][j] == game_board[i][j-1]:
                return False
            if game_board[i][j] == 2048:
                return True

    # TODO: Loop over the board and determine if the game is over
    # TODO: Don't always return false
    return True


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
