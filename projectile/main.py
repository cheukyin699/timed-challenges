import pygame
import math

pygame.init()

# Constants
SIZE = [500, 500]
WHITE = (200, 200, 200)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

BALL_R = 10

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Projectile Game')
running = True

# For rendering fonts
font_name = pygame.font.get_default_font()
dfont = pygame.font.SysFont(font_name, 40, True)

# 30 FPS
clock = pygame.time.Clock()

ball = [0, 0]   # location of ball
angle = math.radians(45)    # angle of fire
timer = 5 * 1e3       # miliseconds
state = 0
# 0 - started timer
# 1 - started firing ball
# 2 - ended game (restart?)
clicks = 0
scale = 1
vx, vy = 0, 0


def get_ball_y(vy, t):
    '''
    Function to get y position of ball
    '''
    return vy * t - 0.5 * 9.8 * t ** 2


def get_ball_x(vx, t):
    return vx * t


def clicks_to_speed(clicks, scale):
    return clicks * scale


def speed_to_unitvec(speed, angle):
    '''
    Returns vx, vy as tuple
    '''
    return speed * math.cos(angle), speed * math.sin(angle)


while running:
    delta = clock.tick(30)
    # Event handling
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        if evt.type == pygame.MOUSEBUTTONUP:
            if state == 0:
                clicks += 1

    # Updates
    if state == 0:
        timer -= delta
        if timer <= 0:
            # Change state
            state = 1
            # init variables
            timer = 0
            vx, vy = speed_to_unitvec(clicks_to_speed(clicks, scale), angle)
    elif state == 1:
        timer += delta
        ball[0] = get_ball_x(vx, timer / 1.0e3)
        ball[1] = get_ball_y(vy, timer / 1.0e3)
        if ball[1] <= 0 and ball[0] > 0:
            # Change state
            state = 2

    # Drawing on screen
    screen.fill((0, 0, 0))
    if state == 0:
        # Display clicking text
        seconds = str(timer / 1.0e3)
        t = dfont.render(seconds, True, RED)
        screen.blit(t, (SIZE[0] / 2, SIZE[1] / 2))
    elif state == 1:
        # Display moving ball
        pos = list(map(int, ball[:]))
        pos[1] = int(SIZE[1] - pos[1])
        pygame.draw.circle(screen, BLUE, pos, BALL_R)
    elif state == 2:
        # Display text
        t = dfont.render("You lasted %.2f seconds!" % (timer / 1e3),
                         True, WHITE)
        screen.blit(t, (0, 0))
    pygame.display.flip()

pygame.quit()
