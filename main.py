import socket


board = [' ' for x in range(10)]


def insertletter(letter,pos):
    board[pos] = letter

def IsSpaceFree(pos):
    return board[pos] == ' '
def SORC():
    run = True
    while run:
        INPUT = input('Do you want to connect someone or be a server?[C/S]')
        if (INPUT == 'C'or INPUT=='c' or INPUT =='S' or INPUT == 's'):
            return INPUT
        else:
            pass
            
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
        return False
    else:
        return True


def game():
    while not (IsBoardFull(board)):
        if not (IsWinner(board, 'X')):
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


def main():
    print("Welcome to Tic Tac Toe !")
    CONNECTION  =  SORC()
    if CONNECTION == 'S' or CONNECTION == 's':
        print('[STARTING] server is starting....')
        PORT = 2412
        SERVER = socket.gethostbyname(socket.gethostname())
        ADDR = (SERVER, PORT)
        FORMAT = 'utf-8'
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        print(f'[LISTENING] Sever is listening on {SERVER}')
        NAME = input("What should I call you?")
        while True:
            conn ,addr = server.accept()
            print(f'[NEW CONNECTION] {addr} conneted')
            game()





    elif CONNECTION == 'C' or CONNECTION == 'C':
        pass


main()