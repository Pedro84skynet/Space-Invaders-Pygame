import pygame 
import time

from spaceObjects import SpaceObjects
from spaceObjects import SpaceShip
from spaceObjects import SpaceInvader
from spaceObjects import SpaceProtonTorpedo
from graphics import Graphics

class GameMechanics():

    spaceObjectsList = []
    score = 0
    gameOver = False
    gameRunning = True
    spawntime = 4
    spawntimeIncrement = 5
    gameLevel = 1
    gameBossesTime = 5
    gameBossesGapTime = 5
    gameLevelScore = 1000
    shotsFired = 0

    def __init__(self, assets_dict, screenWidth, screenHeight):

        pygame.init()
        clock = pygame.time.Clock()
        clock.tick(60)
        pygame.mixer.init()
        pygame.display.set_caption("New Space Invaders")

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.assets_dict = assets_dict
        self.shipSprite = pygame.image.load(assets_dict['Ship'])
        self.shipSpriteLeft = pygame.image.load(assets_dict['ShipLeft'])
        self.shipSpriteRight = pygame.image.load(assets_dict['ShipRight'])
        self.InvaderSprite = pygame.image.load(assets_dict['Invader'])
        self.InvaderHardSprite = pygame.image.load(assets_dict['InvaderHard'])
        self.ProtonTorpedoSprite = pygame.image.load(assets_dict['ProtonTorpedo'])
        self.bullet = pygame.image.load(assets_dict['Bullet'])
        self.backgroundImage = pygame.image.load(assets_dict['Background'])
        self.shotSound = pygame.mixer.Sound(assets_dict['ShotSound'])
        self.explosion = pygame.mixer.Sound(assets_dict['Explosion'])

    def input_reader(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.shotsFired <= 4:
                    shot = SpaceProtonTorpedo(self.ProtonTorpedoSprite, self.ProtonTorpedoSprite, self.ProtonTorpedoSprite, 
                                                self.player.positionX() + 25,
                                                self.player.positionY(), 
                                                self.screenWidth, 
                                                self.screenHeight)
                    self.spaceObjectsList.append(shot)
                    self.shotsFired += 1
                    pygame.mixer.Sound.play(self.shotSound)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.player.move_to(self.player.positionX() - 1)
        elif pressed[pygame.K_RIGHT]:
            self.player.move_to(self.player.positionX() + 1)
        else:
            self.player.move_to(self.player.positionX())
    
    def ufo_vs_ship_hit_detector(self):
        for enemy in self.spaceObjectsList:
                if isinstance(enemy, SpaceInvader):
                    if  (enemy.positionX() - 40 < self.player.positionX() + 40 and
                         self.player.positionX() - 40 < enemy.positionX() + 40 and
                         enemy.positionY() - 40 < self.player.positionY() + 40 and
                         self.player.positionY() - 40 < enemy.positionY() + 40):
                        self.gameOver = True
                        self.gameRunning = False

    def shot_vs_ufo_hit_detector(self):
        for shot in self.spaceObjectsList:
                if isinstance(shot, SpaceProtonTorpedo):
                    new_list = []
                    for enemy in self.spaceObjectsList:
                        if (isinstance(enemy, SpaceInvader) and 
                            (enemy.positionX() + 15) < shot.positionX() < (enemy.positionX() + 65) and
                            (enemy.positionY() + 15) < shot.positionY() < (enemy.positionY() + 65)):
                            self.score += 100
                            del enemy
                            pygame.mixer.Sound.play(self.explosion)
                        else:
                            new_list.append(enemy)
                    self.spaceObjectsList = new_list

    def object_mover(self):
        for obj in self.spaceObjectsList:
                if isinstance(obj, SpaceShip):
                    continue
                else:
                   obj.move_to()
    
    def shot_eraser(self):
        new_list = []
        for shot in self.spaceObjectsList: 
            if isinstance(shot, SpaceProtonTorpedo):
                if shot.positionY() < self.screenHeight*(-7):
                    del shot
                    self.shotsFired -= 1
                else:
                    new_list.append(shot)
            else:
                new_list.append(shot)
        self.spaceObjectsList = new_list  

    def difficulty_ajuster(self, timeElapsed):
        
        if int(timeElapsed) > self.spawntime:
            if self.gameLevel > self.gameBossesTime:
                for i in range(5):
                    ufo = SpaceInvader(self.InvaderSprite, self.InvaderHardSprite,  self.InvaderHardSprite, 100*i, 50, 
                                    self.screenWidth, self.screenHeight)
                    ufo.rage_mode()
                    self.spaceObjectsList.append(ufo)
                self.gameBossesTime += self.gameBossesGapTime
                if self.gameBossesGapTime > 1:
                    self.gameBossesGapTime -= 1
                
            ufo = SpaceInvader(self.InvaderSprite, 
                                self.InvaderHardSprite,  
                                self.InvaderHardSprite, 0, 50, 
                                self.screenWidth, self.screenHeight)
            self.spaceObjectsList.append(ufo)
            self.spawntime += self.spawntimeIncrement
        if self.score > self.gameLevelScore:
            self.gameLevel += 1
            if self.spawntimeIncrement != 1:
                self.spawntimeIncrement -= 1
            self.gameLevelScore += 1000

    def game_on(self):

        start = time.time()

        self.graphics = Graphics(self.screenWidth, self.screenHeight, self.bullet, self.backgroundImage)

        self.player = SpaceShip(self.shipSprite, self.shipSpriteLeft, self.shipSpriteRight, int(self.screenWidth/2) - 100, self.screenHeight - 120, self.screenWidth, self.screenHeight)

        self.spaceObjectsList.append(self.player)

        for i in range(5):
            ufo = SpaceInvader(self.InvaderSprite, self.InvaderHardSprite,  self.InvaderHardSprite, 100*i, 50, 
                               self.screenWidth, self.screenHeight)
            self.spaceObjectsList.append(ufo)

        while self.gameRunning:
            
            self.input_reader()
            self.ufo_vs_ship_hit_detector()
            self.shot_vs_ufo_hit_detector()
            self.object_mover()
            self.shot_eraser()

            self.graphics.draw_screen(self.spaceObjectsList, self.score, self.gameLevel, self.shotsFired, self.gameOver)

            end = time.time()
            timeElapsed = end - start
            self.difficulty_ajuster(timeElapsed)

        self.gameOver = True
        self.gameRunning = True                  
        while self.gameRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameRunning = False
            self.graphics.draw_screen(self.spaceObjectsList, self.score, self.gameLevel, self.shotsFired, self.gameOver)
