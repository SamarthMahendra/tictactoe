# tictactoe
tictoegame using minimax algorithm and 2d animation using matplotlib

library used:
-emoji
-random
-time
-matplotlib

functions:
  inputhuman():
    takes input from the user, the co-ordinates, check if its valid move.
    if its valid move then inserts the move into the matrix
  computerplay():
    tries out all the possiblities using minimax algorithm and then plays the optimal solution
  display():
    using matplotlib plots the matrix i.e status of the game after each play
