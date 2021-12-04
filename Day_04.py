# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 18:39:00 2021

@author: rist
"""

numbers = []

f = open("input.txt", "r")
numbers = f.readline().strip('\n').split(',')
numbers = [int(x) for x in numbers]

boards = []

while True:
    line = f.readline() #empty row
    if not line:
        break
    
    board = []
    for i in range(5):
        line = f.readline().strip('\n').replace('  ', ' ').split(' ')
        if '' in line:
            line.remove('')

        row = [int(x) for x in line]
        board.append(row) 
    
    boards.append(board)
    
def play_number(boards, number):
    for b, board in enumerate(boards):
        for r, row in enumerate(board):
            for i, x in enumerate(row):
                if x == number:
                    boards[b][r][i] = 'x'
                    
def check_winner(boards):
    for i, board in enumerate(boards):
        for row in board:
           if row.count('x') == 5:
               return i
        
        for j in range(5):
            col = [row[j] for row in board]
            if col.count('x') == 5:
               return i
    return -1

#Part 1
play_boards = boards.copy()
for n in numbers:
    play_number(play_boards, n)
        
    winner = check_winner(play_boards)
    if winner > -1:
        break
        
sum = 0
for row in play_boards[winner]:
    for num in row:
        if not num == 'x':
            sum += num
print(sum*n)

#Part 2
def check_winners(boards, winners):
    for i, board in enumerate(boards):
        if not i in winners:
            for row in board:
               if row.count('x') == 5:
                   winners[i] = len(winners)+1
                   break
               
        if not i in winners:           
            for j in range(5):
                col = [row[j] for row in board]
                if col.count('x') == 5:
                   winners[i] = len(winners)+1
                   break


play_boards = boards.copy()
winners ={}
for n in numbers:
    play_number(play_boards, n)
        
    check_winners(play_boards, winners)
    if len(winners) == len(play_boards):
        break
    
sum = 0
looser = -1
for key, val in winners.items():
    if val == len(winners):
        looser = key
        break
    
for row in play_boards[looser]:
    for num in row:
        if not num == 'x':
            sum += num
print(sum*n)
