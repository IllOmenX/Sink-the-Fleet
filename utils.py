import numpy as np
import random

#Constants
water = '~'
board_measure = 10

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
def shoot(player: Player, board: Board):
    if player.kind == 'Human':
        row, col = [int(coord) for coord in input("Wich coords to shoot...: ").split()]
    else:
        row = random.randint(0,board_measure-1)
        col = random.randint(0,board_measure-1)
    
    if board[row, col] == 'O':
        shoot(player, board)
        
def createArmy(board: Board):
    army = []
    for i in ships.keys():
        for num in range(ships[i][0]): #0 is the num_ships
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
                    #Si row - (Ship.len -1) es menor que 0 significa que el barco se sale del Board por la parte norte
                    continue
                else:
                    #Comprobamos si se puede colocar el barco
                    for cell in range(ship.len):
                        if board[row-cell, col] == water:
                            placed = True
                            continue
                        else:
                            placed = False
                            break
                    #Si se puede colocar el barco, lo colocamos y salimos del bucle
                    if placed == True:
                        for cell in range(ship.len):
                            board[row-cell, col] = 'O'
                            ship.coordinates.append([row-cell, col]) #We append the coordinates of the ship that we just placed
                        break
                    
            elif orientation == 'E':
                
                if col + (ship.len -1) > board_measure-1:
                    #Si col + (Ship.len -1) es mayor que 9 significa que el barco se sale del Board por la parte este
                    continue
                else:
                    #Comprobamos si se puede colocar el barco
                    for cell in range(ship.len):
                        if board[row, col+cell] == water:
                            placed = True
                            continue
                        else:
                            placed = False
                            break
                    #Si se puede colocar el barco, lo colocamos y salimos del bucle
                    if placed == True:
                        for cell in range(ship.len):
                            board[row, col+cell] = 'O'
                            ship.coordinates.append([row, col+cell]) #We append the coordinates of the ship that we just placed
                        break
                    
            if orientation == 'S':
                
                if row + (ship.len -1) > board_measure-1:
                    #Si row + (Ship.len -1) es mayor que 9 significa que el barco se sale del Board por la parte sur
                    continue
                else:
                    #Comprobamos si se puede colocar el barco
                    for cell in range(ship.len):
                        if board[row+cell, col] == water:
                            placed = True
                            continue
                        else:
                            placed = False
                            break
                    #Si se puede colocar el barco, lo colocamos y salimos del bucle
                    if placed == True:
                        for cell in range(ship.len):
                            board[row+cell, col] = 'O'
                            ship.coordinates.append([row+cell, col]) #We append the coordinates of the ship that we just placed
                        break

            elif orientation == 'W':
                
                if col - (ship.len -1) < 0:
                    #Si col - (Ship.len -1) es menor que 0 significa que el barco se sale del Board por la parte oeste
                    continue
                else:
                    #Comprobamos si se puede colocar el barco
                    for cell in range(ship.len):
                        if board[row, col-cell] == water:
                            placed = True
                            continue
                        else:
                            placed = False
                            break
                    #Si se puede colocar el barco, lo colocamos y salimos del bucle
                    if placed == True:
                        for cell in range(ship.len):
                            board[row, col-cell] = 'O'
                            ship.coordinates.append([row, col-cell]) #We append the coordinates of the ship that we just placed
                        break
