import pygame
import os
from pygame.locals import *
pygame.init()
WIDTH = 300
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
player_image = pygame.image.load(os.path.join("Images","player.png"))
player_image = pygame.transform.scale(player_image,(30,30))
clock = pygame.time.Clock()

        
class MainRun:
    def __init__(self,WIDTH,HEIGHT):
        self.w = WIDTH
        self.h = HEIGHT
        self.Main()

    def Main(self):
        #Put all variables up here
        x = 100
        y = 100
        vel = 5
        BLUE = 175, 238, 238
        stopped = False
        while stopped == False:
            WIN.fill(BLUE)
            WIN.blit(player_image,(x,y))
            pygame.display.update()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stopped = True
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        v-=vel
                    if event.key == pygame.K_DOWN:
                        y+=vel
                    if event.key == pygame.K_RIGHT:
                        x+=vel
                    if event.key == pygame.K_LEFT:
                        x-=vel
                    if event.key == pygame.K_q:
                        stopped = True
                        pygame.quit()
            

if __name__ == "__main__":
    MainRun(WIDTH,HEIGHT)
