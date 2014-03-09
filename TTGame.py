import pygame
from pygame.locals import *
import sys, os
import random
from math import *

pygame.init()

Screen = (800,600)
Surface = pygame.display.set_mode(Screen)
Ping = pygame.mixer.Sound('Ping.wav')
Click = pygame.mixer.Sound('Click.wav')
pygame.display.set_caption("TTGame - By JKG, AM & PG")                       
icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
Ping.set_volume(0.4)
Click.set_volume(0.4)

def stadium() :
        global Screen , Surface , Ping , Click, icon, white, black, clock, Font, Font2, Font3, Font4, CirclesInTheAir, speed,Circles,Paddles,PScore, AIScore
        Screen = (800,600)
        Surface = pygame.display.set_mode(Screen)
        Ping = pygame.mixer.Sound('Ping.wav')
        Click = pygame.mixer.Sound('Click.wav')
        pygame.display.set_caption("new tt V.2.0.1- By JKG, AM & PG")                       
        icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
        Ping.set_volume(0.4)
        Click.set_volume(0.4)
        white = [255, 255, 255]
        black = [0, 0, 0]
        clock = pygame.time.Clock()
        # Storing Font types
        Font = pygame.font.Font(None,12)        
        Font2 = pygame.font.Font(None,18)
        Font3 = pygame.font.Font(None,32)
        Font4 = pygame.font.Font(None,48)

        CirclesInTheAir = 1             # Number of Cirles in the stadium
        speed=50
        Circles = []                    # List to store stoboscopic balls
        
        #Appear the balls in middle of the screen
        for x in xrange(CirclesInTheAir):
            Circles.append(Circle(Screen[0]/2,Screen[1]/2))
        Paddles = []    #Declaring list to store all the paddles
        #To show paddles on the screen
        Paddles.append(Paddle(Screen[0]/2,10,10,1))
        Paddles.append(Paddle(Screen[0]/2,590,10,2))
        PScore = 0      #To store player score
        AIScore = 0     #To store computer's score




##pygame.mouse.set_visible(False)


white = [255, 255, 255]
black = [0, 0, 0]
clock = pygame.time.Clock()

Font = pygame.font.Font(None,12)
Font2 = pygame.font.Font(None,18)
Font3 = pygame.font.Font(None,32)
Font4 = pygame.font.Font(None,48)

CirclesInTheAir = 1
speed=50

###################################################################################################################################################################
# This is a menu class module. 
# SimMen - menu class module.

