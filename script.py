from tic_tac_toe import *

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

print_board(board)
while not game_is_over(board):
    move1 = eval(input("You are X. Write the number of field that you want to play on (write e to exit): "))
    if move1 == "e":
        break
    select_space(board, move1, "X")
    print("\nYou played...\n")
    print_board(board)
    print("\nComputer is playing\n")
    select_space(board, minimax(board, False)[1], "O")
    print_board(board)
    if game_is_over(board):
        if has_won(board, "X"):
            print("\nCongratulations!!!\nYou won!\n")
        elif has_won(board, "O"):
            print("\nGame over. You lost... \n Don't worry. Better luck next time!\n")

            



