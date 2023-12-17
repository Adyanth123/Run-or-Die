import pygame
import os
from pygame.locals import *
import time
import random
from random import randint
#Importing all modules needed for program
pygame.init()
pygame.mixer.init()
pygame.font.init()
#Initializing
WIDTH = 300
HEIGHT = 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("RUN or DIE")
#Setting screen height and width including making screen
BLUE = 175, 238, 238
#BG color
clock = pygame.time.Clock()
#FPS
class death:
    def __init__(self):
        self.dead = pygame.image.load(os.path.join("Images", "game_over.png"))
        self.dead = pygame.transform.scale(self.dead, (WIDTH, HEIGHT))
    def draw(self):
        WIN.blit(self.dead, (0,0))
    def button(self):
        self.dead_button = pygame.image.load(os.path.join("Images", "again.png"))
        self.dead_button = pygame.transform.scale(self.dead_button, (200,100 ))
        self.rect = self.dead_button.get_rect()
        WIN.blit(self.dead_button, (50, 100))

def bg_music(volume, e):
    if e == 1:
        pygame.mixer.music.load(os.path.join("Music", "bg_music.ogg"))
    elif e == 2:
        pygame.mixer.music.load(os.path.join("Music", "bg_music1.ogg"))
    elif e == 3:
        pygame.mixer.music.load(os.path.join("Music", "bg_music2.ogg"))
    elif e == 4:
        pygame.mixer.music.load(os.path.join("Music", "bg_music3.ogg"))
    elif e == 5:
        pygame.mixer.music.load(os.path.join("Music", "bg_music4.ogg"))
    elif e == 6:
        pygame.mixer.music.load(os.path.join("Music", "bg_music5.ogg"))
    elif e == 7:
        pygame.mixer.music.load(os.path.join("Music", "bg_music6.ogg"))
    elif e == 8:
        pygame.mixer.music.load(os.path.join("Music", "bg_music7.ogg"))
    elif e == 9:
        pygame.mixer.music.load(os.path.join("Music", "over.mp3"))
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(1)
def score(score):
    myfont = pygame.font.SysFont("comic_sans", 30)
    score = myfont.render(f"Score: {score}", 1, (0,0,0))
    WIN.blit(score, score.get_rect(center=WIN.get_rect().center))
class Coin:
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join("Images", "coin.png"))
        self.image = pygame.transform.scale(self.image, (40,40))
        self.hitbox = pygame.transform.scale(self.image, (30,30))
        self.x = x
        self.y = y
        self.c = 1
        self.coin_rect = self.hitbox.get_rect(topleft=(self.x, self.y))
    def draw(self):
        WIN.blit(self.image, (self.x, self.y))
    def coin_sound(self):
        for self.c in range(0,self.c):
            pygame.mixer.music.load(os.path.join("Music", "coin.wav"))
            pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.play(-1)
            self.c -= 1
