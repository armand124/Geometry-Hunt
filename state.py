import os
import json
import pygame as game
class State: 
    def __init__(self):
        pass
    #Game state
    running = True
    inLevel =False
    postLevel = False
    mouseDown = False
    inMenu = True
    ending = True
    collideWithObject = False
    #Screen
    mainValley = True
    north = False
    south = False
    east = False
    west = False
    
    #Values
    reader = open(os.path.join("assets",'settings.json'),'r')
    file = reader.read()
    reader.close()
    user = json.loads(file)
    
    volume = user["volume"]
    currentLevel = user["currentLevel"]
    
class Screen:
    WIN = game.display.set_mode((1920, 1080))
    
    