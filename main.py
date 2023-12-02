import pygame
import os
pygame.init()
WIDTH = 300
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
player_image = pygame.image.load(os.path.join("Images","player.png"))
player_image = pygame.transform.scale(player_image,(30,30))

clock = pygame.time.Clock()
class Player:
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = image
    def draw(self):
        WIN.blit(self.image,(self.x,self.y))

    #Method to move object (special input of speedx and speedy)
    def move(self,speedx,speedy):
        global speedx
        global speedy
        self.x += speedx
        self.y += speedy
        
class MainRun:
    def __init__(self,WIDTH,HEIGHT):
        self.w = WIDTH
        self.h = HEIGHT
        self.Main()

    def Main(self):
        #Put all variables up here
        player = Player(60,60,player_image)
        player.draw()
        player.move(speedx,speedy)
        BLUE = 175, 238, 238
        stopped = False
        while stopped == False:
            WIN.fill(BLUE)
            player.draw()
            pygame.display.update()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stopped = True
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        speedy -= 5
                        speedx = 0
                    if event.key == pygame.K_DOWN:
                        speedy += 5
                        speedx = 0
                    if event.key == pygame.K_RIGHT:
                        speedy = 0
                        speedx += 0
                    if event.key == pygame.K_LEFT:
                        speedy = 0
                        speedx -= 0
                    if event.key == pygame.K_q:
                        stopped = True
                        pygame.quit()
            

if __name__ == "__main__":
    MainRun(WIDTH,HEIGHT)
