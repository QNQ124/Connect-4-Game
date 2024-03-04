# Function to check the validity of a number of column
def check_number(number):
    while True:
        try:
            value = int(input(number)) - 1
            if value in [0, 1, 2, 3, 4, 5, 6]:
                return value
        except ValueError:
            print("----------------- invalid number -----------------")

# Function for check if there exist one player win
def check_winner(list, symbol):
    # check row
    for i in range(6):
        for j in range(4):
            if all(list[i][j + s] == symbol for s in range(4)):
                return True

    # check column
    for i in range(7):
        for j in range(3):
            if all(list[j + s][i] == symbol for s in range(4)):
                return True

    # check diagonal
    for i in range(3):
        for j in range(4):
            if all(list[i + s][j + s] == symbol for s in range(4)):
                return True
        for j in range(6, 2, -1):
            if all(list[i + s][j - s] == symbol for s in range(4)):
                return True
    return False


# Main function
def main():

    # welcome message and explain the game
    print("=-------------- Welcome to Connect-4 game ---------------=")
    print("Connect- 4 game. A board of 7 columns x 6 rows is--------=\n"
          "displayed that is held up in physical game as in---------=\n"
          "figure below with row 1 is the bottom row: Players-------=\n"
          "choose a symbol, either X or O. In their turn, they------=\n"
          "drop the symbol from top of the board (number 6) until---=\n"
          "it settles in the bottom empty cell.The first player to--=\n"
          "connect 4 symbols horizontally, vertically or diagonally-=\n"
          "wins until it settles in the bottom empty cell-----------=\n")

    # initial list for game
    list = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    # print list for players
    for i in list:
        print(i)
    # variable for player_1 symbol in game
    player_1_symbol = input("Please choose the first symbol X or O: ").upper()
    while player_1_symbol not in ['X', 'O']:
        player_1_symbol = input("Please choose the first symbol X or O: ").upper()

    # after player_1 choose his symbol put automatically another symbol to player_2
    if player_1_symbol == 'X':
        player_2_symbol = 'O'
    else:
        player_2_symbol = 'X'
    print()

    # Game playing
    player = 1
    while True:
        for i in list:
            print(i)

        # check if a number of column in [1, 2, 3, 4, 5, 6, 7] or not
        column = check_number(f"Player {player}, please enter a column number from 1 to 7: ")

        # check if column is empty or not
        while all(list[row][column] != ' ' for row in range(5, -1, -1)):
            column = int(input(f"Player {player}, Column is not empty. Please choose another column: ")) - 1

        # Update the list with the player's symbol in chosen column
        for row in range(5, -1, -1):
            if list[row][column] == ' ':
                list[row][column] = player_1_symbol if player == 1 else player_2_symbol
                break

        # Check if there exist one player win
        if check_winner(list, player_1_symbol if player == 1 else player_2_symbol):
            for i in list:
                print(i)
            print()
            print(f"Player {player} wins!")
            break

        # Check if all elements of the list is full and there is no winner
        if all(all(i != ' ' for i in j) for j in list):
            for i in list:
                print(i)
            print()
            print("It's a draw!")
            break

        # Switch player to play his turn
        if player == 1:
            player = 2
        else:
            player = 1


main()
