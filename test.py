from tictactoe import initial_state, player, actions, result, winner, terminal, minimax

board = initial_state()

while (not terminal(board)):
    print(board)
    action = minimax(board)
    # board shouldn't be modified in minimax
    board = result(board, action)
    


    



