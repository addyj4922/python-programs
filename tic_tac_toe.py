from os import system
import random as r
print("Welcome to Tic-Tac-Toe!")

def display_board(board):
    #system('cls')
    print()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

#test_board=['a','X','O','X','O','X','O','X','O','X']

def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input("Player 1: Choose X or O: ").upper()
    if marker=='X':
        return('X','O')
    else:
        return ('O','X')


def place_marker(board,marker,position):
    board[position]=marker
#place_marker(test_board,'@',1)
#display_board(test_board)


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))
#display_board(test_board)
#print(win_check(test_board,'X'))


def choose_first_player():
    toss= r.randint(0,1)
    if toss==0:
        return 'Player 1'
    else:
        return 'player 2'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False #BOARD IS NOT FULL
    return True #BOARD IS FULL


def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("choose position between (1-9): "))
    return position


def replay():
    choice=input("Do you want to play again?\n If Yes press Y else for No press N").upper()
    return choice=='Y'


while True:

    the_board=[' ']*10
    player1_marker,player2_marker=player_input()

    turn = choose_first_player()
    print(turn + ' Goes 1st')
    play_game=input("Ready to play? Y or N?\n").upper()
    if play_game=="Y":
        game_on=True
    else:
        game_on=False

    #GAME PLAY
    while game_on:
        if turn == 'Player 1':
            #SHOW THE BOARD
            display_board(the_board)
            #CHOOSE A POSITION
            position=player_choice(the_board)
            #PLACE THE MARKER ON THAT POSITION
            place_marker(the_board,player1_marker,position)
            #CHECK IF THEY WON
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 WINS!!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("THERE IS A TIE!!!")
                    break
                else:
                    turn='Player 2'
            #OR CHECK IF THERE IS A TIE
            #AND IF  THERE IS NO TIE AND NO WIN THEN NEXT PLAYER'S TURN

        else:
            # SHOW THE BOARD
            display_board(the_board)
            # CHOOSE A POSITION
            position = player_choice(the_board)
            # PLACE THE MARKER ON THAT POSITION
            place_marker(the_board, player2_marker, position)
            # CHECK IF THEY WON
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 WINS!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("THERE IS A TIE")
                    break
                else:
                    turn = 'Player 1'
            # OR CHECK IF THERE IS A TIE
            # AND IF  THERE IS NO TIE AND NO WIN THEN NEXT PLAYER'S TURN
    if not replay():
        break