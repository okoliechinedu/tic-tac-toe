players = ["X", "O"]

# Initialize the Tic Tac Toe board
main_board = [[" " for _ in range(3)] for _ in range(3)]

# Create a mapping dictionary for position numbers to indices
position_mapping = {
    "1": (0, 0), "2": (0, 1), "3": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "7": (2, 0), "8": (2, 1), "9": (2, 2)
}

# Possible Wins
TOP_ROW = [position_mapping["1"], position_mapping["2"], position_mapping["3"]]
MIDDLE_ROW = [position_mapping["4"], position_mapping["5"], position_mapping["6"]]
BOTTOM_ROW = [position_mapping["7"], position_mapping["8"], position_mapping["9"]]
LEFT_COLUMN = [position_mapping["1"], position_mapping["4"], position_mapping["7"]]
MIDDLE_COLUMN = [position_mapping["2"], position_mapping["5"], position_mapping["8"]]
RIGHT_COLUMN = [position_mapping["3"], position_mapping["6"], position_mapping["9"]]
DIAGONAL_TOP_LEFT_TO_BOTTOM_RIGHT = [position_mapping["1"], position_mapping["5"], position_mapping["9"]]
DIAGONAL_TOP_RIGHT_TO_BOTTOM_LEFT = [position_mapping["3"], position_mapping["5"], position_mapping["7"]]

current_player_index = 0
game_on = True

print("Player 1 is 'X' and Player 2 is 'O'.")


def print_board(board):
    for row in range(3):
        for col in range(3):
            cell_value = board[row][col]
            print(f"| {cell_value}", end="\t")  # Displays the board in a presentable manner to the play
        print("|\n" + "-" * 13)


def check_win(current_player, current_board):
    game_decision = True

    # horizontal wins
    if all(current_board[row_index][col_index] == current_player for row_index, col_index in TOP_ROW):
        print_board(current_board)
        print(f"{current_player} is the Winner!")
        return game_decision
    elif all(current_board[row_index][col_index] == current_player for row_index, col_index in MIDDLE_ROW):
        print_board(current_board)
        print(f"{current_player} is the Winner!")
        return game_decision
    elif all(current_board[row_index][col_index] == current_player for row_index, col_index in BOTTOM_ROW):
        print_board(current_board)
        print(f"{current_player} is the Winner!")
        return game_decision

    # vertical wins
    elif all(current_board[row_index][col_index] == current_player for row_index, col_index in LEFT_COLUMN):
        print_board(current_board)
        print(f"{current_player} is the Winner!")
        return game_decision
    elif all(current_board[row_index][col_index] == current_player for row_index, col_index in MIDDLE_COLUMN):
        print_board(current_board)
        print(f"{current_player} is the Winner!")
        return game_decision
    elif all(current_board[row_index][col_index] == current_player for row_index, col_index in RIGHT_COLUMN):
        print_board(current_board)
        print(f"{current_player} is the Winner!")
        return game_decision

    # Diagonal wins
    elif all(current_board[row_index][col_index] == current_player for row_index, col_index in DIAGONAL_TOP_LEFT_TO_BOTTOM_RIGHT):
        print_board(current_board)
        print(f"{current_player} is the Winner!")
        return game_decision
    elif all(current_board[row_index][col_index] == current_player for row_index, col_index in DIAGONAL_TOP_RIGHT_TO_BOTTOM_LEFT):
        print_board(current_board)
        print(f"{current_player} is the Winner!")
        return game_decision

    # check for draw
    sample_list = []
    for key, values in position_mapping.items():
        sample_list.append(values)
    if all(cell != " " for row_index, col_index in sample_list for cell in current_board[row_index][col_index]):
        print_board(current_board)
        print("It's a draw")
        return game_decision


while game_on:
    print_board(main_board)
    user_input = input(f"Player {players[current_player_index]}, What position do you want to play on the board?")

    # checks for valid user input
    if int(user_input) in range(1, 10):
        player = players[current_player_index]  # selects current players
        row_, col_ = position_mapping[user_input]

        # checks if a position is already filled
        if players[0] in main_board[row_][col_] or players[1] in main_board[row_][col_]:
            current_player_index = (current_player_index + 1) % len(players)
            print("Position already Taken!")
        else:
            main_board[row_][col_] = player
            decision = check_win(player, main_board)
            if decision:
                game_on = False
    else:
        print("Select a number between 1 and 9")
        current_player_index = (current_player_index + 1) % len(players)

    current_player_index = (current_player_index + 1) % len(players)  # Toggle between players
