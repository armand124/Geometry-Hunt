import pygame as game
from state import *
class Button():
    def __init__(self , x , y , imagePressed,imageUnpressed):
        self.rect = imagePressed.get_rect()
        self.rect.topleft = (x,y)
    
    
    def buttonPressed(self):
       if State.mouseDown == True:
        if self.rect.collidepoint(game.mouse.get_pos()):
                State.collideWithObject |= True
                State.mouseDown = False
                return True
        else:
            State.collideWithObject |= False
            
    def buttonOnCursor(self):
        if self.rect.collidepoint(game.mouse.get_pos()):
                return True
    def showButton(self,imagePressed,imageUnpressed): 
        if Button.buttonOnCursor(self):
         Screen.WIN.blit(imagePressed, (self.rect.x-5 , self.rect.y-5))
        elif Button.buttonPressed(self):
         Screen.WIN.blit(imagePressed,(self.rect.x,self.rect.y))
        else:
         Screen.WIN.blit(imageUnpressed,(self.rect.x,self.rect.y))