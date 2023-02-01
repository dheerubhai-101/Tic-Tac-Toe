# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:12:35 2021

@author: dheeraj
"""

import pygame
import numpy as np
import math

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

b_rows=3
b_columns=3
board= np.zeros((b_rows,b_columns))


player=1

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
            #pygame.draw.circle( screen,BG_Colour,(int(col*200 + 100),int(row*200+100)),40)
            
    
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
            draw_vert_line(col,player)
            return True
        
    #horizonatal check
    for row in range(b_rows):
        if board[row][0]==board[row][1]==board[row][2] and board[row][0]==player:
            draw_hor_line(row, player)
            return True
    #diagonal check 1
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]==player:
        draw_diago1(player)
        return True
    
    #diagonal check 2
    if board[2][0]==board[1][1]==board[0][2]==player:
        draw_diago2(player)
        return True
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
        pygame.draw.line( screen,col_X,(xpos,20),(xpos,580),15)
    elif player==2:
        pygame.draw.line( screen,col_O,(xpos,20),(xpos,580),15)
    


def draw_hor_line(row,player):
    ypos= row*200+100
    if player==1:
        pygame.draw.line( screen,col_X,(20,ypos),(580,ypos),15)
    elif player==2:
        pygame.draw.line( screen,col_O,(20,ypos),(580,ypos),15)

def draw_diago1(player):
    if player==1:
        pygame.draw.line( screen,col_X,(20,20),(580,580),15)
    elif player==2:
        pygame.draw.line( screen,col_O,(20,20),(580,580),15)

        

def draw_diago2(player):
     if player==1:
        pygame.draw.line( screen,col_X,(20,580),(580,20),15)
     elif player==2:
        pygame.draw.line( screen,col_O,(20,580),(580,20),15)
        
def restart():
    screen.fill(BG_Colour)
    draw_board()
    for row in range(b_rows):
        for col in range(b_columns):
            board[row][col]=0
            
            



game_over= False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            
            mouseX= event.pos[0] #event.pos gives the coordinates as a tuple 
            mouseY= event.pos[1] #and [] is for getting x,y coodinates using indices
            
            clicked_row= mouseY//200
            clicked_column= mouseX//200
            
            
            if free_space(clicked_row,clicked_column):
                if player==1:
                    mark_square(clicked_row,clicked_column, 1)
                    draw_X(clicked_column,clicked_row)
                    if check_win(player):
                        game_over=True
                    player=2
                elif player==2:
                    mark_square(clicked_row,clicked_column, 2)
                    draw_O(clicked_column,clicked_row)
                    if check_win(player):
                        game_over=True
                    player=1
            
            full_board
            print(board)
            print(empty_space_count(board))
        
        if event.type==  pygame.KEYDOWN:
            if  event.key== pygame.K_r or event.key== pygame.K_F5:
                restart()
                player=1
                game_over= False
                
    pygame.display.update()