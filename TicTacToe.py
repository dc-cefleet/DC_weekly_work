# this function is continually called by the game running function to update the board
def display_board(moves):
# '''
# Inputs: 9 postions on board. Left to right. Top to bottom form(X/O/#)
# Input ex. # moves = ['X', 'O','X', 'O','X', 'O','X', '','X']
# Outputs: Prints a board filled with Xs/Os/_s
# Functionality: working
# '''
    print(f' {moves[0]} | {moves[1]} | {moves[2]} \n__________\n {moves[3]} | {moves[4]} | {moves[5]} \n __________\n {moves[6]} | {moves[7]} | {moves[8]}')

    # this function runs the game. it will set up the game and walk the user through it
def run_game():
    # Player one is Xs
    # Player two is Os
    # initialize moves array
    moves = []
    [moves.append('') for x in range(0,9)]
    count = 0
    player_flip = True
    while count < 40: # eventually, run until a return condition is met
        if player_flip:
            index = int(input('Player 1, what is your move? '))
            if index not in range(0,9):
                print('Input must be a digit between 0-8')
                continue
            if (moves[index] == ''):
                moves[index] = 'X'
            else: 
                print('A move has already been played here.')
                continue
        else:
            index = int(input('Player 2, what is your move? '))
            if index not in range(0,9):
                print('Input must be a digit between 0-8')
                continue
            if (moves[index] == ''):
                moves[index] = 'O'
            else: 
                print('A move has already been played here.')
                continue
    # check to see if game is over
        if winner(moves, 'X'):
            display_board(moves)
            print('Congrats Player 1! You win!')
            return
        elif winner(moves, 'O'):
            display_board(moves)
            print('Congrats Player 2! You win!')
            return
        if '' not in moves:
            display_board(moves)
            print('The game finished with no winner... Try harder next time.')
            return
        player_flip = not player_flip
        count+=1 # to prevent infinite loop while testing
        display_board(moves)
    return
        
def winner(moves, char):
    #horizontal row 1
    if (moves[0]==char and moves[1]==char and moves[2]==char):
        return True
    #horizontal row 2
    if (moves[3]==char and moves[4]==char and moves[5]==char):
        return True
    #horizontal row 3
    if (moves[6]==char and moves[7]==char and moves[8]==char):
        return True
    #vertical 1
    if (moves[0]==char and moves[3]==char and moves[6]==char):
        return True
    #vertical 2
    if (moves[1]==char and moves[4]==char and moves[7]==char):
        return True
    #vertical 3
    if (moves[2]==char and moves[5]==char and moves[8]==char):
        return True
    #diagonal 1
    if (moves[0]==char and moves[4]==char and moves[8]==char):
        return True
    #diagonal 2
    if (moves[2]==char and moves[4]==char and moves[6]==char):
        return True