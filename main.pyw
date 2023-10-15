import pygame
import math
import random
import os
from pygame import mixer

#AI
import cv2
from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.8, maxHands=1)
video=cv2.VideoCapture(0)


pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 700

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#caption and dp
pygame.display.set_caption("INFINITE RUNNER")
icon = pygame.image.load('player.png')
pygame.display.set_icon(icon)


#load image
bg = pygame.image.load("front.png").convert()
game_bg = pygame.image.load("bg.jpeg").convert()
you_lose = pygame.image.load('lose.png').convert()
bg_width = bg.get_width() 
bg_rect = bg.get_rect()

#game run status variable
run = False

# BGM

menu_bgm = mixer.Sound('main menu.mp3')
game_bgm = mixer.Sound('bg(4).mp3')
if run == False :
    menu_bgm.play(-1) 

#define game variables

scroll = 0
FPS = 60


tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1
         
#Event handler
def event_handler():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      os._exit(0)
      
    if event.type == pygame.KEYDOWN:                          #Keydown check
      if event.key == pygame.K_ESCAPE: 
        os._exit(0)



#GAME OVER
def game_over(score_value):
    font2 = pygame.font.Font('sabo.otf', 35)
    gameover_bgm = mixer.Sound('game_over.mp3')
    gameover_bgm.play()
    pygame.display.flip()
    for i in range(4,0,-1):
      screen.blit(you_lose, (0, 0))
      score = font2.render('YOU SCORED : ' + str(score_value), True, (0,0,0))
      screen.blit(score, (750, 650))
      exit_time = font2.render('Game exits in  ' + str(i) +' sec', True, (0,0,0))
      screen.blit(exit_time, (750, 600))
      pygame.display.flip()
      event_handler()
      pygame.time.delay(1000)
    
              
        
#draw scrolling background
def infinite_scroll():
  global scroll
  for i in range(0, tiles):
    screen.blit(game_bg, (i * bg_width + scroll, 0))
  clock.tick(FPS)

  #scroll background
  scroll -= 5

  #reset scroll
  if abs(scroll) > bg_width:      #scroll = image width ==> image out of screen
    scroll = 0

#Score
def show_score(x, y,score):
    score = font.render('SCORE : ' + str(score), True, (128,128,128))
    screen.blit(score, (x, y))

#collision 
def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if distance < 50:
        return True
    else:
        return False


#Opening screen

count = 0
startgame_x = 120
startgame_y = 600
while True:
  #AI
  fingersup_count = 0
  ret,frame=video.read()
  hands,img=detector.findHands(frame)
  if hands:
      lmList = hands[0]
      fingersUp = detector.fingersUp(lmList)
      print(fingersUp)
      for i in fingersUp:
        if i == 1:
          fingersup_count +=1
    
  if fingersup_count == 2:
    run = True

  #Gamplay
  count+=1
  screen.blit(bg, (0, 0))
  screen.blit(bg, (bg_width, 0))

  font = pygame.font.Font('sabo.otf', 35)

  if count%2 == 0:
    score = font.render('SHOW ANY TWO FINGERS OR PRESS SPACE TO START ', True, (0, 0, 0))
    screen.blit(score, (startgame_x, startgame_y))
  else:
    score = font.render('SHOW ANY TWO FINGERS OR PRESS SPACE TO START ', True, (128,128,128))
    screen.blit(score, (startgame_x, startgame_y))
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE: 
        os._exit(0)       
      if event.key == pygame.K_SPACE:
        run = True
        break                  
        
    if event.type == pygame.QUIT:
      os._exit(0)

  if run == False:
    continue
  else:
    break
    
  

#-----------
#Game screen
#-----------

#Player
player = []
for i in range(15):
  img = pygame.image.load('run ('+str(i+1)+').png')
  player.append(img)

#player coordinates and variables
player_x = 100
player_y = 530
y_change = 0 
gravity = 10
jump = False


#Defender
game_speed = 15
interval = 1
def_y = 540
def_img = []
def_x = []
defender = pygame.image.load('331.png')

for i in range(1000):
  if i%100 == 0:
    def_img.append(defender)
    def_x.append(random.randint(1280,1500))

cnt = 1

#bgm
if run:
    menu_bgm.stop()
    game_bgm.play(-1)

#Game loop
while run:
    cnt+=1
    seconds = pygame.time.get_ticks()/1000
    
    #AI
    ret,frame=video.read()
    hands,img=detector.findHands(frame)

    #bg
    infinite_scroll()
    
  
    #Sprite blit
    screen.blit(player[0],(player_x,player_y))
    player.append(player[0])
    player.remove(player[0])


    #Close event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os._exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                os._exit(0)

    #player movement mechanics
    if hands:
      lmList = hands[0]
      fingerUp = detector.fingersUp(lmList)
      print(fingerUp)
      if fingerUp==[1,1,1,1,1] and player_y == 530:
        y_change = 80
        jump = True
                                   
    if jump == True :
      player_y -= y_change
      y_change -= gravity

    if player_y > 530:
      player_y = 530
      y_change = 0
      jump = False

    
    #speed increase
    if int(seconds) % 5 == 0:
      game_speed += 0.05
    

    #Defenders
    i = 0
    if seconds % random.random() == 0:  
        screen.blit(def_img[i],(def_x[i],def_y)) 
        def_x[i] -= game_speed
        collision_enemy = isCollision(def_x[i], 550,100, player_y)
        
        if collision_enemy == True:
            break

    else:
        screen.blit(def_img[i],(def_x[i],def_y)) 
        def_x[i] -= game_speed
        collision_enemy = isCollision(def_x[i], 550,100, player_y)

        if collision_enemy == True:
            game_bgm.stop()
            break
        if def_x[i] < -100:
            def_x[i] = random.randint(1280,1500)
        i+=1
             
    show_score(1050, 10,int(seconds))
    
    pygame.display.flip()
    
    small_frame = cv2.resize(frame,(0,0),fx=0.3,fy = 0.25)
    cv2.imshow('frame',small_frame)

game_over(int(seconds))

pygame.quit()
video.release()
cv2.destroyAllWindows()


