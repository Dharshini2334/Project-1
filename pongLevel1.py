############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: PONG                               #####
##### PROJECT ID: CYBX003                              #####
#####                                                  #####
############################################################

#Importing the module pygame
import pygame

pygame.init()

#Setting our window screen
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption('Pong Game')


#Colours to be used in the game
white = (255, 255, 255)
aquamarine4 = (69,139,116)	

#Level
level = 1

#Speed Factor
speedFactor = 1


#creating a class of objects to be used in the game such as the paddle and ball
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.dx = 1
        self.dy = 1

paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

paddle_speed = 25

ball = Ball()
ball.rect.x = 375
ball.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ball)

#Displaying the game screen
def redraw():
    win.fill(aquamarine4)
    #Title Font
    font = pygame.font.SysFont('Comic Sans MS', 30)
    levelText = 'PONG GAME - Level ' + str(level)
    text = font.render(levelText, False, white)
    textRect = text.get_rect()
    textRect.center = (750//2, 25)
    win.blit(text, textRect)

    #Player 1 Score
    p1_score = font.render(str(paddle1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    win.blit(p1_score, p1Rect)

    #Player 2 Score
    p2_score = font.render(str(paddle2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    win.blit(p2_score, p2Rect)


    all_sprites.draw(win)
    pygame.display.update()

#Displaying the game screen
def flashLevel():
    win.fill(aquamarine4)
    #Title Font
    font = pygame.font.SysFont('Comic Sans MS', 30)
    flashLevelText = 'LEVEL: ' + str(level)
    text = font.render(flashLevelText, False, white)
    textRect = text.get_rect()
    textRect.center = (750//2, 750//2)
    win.blit(text, textRect)

    #Player 1 Score
    p1_score = font.render(str(paddle1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    win.blit(p1_score, p1Rect)

    #Player 2 Score
    p2_score = font.render(str(paddle2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    win.blit(p2_score, p2Rect)


    all_sprites.draw(win)
    pygame.display.update()    


#Main loop
run = True
while run:
    pygame.time.delay(125)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # if points are above 5
    if paddle1.points >= 5 or paddle2.points >= 5:
        level += 1
        print(str(level))
        # flashLevel()
        paddle1.points = 0
        paddle2.points = 0  

    # stop after the forth level
    if level > 3:
        print('Stop')
        ball.speed = 0
        run = False

    # increase the paddle speed for levels 3 and 4
    if level == 3:
        speedFactor = 2

    #Control keys (up & down, w & s keys respectively)
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y += -(paddle_speed * speedFactor)
    if key[pygame.K_s]:
        paddle1.rect.y += (paddle_speed * speedFactor)
    if key[pygame.K_UP]:
        paddle2.rect.y += -(paddle_speed * speedFactor)
    if key[pygame.K_DOWN]:
        paddle2.rect.y += (paddle_speed * speedFactor)

    #Ball movement
    ball.rect.x += (ball.speed * level) * ball.dx
    ball.rect.y += (ball.speed * level) * ball.dy

    #Ball collisions with the walls i.e The ball bounces back instead of moving continously
    if ball.rect.y > 490:
        ball.dy = -1

    if ball.rect.x > 740:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = -1
        paddle1.points +=1

    if ball.rect.y < 10:
        ball.dy = 1

    if ball.rect.x < 10:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = 1
        paddle2.points += 1
    
    if paddle1.rect.colliderect(ball.rect):
        ball.dx = 1

    if paddle2.rect.colliderect(ball.rect):
        ball.dx = -1 

    #Calling the redraw function
    redraw() 

pygame.quit()
    
