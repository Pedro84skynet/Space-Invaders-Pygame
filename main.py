import pygame 
import time

from spaceObjects import SpaceObjects
from spaceObjects import SpaceShip
from spaceObjects import SpaceInvader
from spaceObjects import SpaceProtonTorpedo
from graphics import Graphics
from logic import GameMechanics


def main():
    print("Welcome to Space Invader PyGame!")
    assets_dict = {
        "Ship": './assets/imgs/smallfighter0006.png',
        "ShipLeft": './assets/imgs/smallfighter0003.png',
        "ShipRight": './assets/imgs/smallfighter0009.png',
        "Invader": './assets/imgs/ufo.png',
        "InvaderHard": './assets/imgs/ufoHard.png',
        "ProtonTorpedo": './assets/imgs/shot.png',
        "Bullet": './assets/imgs/bullet.png',
        "Background": './assets/imgs/background.png',
        "ShotSound": './assets/sounds/weaponfire6.wav',
        "Explosion": './assets/sounds/explosion4.wav'
    }
    game = GameMechanics(assets_dict, 800, 600)
    game.game_on()

if __name__ == "__main__":
    main()


