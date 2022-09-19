import pygame 
import time

class Graphics():

    def __init__(self, screen_width, screen_height, bullet,  backgroundImage):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.bullet = bullet
        self.background = backgroundImage
        font_list = pygame.font.get_fonts()
        if 'freemono' in font_list:
            self.font = pygame.font.SysFont('freemono', 20)
        elif 'arial' in font_list:
            self.font = pygame.font.SysFont('arial', 20)
        else:
            self.font = pygame.font.SysFont('dejavuserif', 20)

    def draw_screen(self, listObjects, score, level, shotsFired, gameOver):
        if gameOver:
            self.screen.fill((0,0,0))
            endText = self.font.render("GAME OVER", True, (255,255,255))
            scoreText = self.font.render("Score: {}".format(score), True, (255,255,255))
            self.screen.blit(endText, (int(self.screen_width/2) - 60, int(self.screen_width/2) - 150))
            self.screen.blit(scoreText, (int(self.screen_width/2) - 60, int(self.screen_width/2)- 120))
            pygame.display.update()
        else:
            self.screen.blit(self.background, (0, 0))
            pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(0, 0, self.screen_width, 21))
            pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(0, self.screen_height -21, self.screen_width, self.screen_height))
            for obj in listObjects:
                self.screen.blit(obj.image(), obj.position())
            scoreText = self.font.render("Score: {}".format(score), True, (255,255,255))
            levelText = self.font.render("Level: {}".format(level), True, (255,255,255))
            self.screen.blit(levelText, (0, 0))
            self.screen.blit(scoreText, (self.screen_width - 150, 0))
            for i in range(5 - shotsFired):
                self.screen.blit(self.bullet, (25*i, self.screen_height - 20))
            pygame.display.update()
            