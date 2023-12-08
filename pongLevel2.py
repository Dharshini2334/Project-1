############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: PONG                               #####
##### PROJECT ID: CYBX003                              #####
#####                                                  #####
############################################################

#Importing the module pygame
import random
import pygame

pygame.init()

#Setting our window screen
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption('Pong Game')

#Colours that will be used in the game
white = (255, 255, 255)
aquamarine4 = (69, 139, 116)

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

#Texts to be displayed in the background
background_texts = [
    "Nice shot!",
    "Great move!",
    "You're on fire!",
    "Keep it up!",
    "Amazing!",
    "Fantastic!"
]


def get_random_background_text():
    return random.choice(background_texts)

def redraw(background_text):
    win.fill(aquamarine4)
    font = pygame.font.SysFont('Comic Sans MS', 30)
    levelText = 'PONG GAME - Level ' + str(level)
    text = font.render(levelText, False, white)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 25)
    win.blit(text, textRect)

    # Display background text
    background_text_render = font.render(background_text, False, white)
    background_text_rect = background_text_render.get_rect()
    background_text_rect.center = (750 // 2, 75)
    win.blit(background_text_render, background_text_rect)

    p1_score = font.render(str(paddle1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    win.blit(p1_score, p1Rect)

    p2_score = font.render(str(paddle2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    win.blit(p2_score, p2Rect)

    all_sprites.draw(win)
    pygame.display.update()

def draw_quiz(question, true_button, false_button):
    win.fill(aquamarine4)
    font = pygame.font.SysFont('Comic Sans MS', 15)
    question_text = font.render(question["question"], True, white)
    question_rect = question_text.get_rect(center=(750 // 2, 100))
    win.blit(question_text, question_rect)

    pygame.draw.rect(win, (0, 255, 0), true_button)
    pygame.draw.rect(win, (255, 0, 0), false_button)

    true_text = font.render("True", True, white)
    true_rect = true_text.get_rect(center=true_button.center)
    win.blit(true_text, true_rect)

    false_text = font.render("False", True, white)
    false_rect = false_text.get_rect(center=false_button.center)
    win.blit(false_text, false_rect)

    pygame.display.update()

def quiz(true_button, false_button):
    questions_for_level = {
        2: [
            {"question": "The evolution of computer science began beofre the development of the first computer system", "answer": False},
            {"question": "The first slide rule appeared around 1622", "answer": True},
            {"question": "An algorithm is usless when its too long to execute", "answer": False},
            {"question": "Computer science is the study of computers", "answer": False},
            {"question": "Algorithms are exclusive to the field of computer science", "answer": False}
        ],
        3: [
            {"question": "The first electronic programmable computer is ENIAC", "answer": True},
            {"question": "All conceivable problems can be solved algorithmically", "answer": True},
            {"question": "Jacquard's loom was the first programmable device", "answer": True},
            {"question": "Algorithms usually contain a set of instructions to be executed in any order", "answer": False},
            {"question": "During the 3rd generation of computing, the desktop machine shrunk", "answer": False}
        ]
        # Add more levels and questions as needed
    }

    questions = questions_for_level.get(level, [])
    for question in questions:
        draw_quiz(question, true_button, false_button)

        answer = None
        while answer is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if true_button.collidepoint(event.pos):
                        answer = True
                    elif false_button.collidepoint(event.pos):
                        answer = False

        if answer == question["answer"]:
            feedback_text = "Correct!"
            print(feedback_text)
        else:
            feedback_text = "Incorrect!"
            print(feedback_text)

        draw_quiz_feedback(feedback_text)
        pygame.time.delay(2000)

def draw_quiz_feedback(feedback_text):
    font = pygame.font.SysFont('Comic Sans MS', 15)
    feedback_render = font.render(feedback_text, True, white)
    feedback_rect = feedback_render.get_rect(center=(750 // 2, 400))
    win.blit(feedback_render, feedback_rect)
    pygame.display.update()

run = True
background_text = get_random_background_text()
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 10000)  # Set a timer event every 10 seconds

true_button = pygame.Rect(250, 200, 100, 50)
false_button = pygame.Rect(400, 200, 100, 50)

while run:
    pygame.time.delay(120)  # Reduced delay for smoother paddle movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == timer_event:
            background_text = get_random_background_text()

    if paddle1.points >= 2 or paddle2.points >= 2:
        level += 1
        print("Level:", level)
        paddle1.points = 0
        paddle2.points = 0

        # Display quiz between levels
        redraw(background_text)
        quiz(true_button, false_button)

    if level > 3:
        print('Stop')
        ball.speed = 0
        run = False

    if level == 3:
        speedFactor = 3

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and paddle1.rect.y > 0:
        paddle1.rect.y -= paddle_speed
    if key[pygame.K_s] and paddle1.rect.y < 425:
        paddle1.rect.y += paddle_speed
    if key[pygame.K_UP] and paddle2.rect.y > 0:
        paddle2.rect.y -= paddle_speed
    if key[pygame.K_DOWN] and paddle2.rect.y < 425:
        paddle2.rect.y += paddle_speed

    ball.rect.x += (ball.speed * level) * ball.dx
    ball.rect.y += (ball.speed * level) * ball.dy

    if ball.rect.y > 490:
        ball.dy = -1

    if ball.rect.x > 740:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = -1
        paddle1.points += 1
        print("Player 1 scores!", background_text)

    if ball.rect.y < 10:
        ball.dy = 1

    if ball.rect.x < 10:
        ball.rect.x, ball.rect.y = 375, 250
        ball.dx = 1
        paddle2.points += 1
        print("Player 2 scores!", background_text)
    
    if paddle1.rect.colliderect(ball.rect):
        ball.dx = 1
    
    if paddle2.rect.colliderect(ball.rect):
        ball.dx = -1

    redraw(background_text)

pygame.quit()