class Menu():
        # Menu class definition
        # need a position to init, minimum
        # Provides some limited cusomizability
        # Uses system font so it's compatible with anything
        def __init__(self, pos, data=[], textsize=32,\
                        wordcolor=[255, 255, 0], backcolor=[0, 0, 255], selectedcolor=[0, 255, 255], lprn=20):
                import pygame
                self.rect = pygame.Rect((pos), (0, 0))
                self.data = data
                self.textrects = []
                self.textsurfs = []
                self.cursorpos = 0
                self.pos = pos
                self.font = pygame.font.SysFont(None, 32)
                self.wordcolor = wordcolor
                self.backcolor = backcolor
                self.selectedcolor = selectedcolor
                self.textsize = textsize
                self.looprun = lprn#looprun
                self.scroll = False
                self.selected = False
                for word in self.data:
                        self.textsurfs.append(self.font.render(str(word), True, self.wordcolor))
                        rect = self.font.render(str(word), True, self.wordcolor).get_rect()
                        self.textrects.append(rect)
        def add(self, words):
                # add one or more elements of data
                self.data.extend(words)
                for word in words:
                        self.textrects.append(self.font.render(str(word), True, self.wordcolor).get_rect())
                        self.textsurfs.append(self.font.render(str(word), True, self.wordcolor))
        def remove(self, item=False):
                if not item:
                        # Remove the last element of data
                        self.data.pop()
                        self.textrects.pop()
                        self.textsurfs.pop()
                else:
                        thingpop = self.data.index(item)
                        self.data.pop(thingpop)
                        self.textrects.pop(thingpop)
                        self.textsurfs.pop(thingpop)
        def update(self, Surface, event):
                import pygame
                # Blit and updated the text box, check key presses
                height = 0
                curpos = []# Stop python from making curpos and self.pos point to the same list
                for n in self.pos:
                        curpos.append(n)
                curpos[0] += 1
                self.rect.height = len(self.data)*self.textsize# Define the max height of the text box
                if self.rect.height > Surface.get_height():
                        self.scroll = True
                else:
                        self.scroll = False
                # Define the max width of the text box based on the word length it holds
                maxsize = sorted(self.data)
                maxsize = len(maxsize[0])
                self.rect.width = maxsize*self.textsize/2
                pygame.draw.rect(Surface, self.backcolor, self.rect)# Draw the text box
                pygame.draw.rect(Surface, self.wordcolor, self.rect, 1)# Draw the text box outline
                
                # Update rects and surfaces
                for surf in self.textsurfs:
                        if not self.textsurfs.index(surf) == self.cursorpos:
                                Surface.blit(surf, curpos)
                                self.textrects[self.textsurfs.index(surf)].topleft = curpos
                        else:
                                rect = self.textrects[self.textsurfs.index(surf)]
                                rect.topleft = curpos
                                surf = self.font.render(str(self.data[self.textsurfs.index(surf)]), True, self.selectedcolor)
                                Surface.blit(surf, curpos)
                        curpos[1] += self.textsize
                e = event
                if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_UP:
                                if self.cursorpos > 0:
                                        self.cursorpos -= 1
                        elif e.key == pygame.K_DOWN:
                                if self.cursorpos < len(self.data)-1:
                                        self.cursorpos += 1
                        elif e.key == pygame.K_SPACE:
                                self.selected = self.data[self.cursorpos]
                elif e.type == pygame.MOUSEMOTION:
                        mousepos = pygame.mouse.get_pos()
                        for rect in self.textrects:
                                if rect.collidepoint(mousepos):
                                        self.cursorpos = self.textrects.index(rect)
                elif e.type == pygame.MOUSEBUTTONDOWN:
                        self.selected = self.data[self.cursorpos]
                elif e.type == pygame.QUIT:
                        self.selected = pygame.QUIT
                return





class Circle:           #class defining features of ball 
    def __init__(self,x,y):
        self.x = x              #x-coordinate of centre of ball
        self.y = y              #y-coordinate of centre of ball
        angle = random.randint(0,360)           #randomizing the angle at which ball is deflecting at the start
        self.speedy = 0.7*cos(radians(angle))   #To randomize speed
        self.speedx = 0.7*sin(radians(angle))   #To randomize speed
        self.placesbeen = []    # Recording places where ball had been for stroboscopic images
        self.radius = 5
        self.add = 0            #Number of stroboscopic ball
        self.stopped = False
        self.stoppedtime = 0
Circles = []    #Declaring list to store all the balls

#Appear the balls in middle of the screen
for x in xrange(CirclesInTheAir):
    Circles.append(Circle(Screen[0]/2,Screen[1]/2))

#class defining features of paddle
class Paddle:
    def __init__(self,x,y,size,player):
        self.rect = [x,y,100,size]
        self.player = player
        
Paddles = []    #Declaring list to store all the paddles
#To show paddles on the screen
Paddles.append(Paddle(Screen[0]/2,10,10,1))
Paddles.append(Paddle(Screen[0]/2,590,10,2))
PScore = 0      #To store player score
AIScore = 0     #To store computer's score


