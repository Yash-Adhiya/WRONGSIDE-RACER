import pygame
import time # as we will need at time for restart the game when accident is occures
import random
pygame.init()   # we have to initialize our pygame and display
gray=(119,118,110)#rgb code of selected color
black=(0,0,0) 
red=(255,0,0)
green=(0,200,0)
bright_green=(0,255,0)
bright_red=(255,0,0)
width=800  #--->width of our screen
hight=600  #--->hight of our screen
screen=pygame.display.set_mode((width,hight))  #step of creating display (set_mode)
pygame.display.set_caption("WRONGSIDE RACER")     # our window name is defined by set_caption
clock=pygame.time.Clock() 

# NOW THIS IS THE TIME TO ADD OUR CAR #

carimage=pygame.image.load("bigcar1.png")
backgroundleft=pygame.image.load("left.png")	#load background left side image
backgroundright=pygame.image.load("right.png")	#load background right side image 


#NOW WE HAVE TO ENTER THIS IMAGE BY USING blit function
car_width=65




def car(x,y):
    screen.blit(carimage,(x,y))   #--> Hear blit fn locate our image to the screen and it sets to an allignment of x,y

def background():
	screen.blit(backgroundleft,(0,0))	#set left side position of background image at x #axis & y axis 
	screen.blit(backgroundright,(680,0))	#set right side position of background image at x axis & y axis
    #screen.blit(background_road, (-120,0))
    


# NOW WE WILL WORK ON DESPLAYING MESSAGES WHEN OUR CAR IS CRASHED


# 1)-->decide a text fashion
def text_objects(text,font):
    textsurface=font.render(text,True,black)  # hear render is method and is allow us to print fonts on the game screen
    return textsurface,textsurface.get_rect() # hear get_rect allows us to allign  our fonts in specified area

def message_display(text):    # text are going to be coustomize hear
    bigtext=pygame.font.Font('freesansbold.ttf',80)
    textsurf,textrect=text_objects(text,bigtext)
    textrect.center=((width/2),(hight/2))  # Allignment is set to center at half from both hight and width
    screen.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(2) # hear module time help us to access time that is given as an argument and that is 3 sec (sleep will make screen stuck for a givrn time)
    game_loop()

def accident():
    message_display("GAME OVER")


def obstacles(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("bigcar7.png")
    if obs==1:
        obs_pic=pygame.image.load("bigcar2.png")
    if obs==2:
        obs_pic=pygame.image.load("bigcar3.png")
    if obs==3:
        obs_pic=pygame.image.load("bigcar4.png")
    if obs==4:
        obs_pic=pygame.image.load("bigcar5.png")
    if obs==5:
        obs_pic=pygame.image.load("bigcar6.png")
    if obs==6:
        obs_pic=pygame.image.load("bigcar7.png")
    screen.blit(obs_pic,(obs_startx,obs_starty))

def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render('passed'+str(passed),True,black)
    score=font.render('score'+str(score),True,red)
    screen.blit(text,(0,50))
    screen.blit(score,(0,30))


    
  


def game_loop():  # all the function wll be called in this function only and all work will be done in this fn.
    x=(width*0.45)
    y=(hight*0.75)
    #for another car as an obstacles
    obstacle_speed=20
    obs=0
    y_movement=0
    obs_startx=random.randrange(200,(width-200))
    obs_starty=-750
    obs_width=65
    obs_hight=130
    passed=0
    level=0
    score=0
    # now to move car... initialize its movement by 0
    x_movement=0
    flag=False
    while not flag:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
        
        
        # now set a buttons on key board to move a car
        if event.type==pygame.KEYDOWN: # KEYDOWN indicates when key is pressed
            if event.key==pygame.K_LEFT:
                x_movement=-20
            if event.key==pygame.K_RIGHT:
                x_movement=20
            if event.key==pygame.K_a:
                obstacle_speed+=15
            if event.key==pygame.K_b:
                obstacle_speed-=15
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                x_movement=0
        x+=x_movement
        screen.fill(gray)  # if we not close then it fills it with gray
        background()
        obs_starty-=(obstacle_speed/4)
        obstacles(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed

        car(x,y)
        score_system(passed,score)

        if x>690-car_width or x<130:
            accident()
        
        if x>width-(car_width+130) or x<130:
            accident()
        if obs_starty>hight:
            obs_starty=0-hight
            obs_startx=random.randrange(180,(width-180))
            obs=random.randrange(0,7)
            passed+=1
            score=passed*10
            
             
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+=2
                bigtext=pygame.font.Font('freesansbold.ttf',80)
                textsurf,textrect=text_objects('LEVEL'+str( level),bigtext)
                textrect.center=((width/2),(hight/2))  
                screen.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(2) 
        
        if y<obs_starty+obs_hight:
            if x>obs_startx and x<obs_startx+obs+obs_width or x+car_width> obs_startx and x+car_width<obs_startx+obs<width:
                accident()
            
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
