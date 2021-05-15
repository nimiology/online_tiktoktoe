import socket


board = [' ' for x in range(10)]

def insertletter(letter,pos):
    board[pos] = letter

def IsSpaceFree(pos):
    return board[pos] == ' '
def SORC():
    RUN = True
    while RUN:
        INPUT = input('Do you want to connect someone or be a server?[C/S]')
def PrintBoard(board):
    print('   |   |')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('   |   |')

def IsWinner(board, letter):
    return (board[1] == letter and board[2] == letter and board[1] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)

def PlayerMove():
    run = True
    while run:
        move = input('Please select position to place \'X\' (1-9):')
        try:
            move = int(move)
            if move > 0 and move<10 :
                if IsSpaceFree(move):
                    run = False
                    insertletter('X', move)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print('Please type number within the range!')
        except:
            print("Please write a number!")

def IsBoardFull(Board):
    if Board.count(" ") > 1:
        return True
    else:
        return False

def main():
    print("Welcome to Tic Tac Toe !")
    CONNECTION  =  SORC()
    while not (IsBoardFull(board)):
        if not (IsWinner(board,'X')):
            PlayerMove()
            PrintBoard(board)
        else:
            print("X\'s won!")
            break

        if not (IsWinner(board, 'O')):
            pass
        else:
            print("O\'s won!")
            break
    if IsBoardFull(board):
        print("Tie Game!")

