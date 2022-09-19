import pygame 
import time

class SpaceObjects():

    sprite_list = []

    def __init__(self, sprite, spriteAux1, spriteAux2, x, y, screenWidth, screenHeigth):
        self.posX = x
        self.posY = y
        self.screenWidth = screenWidth
        self.screenHeigth = screenHeigth
        self.sprite = sprite
        self.spriteStd = sprite
        self.spriteAux1 = spriteAux1
        self.spriteAux2 = spriteAux2

    def __str__(self):
        print("({},{})".format(self.posX, self.posY))

    def move_to(self, x, y):
        self.posX = x
        self.posY = y

    def position(self):
        return (self.posX, self.posY)

    def positionX(self):
        return self.posX
    
    def positionY(self):
        return self.posY

    def image(self):
        return self.sprite

class SpaceShip(SpaceObjects):

    def __str__(self):
        return "SpaceShip at ({},{})".format(self.posX, self.posY)

    def move_to(self, x):
        if  0 < x < self.screenWidth - 64:
            if x > self.posX:
                self.sprite = self.spriteAux2
            elif x < self.posX:
                self.sprite = self.spriteAux1
            else:
                self.sprite = self.spriteStd
            self.posX = x

class SpaceInvader(SpaceObjects):

    directionRight = True
    move = 1

    def __str__(self):
        return "SpaceInvader at ({},{})".format(self.posX, self.posY)

    def move_to(self):
        if self.directionRight:
            self.posX += self.move
            if self.posX > self.screenWidth -80:
                self.posY += 40
                self.directionRight = False
        else:
            self.posX -= self.move
            if self.posX < 0:
                self.posY += 40
                self.directionRight = True
    
    def rage_mode(self):
        self.move += 1
        self.sprite = self.spriteAux1


class SpaceProtonTorpedo(SpaceObjects):

    def __str__(self):
        return "SpaceProtonTorpedo at ({},{})".format(self.posX, self.posY)

    def move_to(self):
        self.posY -= 5