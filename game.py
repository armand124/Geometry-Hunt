import pygame as game
import os
import sys
import json
from state import *
from player import *
from interactive import *

class Level:
    next_un = game.image.load(os.path.join("assets/level","unpressedContinue.png")).convert_alpha()
    next_p = game.image.load(os.path.join("assets/level", "continuePressed.png")).convert_alpha()
    
    quit_un = game.image.load(os.path.join("assets/level","unpressedQuit.png")).convert_alpha()
    quit_p = game.image.load(os.path.join("assets/level", "quitPressed.png")).convert_alpha()
    
    #Forms 
    square_png = game.image.load(os.path.join("assets/level","square.png")).convert_alpha()
    triangle_png = game.image.load(os.path.join("assets/level","triangle.png")).convert_alpha()
    pentagon_png = game.image.load(os.path.join("assets/level","pentagon.png")).convert_alpha()
    
    square_find = game.image.load(os.path.join("assets/player",'find_square.png')).convert_alpha()
    tri_find = game.image.load(os.path.join("assets/player",'find_tri.png')).convert_alpha()
    penta_find = game.image.load(os.path.join("assets/player",'find_penta.png')).convert_alpha()
    
    finish_g = game.image.load(os.path.join("assets/level",'finishedScreen_good.png')).convert_alpha()
    finish_b = game.image.load(os.path.join("assets/level",'finishedScreen_bad.png'))
    
    stop = game.image.load(os.path.join("assets/level",'stopped.png')).convert_alpha()
    
    nextButton = Button(790,500,next_p,next_un)
    quitButton = Button(790,730,quit_p,quit_un)
    
    elements = []
    reader = open(os.path.join("assets/level",'levels.json'),'r')
    file = reader.read()
    reader.close()
    level = json.loads(file)
    def formID(id):
        if id == 0:
            return Level.square_png
        if id == 1:
            return Level.triangle_png
        return Level.pentagon_png
    def required(id):
        x,y,chunk,form = id
        if form == 0:
            return Level.square_find
        if form == 1:
            return Level.tri_find
        return Level.penta_find
    
    def parsedElements():
        available = []
        for x in range(0,len(Level.elements)):
         xCord,yCord,chunk,form = Level.elements[x]
         if (chunk == 0 and State.mainValley) or (chunk == 1 and State.north) or (chunk==2 and State.east) or (chunk==3 and State.west) or (chunk==4 and State.south):
            chosenForm = (xCord,yCord,Level.formID(form),x)
            available.append(chosenForm)
        return available
    
    def showElements():
        elements = Level.parsedElements()
        if len(Level.elements) == 0:
            State.inLevel = False
            State.ending = True
            State.postLevel = True
        for element in elements:
            crdX , crdY, img, id = element
            Screen.WIN.blit(img,(crdX,crdY))
            if(Player.x <= crdX and Player.x >= crdX-100 and Player.y <= crdY and Player.y >= crdY-100):
                if id == 0:
                    Level.elements.pop(0)
                else:
                    State.inLevel = False
                    State.postLevel = True
                    State.ending = False
    def begin(lvl):
        Player.x = 1920/2
        Player.y = 1080/2
        State.mainValley = True
        State.north = False
        State.stopped = False
        State.south = False
        State.east = False
        State.west = False
        Level.elements.clear()
        for x in range(0,len(Level.level["lvl"][lvl])):
            Level.elements.append((Level.level["lvl"][lvl][x][0],Level.level["lvl"][lvl][x][1],
                                   Level.level["lvl"][lvl][x][2],Level.level["lvl"][lvl][x][3]))
                
                
    def complete():
      if State.ending:
        Screen.WIN.blit(Level.finish_g,(0,0))
      else:
        Screen.WIN.blit(Level.finish_b,(0,0))
      if Level.nextButton.buttonPressed():
          if State.ending:
            State.currentLevel +=1
          Level.begin(State.currentLevel)
          State.postLevel = False
          State.inLevel = True
      if Level.quitButton.buttonPressed():
         State.inLevel = False
         State.inMenu = True
         State.postLevel = False
         reader = open(os.path.join("assets",'settings.json'),'w')
         settings = {
             "currentLevel" : State.currentLevel
         }
         with reader as outfile:
             json.dump(settings,outfile)
         reader.close()
      Level.quitButton.showButton(Level.quit_p,Level.quit_un)
      Level.nextButton.showButton(Level.next_p,Level.next_un)
      game.display.update()
      
    def stopped():
      Screen.WIN.blit(Level.stop,(0,0))
      if Level.nextButton.buttonPressed():
        State.stopped = False
        State.inLevel = True
      if Level.quitButton.buttonPressed():
          State.inLevel = False
          State.postLevel = 0
          State.inMenu = True
          State.stopped = False
          Player.x = 1920/2
          Player.y = 1080/2
          State.right = True
      Level.quitButton.showButton(Level.quit_p,Level.quit_un)
      Level.nextButton.showButton(Level.next_p,Level.next_un)
      game.display.update()
          