#To Display the menu
def menu():
        global Surface, black, white, clock, Menu
        titlemenu = Menu([20, 65], wordcolor=[255, 0, 0], selectedcolor=[255, 255, 0], data=['Easy', 'Med', 'Hard', 'Quit'])
        Surface.fill(black)
        pygame.mouse.set_visible(True)
        font = pygame.font.Font(None, 32)
        Surface.blit(font.render('The controls are: Left-Right for Player', True, white, black), [0, 0])
        Surface.blit(font.render('The first to score 3 wins the game', True, white, black), [0, 32])
        pygame.display.flip()
        while not titlemenu.selected:           # Pausing till the input is recieved
                titlemenu.update(Surface, pygame.event.poll())
                clock.tick(30)
                pygame.display.flip()

        if titlemenu.selected == 'Easy':
            main(100)    
        elif titlemenu.selected == 'Med':
            main(70)
        elif titlemenu.selected == 'Hard':
            main(20)
        else:
            pygame.quit()
            sys.exit()
            
#To define functions of keyboard keys
def GetInput():
    key = pygame.key.get_pressed()
    for event in pygame.event.get():    # Taking Keyboard Event
        if event.type == QUIT or key[K_ESCAPE]:         # If exit button clicked
            pygame.mouse.set_visible(True)              # Or Esc key pressed
            pygame.quit(); sys.exit()                   # Exit
    if key[K_SPACE]:                                    # If SPACE pressed
            AIScore = 0
            PScore = 0
            stadium()                                   # Rebuild the surface
            menu()                                      # Calling Menu
        # Player Controls
    if key[K_RIGHT]:
        for p in Paddles:
            if p.player == 1: p.rect[0] += 3
    if key[K_LEFT]:
        for p in Paddles:
            if p.player == 1: p.rect[0] -= 3

#To update stroboscopic balls and moving the AI paddle
def Update(difficulty):
    for c in Circles:
        if c.add == 0:
            c.placesbeen.append([c.x,c.y])      # Storing Last positions of the ball
            c.placesbeen.reverse()
            c.placesbeen = c.placesbeen[:25]
            c.placesbeen.reverse()
            c.add = 15
        else:
            c.add -= 1
        if c.stoppedtime == 375:    # After 375ms stroboscopic balls are deleted
            Circles.remove(c)
            continue
    if len(Circles) < CirclesInTheAir:  # Ball added 
       Circles.append(Circle(Screen[1]/2,Screen[0]/2))
    # AI Paddle
    for p in Paddles:
        if p.player == 2:
            k= p.rect[0]-c.x
            if k<0:
               p.rect[0]-=k/difficulty

            elif k>=0:
                p.rect[0]-=k/difficulty

#To update the position of the ball          
def Move(diff):
    for c in Circles:
        c.x += c.speedx
        c.y += c.speedy
    Update(diff)

#To detect the collisions of the ball with wall or the paddles
def CollisionDetect():
    global PScore, AIScore, Click, Ping
    for c in Circles:
        if c.y <= 0-c.radius:                   #To detect the collision with AI paddle
            if not c.stopped:
                c.stopped = True
                c.speedx = 0
                c.speedy = 0
                if AIScore<3 and PScore<3:      # Check for current scores
                        AIScore += 1            # Update score
                
            else:
                c.stoppedtime += 1
                        
        if c.x <=0:                             #To detect the collision with left wall
            c.x = 0
            c.speedx *= -1
            Click.play(0)
        if c.y >= Screen[1]+c.radius:           #To detect the collision with player paddle
            if not c.stopped:
                c.stopped = True
                c.speedx = 0
                c.speedy = 0
                if AIScore<3 and PScore<3:      # Check for current scores
                        PScore += 1             # Update score
            else:
                c.stoppedtime += 1
        
        if c.x >= Screen[0]:                   #To detect the collision with right wall
            c.x = Screen[0]
            c.speedx *= -1
            Click.play(0)                       #Play sound
            
    ##This for loop checks left and right limit of paddle.
    for p in Paddles:
        if p.rect[0]-(p.rect[2]/2) < 0:
            p.rect[0] = (p.rect[2]/2)
        if p.rect[0]+(p.rect[2]/2) > Screen[0]:
            p.rect[0] = Screen[0] - (p.rect[2]/2)

    #This for loop detects the collision of the ball with paddle
    for p in Paddles:
        r = PygameRectFromRect(p.rect)
        for c in Circles:
            xdiff = c.x - p.rect[0]
            ydiff = c.y - p.rect[1]
            if abs(xdiff) <= (p.rect[2]/2) + c.radius and abs(ydiff) <= (p.rect[3]/2) + c.radius: #collision
                Ping.play(0)
                c.speedy *= -1
                if ydiff > 0:#lower
                    c.y = r[1] + r[3] + c.radius
                if ydiff < 0:#upper
                    c.y = r[1]-r[3]-c.radius
                c.speedx *= 1.1
                c.speedy *= 1.1
                
