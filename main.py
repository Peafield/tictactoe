row1 = [" ", "|", " ", "|", " "]
row2 = [" ", "|", " ", "|", " "]
row3 = [" ", "|", " ", "|", " "]
dotted_line = ["__________"]
board = [row1, row2, row3]


def user_position(position, timer):
    # User Position
    row = int(position[0])
    index = int(position[1])
    selected_row = board[row - 1]

    # Marker insertion logic
    if timer % 2 == 0:
        if index == 1:
            selected_row[index - 1] = "X"
        elif index == 3:
            selected_row[index + 1] = "X"
        else:
            selected_row[index] = "X"
    else:
        if index == 1:
            selected_row[index - 1] = "O"
        elif index == 3:
            selected_row[index + 1] = "O"
        else:
            selected_row[index] = "O"


def previous_position_checker(user_position):
    # Checks previous positions and returns false if already exist
    if user_position not in previous_positions:
        previous_positions.append(user_position)
    else:
        return False


def row_win_check(current_board):
    # Checks rows to see if there is a win condition
    for row in current_board:
        if (len(set(row[::2]))) == 1 and set(row[::2]) != {' '}:
            print(f"{row[0]} wins!")
            return game_is_on == False
        else:
            return False


def column_win_check():
    # Creates nested listed to check in row_win_check
    column_win = []
    i = 0
    for _ in range(len(board)):
        columns = [item[i] for item in board]
        column_win.append(columns)
        i += 2
    return column_win


def diagonal_win_check():
    # Creates nested listed to check in row_win_check
    diagonal_win = []
    left_diagonal = []
    right_diagonal = []
    position_left = 0
    position_right = -1
    for row in board:
        x = (row[position_left])
        y = (row[position_right])
        left_diagonal.append(x)
        right_diagonal.append(y)
        position_left += 2
        position_right -= 2
    diagonal_win.append(left_diagonal)
    diagonal_win.append(right_diagonal)
    return diagonal_win



print(f'{" ".join(row1)}\n{" ".join(dotted_line)}\n{" ".join(row2)}\n{" ".join(dotted_line)}\n{" ".join(row3)}\n')

previous_positions = []
round_counter = 0
game_is_on = True

while game_is_on:
    x_user_position = input("Player One: Chose where to place your X. Enter row and column number (i.e. 11): ")
    if previous_position_checker(x_user_position) == False:
        x_user_position = input("Somethings already there! Choose another spot: ")
        previous_position_checker(x_user_position)
    user_position(x_user_position, round_counter)
    if not row_win_check(board):
        if not row_win_check(column_win_check()):
            if not row_win_check(diagonal_win_check()):
                round_counter += 1
                print(
                    f'{" ".join(row1)}\n{" ".join(dotted_line)}\n{" ".join(row2)}\n{" ".join(dotted_line)}\n{" ".join(row3)}\n')
                o_user_position = input(
                    "Player Two: Chose where to place your O. Enter row and column number (i.e. 11): ")
                if previous_position_checker(o_user_position) == False:
                    o_user_position = input("Somethings already there! Choose another spot: ")
                    previous_position_checker(o_user_position)
                user_position(o_user_position, round_counter)
                if not row_win_check(board):
                    if not row_win_check(column_win_check()):
                        if not row_win_check(diagonal_win_check()):
                            round_counter += 1
    if round_counter == 9:
        print("It's a draw!")
    elif game_is_on == False:
        print("Thanks for playing!")
    else:
        print(
            f'{" ".join(row1)}\n{" ".join(dotted_line)}\n{" ".join(row2)}\n{" ".join(dotted_line)}\n{" ".join(row3)}\n')

# while game_is_on:
#     if round_counter % 2 == 0:
#         x_user_position = input("Player One: Chose where to place your X. Enter row and column number (i.e. 11): ")
#         if previous_position_checker(x_user_position) == False:
#             x_user_position = input("Somethings already there! Choose another spot: ")
#             previous_position_checker(x_user_position)
#         user_position(x_user_position, round_counter)
#         if not row_win_check(board):
#             if not row_win_check(column_win_check()):
#                 if not row_win_check(diagonal_win_check()):
#                     pass
#         round_counter += 1
#     else:
#         o_user_position = input("Player Two: Chose where to place your O. Enter row and column number (i.e. 11): ")
#         if previous_position_checker(o_user_position) == False:
#             o_user_position = input("Somethings already there! Choose another spot: ")
#             previous_position_checker(o_user_position)
#         user_position(o_user_position, round_counter)
#         if not row_win_check(board):
#             if not row_win_check(column_win_check()):
#                 if not row_win_check(diagonal_win_check()):
#                     pass
#         round_counter += 1
#     if round_counter == 9:
#         print("It's a draw!")
#     elif game_is_on == False:
#         print("Thanks for playing!")
#     else:
#         print(f'{" ".join(row1)}\n{" ".join(dotted_line)}\n{" ".join(row2)}\n{" ".join(dotted_line)}\n{" ".join(row3)}\n')
