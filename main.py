import utils as u
'''
¿Why 
board = u.Board
my_board = board.createBoard(board)
enemy_board = board.createBoard(board)
? self**
'''
if __name__ == '__main__':
    #Create the players (Human vs Machine)
    player = u.Player('Human')
    machine = u.Player
    
    #Create the boards
    board = u.Board
    my_board = board.createBoard()
    enemy_board = board.createBoard()

    #Create army on the board
    my_ships = u.createArmy(my_board)
    enemy_ships = u.createArmy(enemy_board)
    
    #Game start...
    while ('O' in my_board or 'O' in enemy_board):
        #My turn
        u.shoot(player ,enemy_board)
        
        #Enemy turn
        print('Enemy turn...')
        u.shoot(machine, my_board)

    print(my_board)