
import pygame 

pygame.font.init()
pygame.mixer.init()

WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pong")
WHITE = (255,255,255)
BLACK = (0,0,0)
border = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
points = 0

fps = 120
speed = 10
b_speed = 11
bat_height = 70
bat_width = 20

bat_image = pygame.image.load("images/rectangle.png")
bat = pygame.transform.scale(bat_image,(bat_height,bat_width))

ball_image = pygame.image.load("images/ball.png")
ball = pygame.transform.rotate(ball_image,1)

screen_image = pygame.image.load("images/screen.jpeg")
screen = pygame.transform.scale(screen_image,(WIDTH,HEIGHT))

def draw_window():
    screen.blit(screen,(0,0))
    