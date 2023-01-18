import pygame as game
from state import *
from game import *
from player import *
from menu import *
game.init()

clock = game.time.Clock()

while State.running:
    Chunks.screenEvent()
    Chunks.update()
    if State.postLevel:
      Level.complete()
    if State.inMenu:
       Menu.handle()
       Menu.events()
    if State.inLevel:
      if State.mainValley:
        Chunks.mainScreen()
      if State.north:
        Chunks.northScreen()
      if State.east:
        Chunks.eastScreen()
      if State.west:
        Chunks.westScreen()
      if State.south:
        Chunks.southScreen()
      
    clock.tick(320)
