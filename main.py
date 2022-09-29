import utils as u
import numpy as np
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
    machine = u.Player('Machine')
    
    #Create the boards
    board = u.Board
    my_board = board.createBoard()
    enemy_board = board.createBoard()

    #Create army on the board
    my_ships = u.createArmy(my_board)
    enemy_ships = u.createArmy(enemy_board)
    
    #Game start...
    while (u.boat in my_board and u.boat in enemy_board):
        #My Turn
        while 1:
            u.menu()
            while 1:
                try:
                    option = int(input("Choose option: "))
                    break
                except ValueError:
                    print("Invalid option")
                    pass
            if option == 1:
                u.shoot(player ,enemy_board)
                break
            elif option == 2:
                print(my_board)
                continue
            elif option == 3:
                print(enemy_board) #If you want to see the enemy ships coords
                #print(np.char.replace(enemy_board,'O',u.water))
                continue
            elif option == 4:
                exit()
            else:
                print("Option unrecognized")
                continue
        
        #Enemy turn
        print('Enemy turn...')
        u.shoot(machine, my_board)
        
    #End Game
    u.endGame(my_board, enemy_board)