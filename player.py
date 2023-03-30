import pygame as game
from state import *

class Player:
    velocity = 3
    x = 1920/2
    y = 1080/2

    def handleMovement(key):
        if key[game.K_a] and Player.x - Player.velocity > 5:
            Player.x -= Player.velocity
            State.right = False
        if key[game.K_d] and Player.x + Player.velocity < 1810:
            Player.x += Player.velocity
            State.right = True
        if key[game.K_w] and Player.y - Player.velocity > 5:
            Player.y -= Player.velocity
        if key[game.K_s] and Player.y + Player.velocity < 890:
            Player.y += Player.velocity
        
        