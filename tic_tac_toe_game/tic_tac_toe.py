
def display_matrix(matrix):
    for row in matrix:
        print(row)
        
def accept_matrix_input_location(player_name):
    user_input = [-1,-1]
    user_input[0] = input(f"{player_name} Please enter row value:")
    user_input[1] = input(f"{player_name} Please enter column value:")
    if validate_user_input(user_input) == True:
        return user_input
        
def validate_user_input(user_input):
    
    if user_input[0].isdigit() == False or user_input[1].isdigit() == False:
        print("Invalid input. Please enter numeric values.")
        accept_matrix_input_location()  
          
    if int(user_input[0]) not in range(3) or int(user_input[1]) not in range(3):
        print("Invalid input. Please enter values between 0 and 2.")
        accept_matrix_input_location()

    return True

def are_row_values_same(matrix, row_index):
    if not matrix or not (0 <= row_index < len(matrix)):
        return False  # invalid index → not same
    
    row = matrix[row_index]
    if not row:
        return False

    return set(row) in [{"O"}, {"X"}]

def are_column_values_same(matrix, col_index):
    if not matrix or not matrix[0]:
        return False

    try:
        column_values = [row[col_index] for row in matrix if len(row) > col_index]
    except IndexError:
        return False

    return set(column_values) in [{"O"}, {"X"}]

def are_main_diagonal_values_same(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    diagonal_elements = [matrix[i][i] for i in range(len(matrix))]
    return set(diagonal_elements) in [{"O"}, {"X"}]

def are_anti_diagonal_values_same(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)
    anti_diagonal_elements = [matrix[i][n - 1 - i] for i in range(n)]
    return set(anti_diagonal_elements) in [{"O"}, {"X"}]

def is_matrix_full(matrix):
    return all(all(cell in ("X", "O") for cell in row) for row in matrix)

def check_winner(matrix, user_input, player_name):
    if are_row_values_same(matrix, int(user_input[0])):
        print(f"{player_name} Player wins by row match")
        return True
    
    if are_column_values_same(matrix, int(user_input[1])):
        print(f"{player_name} Player wins by column match")
        return True
    
    if are_main_diagonal_values_same(matrix):
        print(f"{player_name} Player wins by diagonal match")
        return True
    
    if are_anti_diagonal_values_same(matrix):
        print(f"{player_name} Player wins by anti-diagonal match")
        return True

def ask_player_name():
    player1 = input("Enter first player's name: ")
    if player1.strip() == "":
        print("Player1 name cannot be empty. Please enter a valid name.")
        return ask_player_name()

    player2 = input("Enter second player's name: ")
    if player2.strip() == "":
        print("Player2 name cannot be empty. Please enter a valid name.")
        return ask_player_name()

    return [player1, player2]

def main():
    matrix = [
                [' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']
            ]

    
    turn = 0
    player1_symbol = ""
    player2_symbol = ""
        
    player_name = ask_player_name()
    players = [player_name[0], player_name[1]]
    print(f'Let\'s play TIC TAC TOE GAME ({player_name[0]} vs {player_name[1]})')
    player1_symbol = input(f'{player_name[0]} Please select between X and O: ')
    
    if(player1_symbol.upper() == 'X'):
        player2_symbol = 'O'
    else:
        player2_symbol = 'X'
    
    display_matrix(matrix)
    while(True):
        user_input = accept_matrix_input_location(players[turn % 2])
        print(f"{players[turn % 2]} chose location {user_input[0]} {user_input[1]}")
        matrix[int(user_input[0])][int(user_input[1])] = player1_symbol if turn % 2 == 0 else player2_symbol
        display_matrix(matrix)
        if check_winner(matrix, user_input,players[turn % 2]) == True or is_matrix_full(matrix):
            print("Game Over")
            break
        turn += 1
        
if __name__ == "__main__":
    main()
        