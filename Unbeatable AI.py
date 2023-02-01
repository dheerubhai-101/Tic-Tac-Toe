# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:12:04 2021

@author: dheeraj
"""

import pygame
import numpy as np
import math
import random

pygame.init()

W=600
H=600
BG_Colour=(28,170,156)
LINE_COLOUR=(23,145,135)
LINE_WIDTH=10
col_X=(66,58,70)
col_O=(240,238,252)
screen= pygame.display.set_mode((W,H))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_Colour)

ai=1
human=2
player=ai

b_rows=3
b_columns=3
board= np.zeros((b_rows,b_columns))


print(board)

def draw_board():
    pygame.draw.line( screen,LINE_COLOUR, (0,200),(600,200), LINE_WIDTH)
    pygame.draw.line( screen,LINE_COLOUR, (0,400),(600,400), LINE_WIDTH)
    pygame.draw.line( screen,LINE_COLOUR, (200,0),(200,600), LINE_WIDTH)
    pygame.draw.line( screen,LINE_COLOUR, (400,0),(400,600), LINE_WIDTH)

draw_board()

def draw_O(col,row):
    #for row in range(b_rows):
     #   for col in range(b_columns):        
    pygame.draw.circle( screen,col_O,(int(col*200 + 100),int(row*200+100)),50,15)
           
            
    
def draw_X(col,row):
    #for row in range(b_rows):
     #   for col in range(b_columns):
    pygame.draw.line( screen,col_X,(col*200+50,row*200+150),(col*200+ 150,row*200+50),20)
    pygame.draw.line( screen,col_X,(col*200+50,row*200+50),(col*200+150,row*200+150),20)
    
    

def free_space(row,col):
    if board[row][col]==0:
        return True
    else:
        return False
   
def mark_square(row,col,player):
    if free_space(row,col):
        board[row][col]= player

def full_board():
    for row in range(b_rows):
        for col in range(b_columns):
            if board[row][col]==0:
                return False
    return True

def check_win(player):
    #vertical check
    for col in range(b_columns):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col]==player:
            return True
        
    #horizonatal check
    for row in range(b_rows):
        if board[row][0]==board[row][1]==board[row][2] and board[row][0]==player:
            return True
    #diagonal check 1
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]==player:
        return True
    
    #diagonal check 2
    if board[2][0]==board[1][1]==board[0][2]==player:
        return True

def draw_win(player):
    #vertical check
    for col in range(b_columns):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col]==player:
            draw_vert_line(col,player)
            
        
    #horizonatal check
    for row in range(b_rows):
        if board[row][0]==board[row][1]==board[row][2] and board[row][0]==player:
            draw_hor_line(row, player)
            
    #diagonal check 1
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]==player:
        draw_diago1(player)
        
    
    #diagonal check 2
    if board[2][0]==board[1][1]==board[0][2]==player:
        draw_diago2(player)
        
    
def empty_space_count(board):
    count=0
    for row in range(b_rows):
        for col in range(b_columns):
            if board[row][col]==0:
                count+=1
    return count

def draw_vert_line(col,player):
    xpos= col*200+100
    
    if player==1:
        pygame.draw.line( screen,col_X,(xpos,20),(xpos,580),10)
    elif player==2:
        pygame.draw.line( screen,col_O,(xpos,20),(xpos,580),10)
    


def draw_hor_line(row,player):
    ypos= row*200+100
    if player==1:
        pygame.draw.line( screen,col_X,(20,ypos),(580,ypos),10)
    elif player==2:
        pygame.draw.line( screen,col_O,(20,ypos),(580,ypos),10)

def draw_diago1(player):
    if player==1:
        pygame.draw.line( screen,col_X,(20,20),(580,580),10)
    elif player==2:
        pygame.draw.line( screen,col_O,(20,20),(580,580),10)

        

def draw_diago2(player):
     if player==1:
        pygame.draw.line( screen,col_X,(20,580),(580,20),10)
     elif player==2:
        pygame.draw.line( screen,col_O,(20,580),(580,20),10)
        
def restart():
    screen.fill(BG_Colour)
    draw_board()
    for row in range(b_rows):
        for col in range(b_columns):
            board[row][col]=0
          
def ai_move():
    best_score= -math.inf
    for row in range(b_rows):
        for col in range(b_columns):
            if board[row][col]==0:
                board[row][col]=ai
                score= minimax(board,0,False)
                board[row][col]=0
                if score>best_score:
                    best_score=score
                    move=[row,col]
    mark_square(move[0], move[1], ai)
    draw_X(move[1], move[0])
        
        
def random_move():
    row= random.randint(0,2)
    col= random.randint(0,2)
    if free_space(row, col):
        mark_square(row, col, ai)
        draw_X(col,row)
    else:
        random_move()
    

def minimax(board,depth, isMaximizer):
    if check_win(ai):
        return 1
    elif check_win(human):
        return -1
    
    elif full_board():
        if True:
            return 0
            

    if isMaximizer:
        best_score= -math.inf
        for row in range(b_rows):
            for col in range(b_columns):
                if board[row][col]==0:
                    board[row][col]=ai
                    score= minimax(board,depth+1,False)
                    board[row][col]=0
                    best_score= max(score,best_score)
        return best_score
    
    else:
        best_score= math.inf
        for row in range(b_rows):
            for col in range(b_columns):
                if board[row][col]==0:
                    board[row][col]=human
                    score= minimax(board,depth+1,True)
                    board[row][col]=0
                    best_score=min(score,best_score)
        return best_score



game_over= False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        
        if player==ai and not game_over:
            ai_move()
            if check_win(player):
                game_over=True
                draw_win(player)
                
            player=human
            print(board)
            print(empty_space_count(board))
        
        
        elif player==human and not game_over:    
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            
                mouseX= event.pos[0] #event.pos gives the coordinates as a tuple 
                mouseY= event.pos[1] #and [] is for getting x,y coodinates using indices
            
                clicked_row= mouseY//200
                clicked_column= mouseX//200
            
                
                
            
                if free_space(clicked_row,clicked_column):
                    mark_square(clicked_row,clicked_column, 2)
                    draw_O(clicked_column,clicked_row)
                    if check_win(player):
                        game_over=True
                        draw_win
                    player=ai
            
        
                print(board)
                print(empty_space_count(board))
                
        
        
        
                
        if event.type== pygame.KEYDOWN:
            if  event.key== pygame.K_r or event.key== pygame.K_F5:
                restart()
                player=ai
                game_over= False
                
    pygame.display.update()