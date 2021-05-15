import socket


board = [' ' for x in range(10)]

FORMAT = 'utf-8'
SERVER = input('What is the server IP?')
PORT = int(input('What is the server PORT?'))
NAME = input("What should I call you?")
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print('[CONNECTION] connected successfully')


def insertletter(letter,pos):
    board[pos] = letter

def IsSpaceFree(pos):
    return board[pos] == ' '
            
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
                    return move
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

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(2048 - len(send_length))
    client.send(send_length)
    client.send(message)

def MYTURN():
    if not (IsWinner(board, 'O')):
        move = PlayerMove()
        send(str(move))
        PrintBoard(board)
    else:
        print("O\'s won!")


def main():
    print("Welcome to Tic Tac Toe !")
    while not (IsBoardFull(board)):
        while True:
            msg = client.recv(2048).decode(FORMAT)
            if msg == 'YOURTURN':
                MYTURN()
            else:
                if not (IsWinner(board, 'X')):
                    insertletter('O',int(msg))
                else:
                    print("X\'s won!")


    if IsBoardFull(board):
        print("Tie Game!")



main()