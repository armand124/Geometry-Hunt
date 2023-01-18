import pygame as game
import sys
import os
from game import *
from state import *
from interactive import *
class Menu:
    background = game.image.load(os.path.join("assets/menu",'background.png')).convert_alpha()
    
    start_pressed = game.image.load(os.path.join("assets/menu",'cv1.png')).convert_alpha()
    start_unpressed = game.image.load(os.path.join("assets/menu",'cv1_u.png')).convert_alpha()
    
    close_pressed = game.image.load(os.path.join("assets/menu",'cv.png')).convert_alpha()
    close_unpressed = game.image.load(os.path.join("assets/menu",'cv_u.png')).convert_alpha()
    
    start = Button(786,450,start_pressed,start_unpressed)
    close = Button(786,660,close_pressed,close_unpressed)
    def handle():
        Screen.WIN.blit(Menu.background,(0,0))
        if Menu.close.buttonPressed():
           State.running = False
        if Menu.start.buttonPressed():
            State.inMenu = False
            State.postLevel = False
            State.inLevel = True
        Menu.start.showButton(Menu.start_pressed,Menu.start_unpressed)
        Menu.close.showButton(Menu.close_pressed,Menu.close_unpressed)
        game.display.update()
        
    def events():
        for event in game.event.get():
            if event.type == game.QUIT:
                State.running = False
                sys.exit()
            if event.type == game.MOUSEBUTTONDOWN:
                State.mouseDown = True