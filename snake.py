import random
import pygame
grid_size = 40
food = (random.randint(10, grid_size - 10), random.randint(10, grid_size - 10))
from sys import exit
pygame.init()
direction = (0, 0)
pygame.display.set_caption('Snake Game')
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
snake_pos = [(20,20)]
Score=0
apple_surface = pygame.image.load('apple_1_0.png').convert_alpha()
apple_surface = pygame.transform.rotozoom(apple_surface, 0, 0.01)
apple_rect = apple_surface.get_rect(topleft=(food[0]*10, food[1]*10))
speed=10
game_over=False

def draw():
    global apple_rect
    screen.fill((250, 250, 250))
    for pos in snake_pos:
        rec = (pos[0]*10, pos[1]*10, 20, 20)
        pygame.draw.rect(screen, (255, 0, 0), rec)

    # pygame.draw.rect(screen, (0, 0, 255), (food[0]*10, food[1]*10, 30, 30))
    apple_surface = pygame.image.load('apple_1_0.png').convert_alpha()
    apple_surface = pygame.transform.rotozoom(apple_surface, 0, 0.015)
    apple_rect = apple_surface.get_rect(topleft=(food[0]*10, food[1]*10))
    screen.blit(apple_surface, apple_rect)
    score()


def score():    
    global Score
    font = pygame.font.Font(None, 26)
    score_surf = font.render(f'Score: {Score}', True, (100, 0, 0))
    score_surf_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_surf_rect)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # w = random.randint(50, 550)
    # h = random.randint(50, 350)
    # apple_rect.midbottom = (w,h)
    # screen.blit(apple_surface, apple_rect)
    if game_over==False: 
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            direction = (1, 0)
            
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            direction = (-1, 0)
        
        if pygame.key.get_pressed()[pygame.K_UP]:
            direction = (0, -1)
            
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            direction = (0, 1)
       


        headx, heady = snake_pos[0]
        dx, dy = direction
        new_head = (headx + dx) % grid_size, (heady + dy) % grid_size

        snake_pos = [new_head] + snake_pos

        if pygame.Rect(new_head[0]*10, new_head[1]*10, 20, 20).colliderect(apple_rect):
            food = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
            Score += 1
        else:
                snake_pos.pop()

        if Score%10==0 and Score!=0:
            speed=10+(Score//10)*5
        if food in snake_pos[1:]:
            while food in snake_pos[1:]:
                food = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        draw()
        if snake_pos[0] in snake_pos[1:]:
            snake_pos = [new_head]
            Score=0
            game_over=True
        print(speed)

    else:
        game_over_surf = pygame.font.Font(None, 100).render('Game Over', True, (255, 0, 0))
        game_over_rect = game_over_surf.get_rect(center=(200, 150))
        screen.blit(game_over_surf, game_over_rect)
        instraction_surf = pygame.font.Font(None, 50).render('Press space to Restart', True, (0, 0, 0))
        instraction_rect = instraction_surf.get_rect(center=(200, 200))
        screen.blit(instraction_surf, instraction_rect)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            game_over=False
            snake_pos = [(20,20)]
            direction = (0,0)
            food = (random.randint(0, grid_size - 5), random.randint(0, grid_size - 5))
            speed=10

    pygame.display.flip()
    clock.tick(speed)