#Loading player
class Character:
    player_left = game.image.load(os.path.join("assets/player", "player_left.png")).convert_alpha()
    player_right = game.image.load(os.path.join("assets/player",'player_right.png')).convert_alpha()
    def show():
        Player.handleMovement(game.key.get_pressed())           
        if State.right:
          Screen.WIN.blit(Character.player_right,(Player.x,Player.y))
        else:
           Screen.WIN.blit(Character.player_left,(Player.x,Player.y)) 

#Loading chunks
class Chunks:
    main_grass =  game.image.load(os.path.join("assets/game",'grass.png')).convert_alpha()
    east = game.image.load(os.path.join("assets/game",'ceva_E.png')).convert_alpha()
    west = game.image.load(os.path.join("assets/game",'ceva_V.png')).convert_alpha()
    south = game.image.load(os.path.join("assets/game",'ceva_N.png')).convert_alpha()
    north = game.image.load(os.path.join("assets/game",'ceva_S.png')).convert_alpha()
    #---------------MAIN CHUNKS-----------------#
    #Main Chunk
    def mainScreen():
        Screen.WIN.blit(Chunks.main_grass,(0,0))
        Character.show()
        Level.showElements()
        if len(Level.elements) > 0 :
          Screen.WIN.blit(Level.required(Level.elements[0]),(0,0))
        game.display.update()
        
    def screenEvent():
        for event in game.event.get():
            if event.type == game.QUIT:
                State.running = False
                sys.exit()
            if event.type == game.MOUSEBUTTONDOWN:
                State.mouseDown = True   
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    State.stopped = not State.stopped            
    #East
    def eastScreen():
        Screen.WIN.blit(Chunks.east,(0,0))
        Character.show()
        Level.showElements()
        if len(Level.elements) > 0 :
          Screen.WIN.blit(Level.required(Level.elements[0]),(0,0))
        game.display.update()
    
    #West
    def westScreen():
        Screen.WIN.blit(Chunks.west,(0,0))
        Character.show()
        Level.showElements()
        if len(Level.elements) > 0 :
          Screen.WIN.blit(Level.required(Level.elements[0]),(0,0))
        game.display.update()
        
    #North
    def northScreen():
        Screen.WIN.blit(Chunks.north,(0,0))
        Character.show()
        Level.showElements()
        if len(Level.elements) > 0 :
          Screen.WIN.blit(Level.required(Level.elements[0]),(0,0))
        game.display.update()
        
    #South
    def southScreen():
        Screen.WIN.blit(Chunks.south,(0,0))
        Character.show()
        Level.showElements()
        if len(Level.elements) > 0 :
          Screen.WIN.blit(Level.required(Level.elements[0]),(0,0))
        game.display.update()
    #----------------------------------------------------#
    
    def update():
        #----For left and right in all chunks----#
        if Player.x <= 10 and State.mainValley:
            State.mainValley = False
            State.west = True
            Player.x = 1700
        if Player.x <= 10 and State.east: 
            State.east = False
            State.mainValley = True
            Player.x = 1700
        if Player.x >=1800 and State.mainValley:
            State.mainValley = False
            State.east = True
            Player.x = 15
        if Player.x >= 1800 and State.west:
            State.west = False
            State.mainValley = True
            Player.x = 15
        #---------------------------------------#    
        
        #------For up and down in all chunks-----#
        if Player.y < 10 and State.mainValley:
            State.mainValley = False
            State.south = True
            Player.y = 870
        if Player.y > 880 and State.south:
            State.south = False
            State.mainValley = True
            Player.y = 20
        if Player.y > 880 and State.mainValley:
            State.mainValley = False
            State.north = True
            Player.y = 20
        if Player.y < 10 and State.north:
            State.north = False
            State.mainValley = True
            Player.y = 870
        #----------------------------------------#


# TODO:
#   Menu
#   Transition
#   Tutorial

Level.begin(State.currentLevel)