class Player:
    def __init__(self, x, y,vel):
        
        self.vel = vel
        
        self.image = pygame.image.load(os.path.join("Images","player.png"))
        self.image = pygame.transform.scale(self.image,(30,30))
        self.hitbox = pygame.transform.scale(self.image, (25,25))
        
        self.rect = self.hitbox.get_rect()
        bg_music(0.5,9)
        self.rect.x = x
        self.rect.y = y
        #Vars for obj
    def update(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y-=self.vel
            
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y+=self.vel
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x+=self.vel

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x-=self.vel

            
        WIN.blit(self.image,self.rect)
        self.rect.clamp_ip(WIN.get_rect())
        #Movement
        
# Player object, making vars, movement, bliting image to screen
class Spike:
    def __init__(self, x ,y,r):
        self.r = r
        self.image = pygame.image.load(os.path.join("Images", "spike.png"))
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image = pygame.transform.rotate(self.image,r)
        self.hitbox = pygame.transform.scale(self.image,(35,35))

        self.x = x
        self.y = y
        
        self.rect = self.hitbox.get_rect(topleft=(x,y))
        #Vars for spike obj
    def draw_spike(self):
        WIN.blit(self.image,(self.x,self.y))
        #Bliting
class Wood:
    def __init__(self, wox, woy, r):
        self.r = r
        self.wood = pygame.image.load(os.path.join("Images", "log.png"))
        self.wood = pygame.transform.scale(self.wood, (150,25))
        self.wood = pygame.transform.rotate(self.wood, self.r)
        self.hitbox = pygame.transform.scale(self.wood, (140, 15))

        self.wox = wox
        self.woy = woy

        self.wood_rect = self.hitbox.get_rect(topleft=(wox,woy))
        #self.coin_rect = self.coin.get_rect()
        #Vars for wood obj
    def draw_wood(self):
        WIN.blit(self.wood,(self.wox,self.woy))
        
        #Bliting
class MainRun:
    def Main(self):
        stopped = False
        FPS = 50
        #FPS for diferent types of computers
        spike1 = Spike(0,0,180)
        spike3 = Spike(50,0,180)
        spike5 = Spike(100,0,180)
        spike7 = Spike(150,0,180)
        spike9 = Spike(200,0,180)
        spike11 = Spike(250,0,180)
        spike13 = Spike(300,0,180)
        spike14 = Spike(0,50,270)
        spike15 = Spike(250,50,90)
        spike16 = Spike(0,150,270)
        spike17 = Spike(250,150,90)
        spike18 = Spike(0,250,270)
        spike19 = Spike(250,250,90)
        spike20 = Spike(0,350,270)
        spike21 = Spike(250,350,90)
        spike22 = Spike(0,450,270)
        spike23 = Spike(250,450,90)
        spike24 = Spike(0,550,270)
        spike25 = Spike(250,550,90)
        spike26 = Spike(0,650,270)
        spike27 = Spike(250,650,90)
        coin = Coin(random.randint(0,220), random.randint(100,700))
        dead = death()
        x = 0
        y = 0
        x1 = 150
        y1 = 0
        player = Player(200,600,5)
        s=0
        t_t = 0
        sfont = 0
        bg_music(0.9, random.randint(1,8))
        #Making all obj and variables
        newfont = pygame.font.SysFont("comic_sans", 50)
        new = newfont.render(f"RUN or DIE", 1, (255,255,255))
        WIN.blit(new, new.get_rect(center=WIN.get_rect().center))
        time.sleep(2)
        pygame.display.update()
        while stopped == False:
            
            #While loop, game loop
            WIN.fill(BLUE)
            clock.tick(FPS)
            speed = 4.6
            speed1 = 5.2
            x+= 0.5
            y += speed
            x1 -= 0.5
            y1 += speed1
            y36 = 20
            y37 = 30
            if y >= 750:
                x = 0
                y=0
            elif y1 >= 750:
                x1 = 100
                y1 = 0
            wood = Wood(x,y, 180)
            wood1 = Wood(x1,y1, 0)
            s+=1
            if sfont >= 6 and stopped == False:
                spike2 = Spike(250, 100, 90)
                spike2.draw_spike()
                spike6 = Spike(0, 100, 270)
                spike6.draw_spike()
                if player.rect.colliderect(spike2.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
                elif player.rect.colliderect(spike6.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
            if sfont >= 11 and stopped == False:
                spike4 = Spike(250, 200, 90)
                spike4.draw_spike()
                spike8 = Spike(0, 200, 270)
                spike8.draw_spike()
                if player.rect.colliderect(spike4.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
                if player.rect.colliderect(spike8.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
            if sfont >= 16 and stopped == False:
                spike28 = Spike(250, 300, 90)
                spike28.draw_spike()
                spike29 = Spike(0, 300, 270)
                spike29.draw_spike()
                spike30 = Spike(250, 400, 90)
                spike30.draw_spike()
                spike31 = Spike(0, 400, 270)
                spike31.draw_spike()
                speed = 4.2
                speed1 = 4.5
                if player.rect.colliderect(spike28.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
                elif player.rect.colliderect(spike29.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
                elif player.rect.colliderect(spike30.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
                elif player.rect.colliderect(spike31.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
            if sfont >= 23 and stopped == False:
                spike32 = Spike(250, 500, 90)
                spike32.draw_spike()
                spike33 = Spike(0, 500, 270)
                spike33.draw_spike()
                spike34 = Spike(250, 600, 90)
                spike34.draw_spike()
                spike35 = Spike(0, 600, 270)
                spike35.draw_spike()
                speed = 4.5
                speed1 = 4.9
                if player.rect.colliderect(spike32.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
                elif player.rect.colliderect(spike33.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
                elif player.rect.colliderect(spike34.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
                elif player.rect.colliderect(spike35.rect):
                    dead.draw()
                    player = Player(200,600,5)
                    stopped = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stopped = True
                    pygame.quit()
                    exit()
            coin.draw()
            spike1.draw_spike()
            spike3.draw_spike()
            spike5.draw_spike()
            spike7.draw_spike()
            spike9.draw_spike()
            spike11.draw_spike()
            spike13.draw_spike()
            spike14.draw_spike()
            spike15.draw_spike()
            spike16.draw_spike()
            spike17.draw_spike()
            spike18.draw_spike()
            spike19.draw_spike()
            spike20.draw_spike()
            spike21.draw_spike()
            spike22.draw_spike()
            spike23.draw_spike()
            spike24.draw_spike()
            spike25.draw_spike()
            spike26.draw_spike()
            spike27.draw_spike()
            wood.draw_wood()
            wood1.draw_wood()
            player.update()
            score(sfont)
            #Drawing everything
            if player.rect.colliderect(spike1.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike3.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike5.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike7.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike9.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike11.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike13.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike14.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike15.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike16.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike17.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike18.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike19.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike20.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike21.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike22.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike23.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike24.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike25.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike26.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(spike27.rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
            elif player.rect.colliderect(wood.wood_rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
                x = 0
                y = 0
                wood = Wood(x,y, 180)
            #Collisions
            elif player.rect.colliderect(wood1.wood_rect):
                dead.draw()
                player = Player(200,600,5)
                stopped = True
                x1 = 0
                y1 = 0
                wood1 = Wood(x1,y1, 0)
            elif player.rect.colliderect(coin.coin_rect):
                sfont +=1
                coin = Coin(random.randint(75,225), random.randint(100,700))
                #coin.coin_sound()
                coin.draw()
            pygame.init()
            pygame.display.update()
            while stopped == True:
                pygame.display.update()
                clock.tick(FPS)
                dead.button()
                bg_music(1, random.randint(1,8))
                sfont = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.display.update()
                        stopped = False
                        pygame.display.update()
            pygame.init()
            pygame.display.update()
            #Updating screen
            
            
main = MainRun()
if __name__ == "__main__":
    main.Main()
#Runs only if on this page, not imported
