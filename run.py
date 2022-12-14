from players import User, Computer


class Game:
    """
    Main class for the game baord to be played and some logic
    """
    def __init__(self):
        """
        Function to create the game board
        Create the list with length 9 that represents
        a 3x3 game board
        """
        self.board = [' ' for _ in range(9)]

        # Variable to keep track of who the current winner is
        self.current_winner = None

    def show_board(self):
        """
        Function that will show the board on
        the command line
        """
        # a for loop for i in range of 3, which 3 spaces
        # are chosen which represents the row indices i.e first row = 012
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            # String concatentation to print vertical lines
            # for the game board for each row
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def show_board_layout():
        """
        Function to show which numbers are at which spot on the board
        i.e 0|1|2. Board layout to be populated with a string for each
        i in the range of the board size, create 3 sub-arrays
        """
        game_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]

        # for loop to add the 3 rows of the board and add columns lines
        for row in game_board:
            # String concatentation to print vertical lines
            # for the game board for each row
            print('| ' + ' | '.join(row) + ' |')

    def player_move(self, square, player):
        """
        Function to check if the chosen move is valid, to then make
        the move i.e place a letter in a box and if the move is good
        it is to return true, if the move is invalid it will return false
        """
        # if statement to check if the selected box is empty (available)
        if self.board[square] == ' ':
            # If the square is empty then assign the players x or o
            self.board[square] = player

            # if statement to check if there is a winner of the game
            # by passing in last move for the check
            if self.game_winner(square, player):
                # Assign the player to current winner if thats the case
                self.current_winner = player
            return True
        return False

    def game_winner(self, square, player):
        """
        Function to check if a player has 3 in a row anywhere on the board.
        This could be in any row, column or diagonal
        """
        row_index = square // 3

        # Get the row from the row_index
        row = self.board[row_index*3:(row_index + 1) * 3]

        # if all == True then return True, otherwise it's Falses
        # with string comprehension,Check for whether that space == player
        # in the row chosen
        if all([space == player for space in row]):
            return True

        # Check the columns for if a player has 3 in a row
        column_index = square % 3

        # For each row, add the column index to get the value in the column
        # Column is to get eerything in the column the player has moved to
        # and then add to a list
        column = [self.board[column_index+i*3] for i in range(3)]

        # if all == True then return True, otherwise it's Falses
        # with string comprehension,Check for whether that space == player
        # in the column chosen
        if all([space == player for space in column]):
            return True

        # Check the diagonal for if a player has 3 in a row, the only
        # way a diaganol could win is if an even box is used (0,2,4,6,8)
        # one diagonal is 0,4 8 and the other is 2,4,6
        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            # If every chosen box == players selection then return True
            # for diagonal_1
            if all([space == player for space in diagonal_1]):
                return True

            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([space == player for space in diagonal_2]):
                return True

        # if all of these checks fail then there is no winner
        # and we return False to continue the game
        return False

    def available_selection(self):
        """
        Function to check if there are any avaialble selections for the
        game player to make. available selection is to be returned a
        boolean (true or false) of whether they are indeed available selections
        """
        return ' ' in self.board

    def available_selections_left(self):
        """
        Function to return the number of empty squares left on the game board
        """
        return self.board.count(' ')

    def player_moves_available(self):
        """
        Function to return a list of indices of the available moves
        for a player after they have made a move
        """
        # Empty list to add moves to
        moves = []

        # Add enumerate to create a list and assign tuples that have
        # the index and the value at the index i.e 0,X 1,X
        for (i, place) in enumerate(self.board):

            # For loop to go through each tuple and assign first item to i
            # and the second item to 'place'. if place empty space
            # then its an available move, then add i to the list
            if place == ' ':
                moves.append(i)
        return moves


def play_game(game, player_x, player_o, print_game=True):
    """
    Function for the game to play and pass it the arguments of game,
    and players for x & o. The extra variable for print is included so
    if it is set to True it prints out all steps for the user to
    play the game. This function is to iterate continually until
    there are no more moves left i.e someone wins or ties
    """
    if print_game:
        # Printing the board so the user can see which numbers
        # are in which position on the board
        print("Welcome to Noughts and Crosses")
        print("""
        |          |
        |          |
  ______|__________|_______
        |          |
        |          |
        |          |
        |          |
  ______|__________|_______
        |          |
        |          |
        """)
        print('Lets play a game! \n')
        game.show_board_layout()
        print('')

    # Assigns the starting letter as "X"
    player = 'X'

    # Keep iterating through the game while there are moves available
    while game.available_selection():
        # make sure the correct player is making the next move, if letter
        # is O then ask O to make move, otherwise its X
        if player == 'O':
            square = player_o.get_next_move(game)
        else:
            square = player_x.get_next_move(game)

        # Takes the available squares and player letter as arguments
        if game.player_move(square, player):
            if print_game:
                print(player + f' made a move to {square}')
                print('')
                # Print updated board including the users move
                game.show_board()

            # if the current winner is not set to None anymore, then
            # a player has won the game
            if game.current_winner:
                if print_game:
                    print(player + " has won!")
                return player

            # To alternate players throughout the game
            # We assign player as == to O if the last
            # player was x, otherwise we assign it to x
            if player == 'X':
                player = "O"
            else:
                player = "X"

    # If statement for once the game goes through the
    # while loop, if the game finishes with a draw it'll
    # be printed to the interface
    if print_game:
        print('This game is a draw!')


if __name__ == "__main__":
    # Assign the User to play with the letter X
    player_x = User('X')

    # Assign the Computer to play with the letter O
    player_o = Computer('O')

    # play is assigned an instance of the game play
    p = Game()

    play_game(p, player_x, player_o, print_game=True)
