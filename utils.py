import numpy as np
import random

#Constants
board_measure = 10
water = '¬'
fail = '~'
boat = 'O'
boat_hit = 'X'
#Dictionary
#Each ship is separated as ship_kind: (num_ships, len_ship)
ships = {'Little' : (4, 1),
         'Medium' : (3, 2),
         'Big'    : (2, 3),
         'Bigass' : (1, 4)}

#Classes
class Player:
    def __init__(self, kind):
        self.kind = kind

class Board:
    def __init__(self, measure = board_measure):
        self.measure = (board_measure, board_measure)
        
    def createBoard():
        return np.full((board_measure, board_measure), water)
    
    

class Ship:
    def __init__(self, name, kind):
        self.name = name
        self.len = ships[kind][1]
        self.coordinates = []
        
#Methods
def endGame(board1: Board, board2: Board):
    if boat in board1:
        print('Player Wins')
        exit() #Game has ended we finish the game
    else:
        print('Machine Wins')
        exit() #Game has ended we finish the game
        
def menu():
    print('''What you what to do?:
          1. Shoot
          2. Look at your board
          3. Look enemy board
          4. Exit''')


def shoot(player: Player, board: Board):
    if player.kind == 'Human':
        while 1:#Loop1 to make sure that the coords are inside the board
            while 1:#Loop2 to make sure the coord format is well done
                try:
                    row, col = [int(coord) for coord in input("Wich coords to shoot, separated with a space...: ").split()]
                    break #Loop2
                except ValueError:
                    print('Wrong coord format')
            if (row < 0 or row > 9) or (col < 0 or col > 9):
                print('Coords not in board, try again...')
            else:
                break #Loop1
    else: #Machine shoot, random
        row = random.randint(0,board_measure-1)
        col = random.randint(0,board_measure-1)
    
    if board[row, col] == boat:
        print("You hit a ship")
        board[row, col] = boat_hit #Ship hitted we turn O into X
        #Maybe that was the last shoot the player needed to destroy all ships, let's check and finish if there are not more ships
        if boat not in board:
            endGame()
        #If there are still more boats we continue
        shoot(player, board)
    elif board[row, col] == water: #Water hit
        print("You hit the water")
        board[row, col] = fail
    elif board[row, col] == boat_hit or board[row, col] == fail:
        print('You already shooted there. Try again...')
        shoot(player, board)
        
def createArmy(board: Board):
    army = []
    for i in ships.keys():
        for num in range(ships[i][0]): #0 is the num_ships in the ships dict
            new_ship = Ship(i + str(num), i)
            placeShip(new_ship, board)
            army.append(new_ship)
    return army

def placeShip(ship: Ship, board: Board):
    placed = False
    all_orientation = ['N', 'E', 'S', 'W']
    
    while not placed:
        row = random.randint(0,board_measure-1)
        col = random.randint(0,board_measure-1)
        orientation = random.choice(all_orientation)
        
        if board[row, col] == water:
            
            if orientation == 'N':
                
                if row - (ship.len -1) < 0:
                    #If row - (ship.len -1) is less than 0 it means that the ship goes off the board on the north side
                    continue
                else:
                    #We check if the ship can be placed
                    for cell in range(ship.len):
                        if board[row-cell, col] == water:
                            placed = True
                            continue
                        else:
                            placed = False
                            break
                    #If the ship can be placed, we place it and exit the loop
                    if placed == True:
                        for cell in range(ship.len):
                            board[row-cell, col] = boat
                            ship.coordinates.append([row-cell, col]) #We append the coordinates of the ship that we just placed
                        break
                    
            elif orientation == 'E':
                
                if col + (ship.len -1) > board_measure-1:
                    #If col + (ship.len -1) is more than 9 it means that the ship goes off the board on the east side
                    continue
                else:
                    #We check if the ship can be placed
                    for cell in range(ship.len):
                        if board[row, col+cell] == water:
                            placed = True
                            continue
                        else:
                            placed = False
                            break
                    #If the ship can be placed, we place it and exit the loop
                    if placed == True:
                        for cell in range(ship.len):
                            board[row, col+cell] = boat
                            ship.coordinates.append([row, col+cell]) #We append the coordinates of the ship that we just placed
                        break
                    
            if orientation == 'S':
                
                if row + (ship.len -1) > board_measure-1:
                    #If row + (ship.len -1) is more than 9 it means that the ship goes off the board on the south side
                    continue
                else:
                    #We check if the ship can be placed
                    for cell in range(ship.len):
                        if board[row+cell, col] == water:
                            placed = True
                            continue
                        else:
                            placed = False
                            break
                    #If the ship can be placed, we place it and exit the loop
                    if placed == True:
                        for cell in range(ship.len):
                            board[row+cell, col] = boat
                            ship.coordinates.append([row+cell, col]) #We append the coordinates of the ship that we just placed
                        break

            elif orientation == 'W':
                
                if col - (ship.len -1) < 0:
                    #If col - (ship.len -1) is less than 0 it means that the ship goes off the board on the west side
                    continue
                else:
                    #We check if the ship can be placed
                    for cell in range(ship.len):
                        if board[row, col-cell] == water:
                            placed = True
                            continue
                        else:
                            placed = False
                            break
                    #If the ship can be placed, we place it and exit the loop
                    if placed == True:
                        for cell in range(ship.len):
                            board[row, col-cell] = boat
                            ship.coordinates.append([row, col-cell]) #We append the coordinates of the ship that we just placed
                        break
