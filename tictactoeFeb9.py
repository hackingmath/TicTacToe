'''Tic Tac Toe
Leading to AI?
with Curtis Feb 9, 2018'''

import random

class Board(object):
    def __init__(self):
        self.spaces = ['_','_','_','_','_','_','_','_','_']
        self.movesList = []

    def sampleBoard(self):
        print("Here are the numbers for the squares:")
        print('     |     |     ')
        print(' ',0,' | ',1,' | ',2)
        print('_____|_____|_____')
        print('     |     |     ')
        print(' ',3,' | ',4,' | ',5)
        print('_____|_____|_____')
        print('     |     |     ')
        print(' ',6,' | ',7,' | ',8)
        print('     |     |     ')
        print()

    def applyMove(self):
        for i,move in enumerate(self.movesList):
            if i % 2 == 0:
                self.spaces[move] = 'X'
            else:
                self.spaces[move] = 'O'

    def display(self):     
        print('     |     |     ')
        print(' ',self.spaces[0],' | ',self.spaces[1],' | ',self.spaces[2])
        print('_____|_____|_____')
        print('     |     |     ')
        print(' ',self.spaces[3],' | ',self.spaces[4],' | ',self.spaces[5])
        print('_____|_____|_____')
        print('     |     |     ')
        print(' ',self.spaces[6],' | ',self.spaces[7],' | ',self.spaces[8])
        print('     |     |     ')


def getMove(movesList):
    human_move = input("What's your move? ")
    while human_move not in '012345678' or int(human_move) in movesList:
        print("Invalid move!")
        human_move = input("What's your move? ")
    return int(human_move)

def computerMove(boardList,spaces):
    '''Computer chooses from list of possible moves'''
    #check for computer win on next move:
    for n in range(9):
        spaces2 = list(spaces)
        if n in boardList:
            continue
        spaces2[n] = 'O'
        #print(spaces2)
        if checkWin('O',spaces2):
            return n
    #check for human win on next move:
    for n in range(9):
        spaces2 = list(spaces)
        if n in boardList:
            continue
        spaces2[n] = 'X'
        #print(spaces2)
        if checkWin('X',spaces2):
            return n
    #check for the trick
    if checkTrick(spaces):
        return random.choice([1,3,5,7])
    #pick the center square
    if 4 not in boardList:
        return 4
    #pick a corner
    corners = [0,2,6,8]
    for c in corners:
        if c in boardList:
            corners.remove(c)
    if len(corners):
        move = random.choice(corners)
        return move
    #otherwise, move randomly
    move = random.choice(0,8)
    while move in boardList:
        move = random.randint(0,8)
    return move

def checkWin(player,boardList):
    '''Checks if player has won'''
    wins = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]
    for w in wins:
        if boardList[w[0]] == boardList[w[1]] == boardList[w[2]] == player:
            return True
    return False

def checkTrick(boardList):
    '''Check for the double wing trick'''
    if (boardList[0] == 'X' and boardList[8] == 'X') or \
       (boardList[2] == 'X' and boardList[6] == 'X'):
        return True
    

def humanWon():
    print("You got lucky. You won!")

def computerWon():
    print("I won! Computers really ARE superior!")

def tie():
    print("It's a tie.")

def askReplay():
    replay = input("Play again? y/n ")
    return replay.lower() == 'y'

def main():
    playing = True
    #playing loop
    while playing:
        #create board
        board1 = Board()
        #display sample board
        #board1.sampleBoard()
        #single game loop:
        game = True
        while game:
            #display sample board
            board1.sampleBoard()
            #get human's move
            human = getMove(board1.movesList)
            #put in moves list
            board1.movesList.append(human)
            #update board
            board1.applyMove()
            #check for human win
            if checkWin('X',board1.spaces):
                board1.display()
                humanWon()
                
                break
            #check for end of game
            if len(board1.movesList) == 9:
                tie()
                break
            #get computer's move:
            computer = computerMove(board1.movesList,board1.spaces)
            #put in moves list
            board1.movesList.append(computer)
            #update board
            board1.applyMove()
            #display board
            board1.display()
            
            #check for computer win
            if checkWin('O',board1.spaces):
                computerWon()
                break
            
        if not askReplay():
            playing = False


main()