#To find size to Render the Rectangle 
def PygameRectFromRect(r):
    tl = (  r[0]-(r[2]/2),  (r[1]+(r[3]/2))  )
    dim = (  r[2],  r[3]  )
    r2 = (tl[0],tl[1],dim[0],dim[1])
    return r2

#To convert the point to the integer
def IntegerisePoint(point):
    returnpoint = [int(round(point[0])),int(round(point[1]))]
    return returnpoint
#To print on the stadium screen the name.
info_text = Font.render("new tt v.2.0.1 ",True,(255,255,255))
info_text_draw_pos = ((Screen[0]/2)-(info_text.get_width()/2),10)

#To Display the result of the match
def Result():
        global Surface, Screen, AIScore, PScore, Font, Font2, Font3, Font4
        p1_score_text = Font3.render("Player, Score "+str(PScore),True,(255,255,255))
        p2_score_text = Font3.render("AI, Score "+str(AIScore),True,(255,255,255))
        p4_text = Font2.render("Press spacebar to return to MAIN MENU ",True,(255,0,255))
        if PScore>AIScore:
                p3_text = Font4.render("You WON! :)", True, (255,0,0))
        else:
                p3_text = Font4.render("You LOST! :(", True, (255,0,0))
                
        Surface.blit(p1_score_text,(Screen[0]/2-p1_score_text.get_width()-20,290))
        Surface.blit(p2_score_text,(Screen[0]/2-p2_score_text.get_width()-20,310))
        Surface.blit(p3_text,(Screen[0]/2+p2_score_text.get_width()-20,300))
        Surface.blit(p4_text,(Screen[0]/2-p2_score_text.get_width()-20,360))
        pygame.display.flip()
        Ping.set_volume(0)
        Click.set_volume(0)
        GetInput()


#To draw the balls and the paddles and update the scores  
def Draw():
    global Surface, Screen, AIScore, PScore, Font, Font2, Font3, Font4
    Surface.fill((0,0,0))
    if PScore<3 and AIScore<3:
        for c in Circles:
                light = 0
                for p in c.placesbeen:
                        point = IntegerisePoint((p[0],Screen[1]-p[1]))
                        pygame.draw.circle(Surface,(light,0,0),point,c.radius)
                        light += 2
                point = IntegerisePoint((c.x,Screen[1]-c.y))
                pygame.draw.circle(Surface,(255,255,255),point,c.radius)
        for p in Paddles:
                r = PygameRectFromRect(p.rect)
                pygame.draw.rect(Surface,(240,120,0),(r[0],Screen[1]-r[1],r[2],r[3]),0)
        Surface.blit(info_text,info_text_draw_pos)
        p1_score_text = Font2.render("Player, Score "+str(PScore),True,(255,255,255))
        p2_score_text = Font2.render("AI, Score "+str(AIScore),True,(255,255,255))
        Surface.blit(p1_score_text,(0+20,20))
        Surface.blit(p2_score_text,(Screen[0]-p2_score_text.get_width()-20,20))
        pygame.display.flip()

       
    else:
        Result()
        
       
#main function determining the order of the calls made to different function        
def main(diff):
    while True:
        GetInput()
        Move(diff)
        CollisionDetect()
        Draw()

    
if __name__ == '__main__': menu()
