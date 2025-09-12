
def display_matrix(matrix):
    for row in matrix:
        print(row)
        
def accept_user_input():
    user_input = [-1,-1]
    user_input[0] = input("Please enter row value:")
    user_input[1] = input("Please enter column value:")
    if validate_user_input(user_input) == True:
        return user_input
        
def validate_user_input(user_input):
    
    if user_input[0].isdigit() == False or user_input[1].isdigit() == False:
        print("Invalid input. Please enter numeric values.")
        accept_user_input()  
          
    if int(user_input[0]) not in range(3) or int(user_input[1]) not in range(3):
        print("Invalid input. Please enter values between 0 and 2.")
        accept_user_input()

    return True

def are_row_values_same(matrix, row_index):
    if not matrix:
        return True  # An empty matrix or row is considered to have same values
    if not matrix[row_index]:
        return True # An empty row is considered to have same values

    # Convert the row to a set and check its length
    return len(set(matrix[row_index])) == 1

def are_column_values_same(matrix, col_index):
    if not matrix or not matrix[0]:
        return True # An empty matrix or column is considered to have same values

    # Extract the column values
    column_values = [row[col_index] for row in matrix]

    # Convert the column values to a set and check its length
    return len(set(column_values)) == 1

def are_main_diagonal_values_same(matrix):
    """Checks if all values in the main diagonal of a square 2D list are the same."""
    if not matrix or len(matrix) != len(matrix[0]):
        return False  # Handle empty or non-square matrix

    diagonal_elements = [matrix[i][i] for i in range(len(matrix))]
    return len(set(diagonal_elements)) == 1

def check_winner(matrix, user_input):
    if are_row_values_same(matrix, int(user_input[0])):
        print("Player wins by row match")
        return True
    if are_column_values_same(matrix, int(user_input[1])):
        print("Player wins by column match")
        return True
    if are_main_diagonal_values_same(matrix):
        print("Player wins by diagonal match")
        return True
def main():
    matrix = [
                [' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']
            ]
    display_matrix(matrix)
    while(True):
        user_input = accept_user_input()
        print("Input Received: ",user_input)
        matrix[int(user_input[0])][int(user_input[1])] = 'X'
        display_matrix(matrix)
        if check_winner(matrix, user_input) == True:
            print("Game Over")
            break
        user_resp = input("Do you want to continue the game? (y/n): ")
        if user_resp.lower() != 'y':
            break
        
if __name__ == "__main__":
    main()
        