# Made by MEHUL KUMAR

import pygame,time
import random
from math import pi

CONST_W = 800
CONST_H = 600
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class simulation:

    screen_w = CONST_W
    screen_h = CONST_H
    L = []
    M = []
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()

    time = 0
    tick = 60
    score = 0 
    pos = 0
    pos_x = 0
    intr = 60000

    trance_status = False

    w_size = 100
    bar_len = 100

    ball_size = 10
    ball_offset = 3

    speed_ctr_width_l = 200
    speed_ctr_width_r = 400
    speed_ctr_len_l =  200
    speed_ctr_len_r =  600

    blocks_offset = 2
    dis = 10
    level = 0

    def upg_level(self,i = 1):
        if(self.level>12):
            return

        self.level+=1
        if(self.level==1):
            self.speed_ctr_width_l = 100
            self.speed_ctr_width_r = 400
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  400
            self.dis=1.5
            self.blocks_offset=2
            
        if(self.level==2):
            self.speed_ctr_width_l = 20
            self.speed_ctr_width_r = 50
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  300
            self.dis=10
            self.blocks_offset=2
            
        if(self.level==3):
            self.speed_ctr_width_l = 70
            self.speed_ctr_width_r = 100
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  400
            self.dis=1.5
            self.blocks_offset=2

            
        if(self.level==4):
            self.speed_ctr_width_l = 100
            self.speed_ctr_width_r = 200
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  400
            self.dis=2.2
            self.blocks_offset=4
            
        if(self.level==5):
            self.speed_ctr_width_l = 100
            self.speed_ctr_width_r = 150
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  300
            self.dis=1.75
            self.blocks_offset=4
            self.ball_offset = 5
            
        if(self.level==6):
            self.speed_ctr_width_l = 70
            self.speed_ctr_width_r = 150
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  400
            self.dis=2
            self.blocks_offset=5
            
        if(self.level==7):
            self.speed_ctr_width_l = 70
            self.speed_ctr_width_r = 150
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  300
            self.dis=1.75
            self.blocks_offset=5
            
        if(self.level==8):
            self.speed_ctr_width_l = 20
            self.speed_ctr_width_r = 70
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  300
            self.dis=3.5
            self.blocks_offset=6
            
        if(self.level==9):
            self.speed_ctr_width_l = 70
            self.speed_ctr_width_r = 100
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  400
            self.dis=3.2
            self.blocks_offset=9
            
        if(self.level==10):
            self.speed_ctr_width_l = 50
            self.speed_ctr_width_r = 100
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  300
            self.dis=3.2
            self.blocks_offset=10

        if(self.level==11):
            self.speed_ctr_width_l = 100
            self.speed_ctr_width_r = 200
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  400
            self.dis=3.2
            self.blocks_offset=15

        if(self.level==12):
            self.speed_ctr_width_l = 10
            self.speed_ctr_width_r = 20
            self.speed_ctr_len_l =  200
            self.speed_ctr_len_r =  400
            self.blocks_offset=random.randint(100,500)
            self.tick=100
            self.trance_status= True
            self.intr = 10
            self.level-=1

    def list_update(self, x = 0, y = CONST_H/2):

        if self.time>self.intr:
            self.time = 0
            self.upg_level()

        self.bar_len = (random.randint(self.speed_ctr_len_l, self.speed_ctr_len_r))

        self.pos = (random.randint(max(y-int(self.bar_len/self.dis),0),min(y+int(self.bar_len/self.dis),self.screen_h)))
        self.L.append(self.pos)

        self.w_size = (random.randint(self.speed_ctr_width_l, self.speed_ctr_width_r))
        self.M.append(self.w_size)

        self.block_list.add(UBlock(BLACK, x , max(self.pos-self.bar_len//2,0),self.w_size))
        self.block_list.add(DBlock(BLACK, x , min(self.pos+self.bar_len//2,self.screen_h),self.w_size))

    def list_start(self):

        self.upg_level()
        self.list_update()
        self.list_update(sum(self.M),self.pos)
        while sum(self.M[1:])<self.screen_w+self.blocks_offset:
            self.list_update(sum(self.M),self.pos)

        self.all_sprites_list.add(ball(BLUE,sum(self.M[0:self.pos_x])+self.M[self.pos_x]//2,self.L[self.pos_x],self.ball_size))

        self.display_changes()

        
    def display_changes(self):
        
        spd =2
        frame = 2

        image = pygame.transform.scale(sky, (frame*CONST_W, CONST_H ))
        rect1 = image.get_rect()
        rect1.x = -((spd*self.score)%(frame*self.screen_w))
        rect1.y = 0
        screen.blit(image,rect1)

        rect2 = image.get_rect()
        rect2.x = -((spd*self.score)%(frame*self.screen_w))+frame*(CONST_W)
        rect2.y = 0
        screen.blit(image,rect2)
        self.block_list.draw(screen)

        image = pygame.transform.scale(space, (50, 50))
        rect3 = image.get_rect()
        for sprite in self.all_sprites_list.sprites():
            rect3.centerx = sprite.rect.centerx
            rect3.centery = sprite.rect.centery
        screen.blit(image,rect3)



        label = myfont.render("SCORE "+str(self.score//80), 1, RED)
        screen.blit(label, (580, 20))
        #pygame.draw.rect(screen,BLUE, (340,10,100,40))
        label = myfont.render("LEVEL "+str(self.level),1, RED)
        screen.blit(label, (20, 20))

        if(self.trance_status==True):
            label = myfont.render("...... Thank You For playing......",10, RED)
            screen.blit(label, (180, 300))

        clock.tick(self.tick)
        self.time+=self.tick
        pygame.display.flip()


    def display_list(self):

        while self.M[0]>0:
            pygame.event.get()
            self.block_list.update(self.blocks_offset)
            pygame.event.get()
            self.all_sprites_list.update(self.ball_offset)
            self.display_changes()
            if(self.level<=11 and self.trance_status==False):
                self.score += self.blocks_offset
            self.M[0]-= self.blocks_offset
            if not self.colli_check():
                return False

        self.M[1]+=self.M[0]
        self.M.pop(0)
        self.L.pop(0)
        while sum(self.M[1:])<self.screen_w+self.blocks_offset:
            self.list_update(sum(self.M),self.pos)
        
        return True

    def colli_check(self):
        if self.trance_status == True:
            return True

        for sprite in self.all_sprites_list.sprites():
            blocks_hit_list =  pygame.sprite.spritecollide(sprite, self.block_list, False)
            if (len(blocks_hit_list)>0 or sprite.rect.y<0 or sprite.rect.y > self.screen_h ):
                image = pygame.transform.scale(fire, (50, 50))
                rect3 = image.get_rect()
                rect3.centerx = sprite.rect.centerx
                rect3.centery = sprite.rect.centery
                screen.blit(image,rect3)
                pygame.mixer.music.load('Expsound.mp3')
                pygame.mixer.music.play()
                pygame.display.flip()
                time.sleep(5)

                image = pygame.transform.scale(sky, (2*CONST_W, CONST_H ))
                rect1 = image.get_rect()
                rect1.x = -((self.score)%(self.screen_w))
                rect1.y = 0
                screen.blit(image,rect1)
                self.block_list.draw(screen)
                label = myfont.render("SCORE "+str(self.score//80), 1, RED)
                screen.blit(label, (580, 20))
                #pygame.draw.rect(screen,BLUE, (340,10,100,40))
                label = myfont.render("LEVEL "+str(self.level),1, RED)
                screen.blit(label, (20, 20))

                label = myfont.render("...... Thank You For playing......",10, RED)
                screen.blit(label, (180, 300))
                pygame.display.flip()

                
                return False
        else:
            return True

class UBlock(pygame.sprite.Sprite):

    def __init__(self, color, x_axis, y_axis, w_size):

        super().__init__()

        self.w_size = w_size
        self.image = brick  
        self.image = pygame.transform.scale(self.image, (w_size, y_axis))
        self.rect = self.image.get_rect()
        self.rect.x = x_axis
        self.rect.y = 0

    def update(self,i):
        if self.rect.x + self.w_size <= 0 :
            self.kill()
        else:
            self.rect.x -= i

class DBlock(pygame.sprite.Sprite):

    def __init__(self, color, x_axis, y_axis,w_size):

        super().__init__()

        self.w_size = w_size
        self.image = brick 
        self.image = pygame.transform.scale(self.image, (w_size, CONST_H - y_axis))
        self.rect = self.image.get_rect()
        self.rect.x = x_axis
        self.rect.y = y_axis

    def update(self,i):
        if self.rect.x + self.w_size <= 0 :
            self.remove()
        else:
            self.rect.x -= i

class ball(pygame.sprite.Sprite, simulation):

    def __init__(self, color, x , y  ,size =20,inc_x=1,inc_y=1):
    
        super().__init__()

        self.image = pygame.Surface([size, size])
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.inc_x = inc_x
        self.inc_y = inc_y
        self.size = size

    def up(self):
        return ( ( event.type == pygame.KEYDOWN and event.key == pygame.K_UP ))
    def down(self):
        return ( ( event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN ) )

    def update(self,i):

        if (pygame.key.get_pressed()[pygame.K_RIGHT]):
            i=(3*i)//2

        if (pygame.key.get_pressed()[pygame.K_LEFT]):
            i=0

        if ( pygame.key.get_pressed()[pygame.K_UP] ):
            self.inc_y=-i
        else:
            self.inc_y=i
        self.rect.y+=int(self.inc_y)

pygame.init()

pygame.key.set_repeat (500, 30)

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

pygame.mixer.music.load('track.mp3')
pygame.mixer.music.play()


brick = pygame.image.load( 'brick.jpeg')
space = pygame.image.load( 'space_craft.png')
sky = pygame.image.load( 'sky.gif')
fire = pygame.image.load( 'fire.png')

myfont = pygame.font.SysFont("monospace", 50)

size = [CONST_W, CONST_H]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Defend the Ship")

done = False
clock = pygame.time.Clock()

screen.fill(BLACK)

game_heli = simulation()
game_heli.list_start()

label = myfont.render("Controls:    Upward thrust - UP KEY",1,WHITE)
screen.blit(label, (100, 220))

label = myfont.render("                     Downward thrust - NO KEY",1,WHITE)
screen.blit(label, (100, 270))

label = myfont.render("                     More thrust - RIGHT KEY ",1,WHITE)
screen.blit(label, (100, 320))

label = myfont.render("                     0 Vertical thrust - LEFT KEY ",1,WHITE)
screen.blit(label, (100, 370))

label = myfont.render("     Press ANY KEY to start ",1,WHITE)
screen.blit(label, (100, 420))


pygame.display.flip()

loop = False
key = True

while not done:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True 

    if pygame.key.get_pressed()[pygame.K_UP]  and key :
        loop = True
        key = False

    if loop:
        loop = game_heli.display_list()
    else:
        pygame.display.flip()

pygame.quit()



