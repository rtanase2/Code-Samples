__author__ = 'Rachelle Tanase'

def generate_maze(size):
    board = ['#'*size]*size
    return board

def print_maze(board):
    for row in board:
        print row

def main():
    print("Welcome to my maze generator!")
    print("Type \"quit\" at any time to quit the program.")
    while(True):
        board_size = raw_input("Enter board size: ")
        if board_size == "quit":
            break;
        else:
            if not board_size.isdigit():
                print("Please enter number or \"quit\".")
            else:
                board_size = int(board_size)
                print_maze(generate_maze(board_size))

if __name__ == '__main__':
    main()