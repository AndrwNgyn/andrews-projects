#first python project -- trying to make connect four

#establishing a board for the game
#a connect 4 board consists of 7 columns and 6 rows, which can be represented using nested lists, first index would be the row, second index would be column

def make_board():
    board = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    return board


###THIS SECTION IS FOR AESTHETIC AND CLARITY
#header just makes it easier to find out "hmm which column is what number?"
def print_board(board):
    header = ' '
    for num in range(1, len(board) + 1):
        header += ' '+ str(num) +'  '
    print(header)
    print('----' * (len(board)) + '-')

#for each row (length of the inner lists), we can then section each cooridnate a spot, as well as making it easier to see the board
#nested for loops to give each element a "spot", then repeat for the rest of the rows
    for row in range(len(board[0])):
        row_with_items = ''
        for col in range(len(board)):
            row_with_items += ('| '+str(board[col][row])) + ' '
        print(row_with_items + '|')
        print('|   ' * (len(board) +1))
        


###THIS SECTION IS FOR MAKING "MOVES"
#This makes sure you're not putting a letter out of bounds of the board. The first "if" statement makes sure the column you're putting the letter in pertains to the bounds of the board
#The second "if" statement makes sure the column you put the letter in is not all filled up
def move_available(board, move):
    if move < 1 or move > (len(board)):
        return False
    if board[move-1][0] != ' ':
        return False
    return True

#Move making function
def make_move(board, column, player):
    if not move_available(board,column):
        print("Trying to place an " + player + " in column " + str(column))
        print("Make sure to pick a column between 1 and " + str(len(board)) + " that is not full")
        print()
        return False

    if player != "X" and player != "O":
        print("Make sure you're using an X or O")
        print()
        return False

    for y in range(len(board[0])-1, -1, -1):
        if board[int(column)-1][y] == ' ':
            board[column-1][y] = player
            print("Placed an " + player + " in column " + str(column))
            print()
            return True
    return False

#Now we have to see how many moves we have available - checks the number of open columns
#uses a for loop to check individually whether a column has a move available, then appends its index to the moves list
def possible_moves(board):
    moves=[]
    for i in range(1, len(board)+1):
        if move_available(board,i):
            moves.append(i)
    return moves
def game_winner(board, symbol):
    #horizontal space check = we check for EVERY row and make sure that the subsequent column (same row still) matches the symbol
    for y in range(len(board[0])):
        for x in range(len(board)-3):
            if board[x][y] == symbol and board[x+1][y] == symbol and board[x+2][y] == symbol and board[x+3][y] == symbol:
                return True

    #same principal for horizontal but checking for vertical spaces
    for x in range(len(board)):
        for y in range(len(board[0])-3):
            if board[x][y] == symbol and board[x][y+1] == symbol and board[x][y+2] == symbol and board[x][y+3] == symbol:
                return True
    #checking for diagonal spots to the right 
    for x in range(len(board)-3):
        for y in range(3, len(board[0])):
            if board[x][y] == symbol and board[x+1][y-1] == symbol and board[x+2][y-2] == symbol and board[x+3][y-3] == symbol:
                return True
    #checking kfor diagonal spots to the left 
    for x in range(len(board)):
        for y in range(len(board[0])-3):
            if board[x][y] == symbol and board[x-1][y+1] == symbol and board[x-2][y+2] == symbol and board[x-3][y+3] == symbol:
                return True

    return False

#need a function to confirm the game is over
def game_over(board):
    return game_winner(board, "X") or game_winner(board, "O") or len(possible_moves(board))==0


#this basically makes a brand new board, 7 and 6 can be modifiable to whatever size board you want
def play_game():
    #generates a brand new board 
    my_board=make_board()
    #by default, the first player is "X"
    turn = "X"  
    winner = False
    #runs while the game is not over, then constantly checks whether the game is over or not - in the meantime, the turns swap
    while(not game_over(my_board)):
        print_board(my_board)
        move = 0
        available = possible_moves(my_board)
        #gives instruction each turn, and gives you a guide as to which spots are open
        while (move not in available):
            move = int(input("It is " + turn + "'s turn. Please select a column. Your options are " + str(available) + ":"))
            make_move(my_board, move, turn)
        #this checks whether the game is over or not
        if game_winner(my_board, turn):
            print(turn + " is the winner!")
            print_board(my_board)
            winner = True
            break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    if not winner:
        print("Tie :(")
        print_board(my_board)

play_game()


#12/25 - player inputs arent shown on the board -> 12/26 resolved: needed to make function for printing board and called it at end of code



