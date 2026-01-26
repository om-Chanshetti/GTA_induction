import pygame
import random

from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))

pygame.display.set_caption("T-Rex Runner")
clock = pygame.time.Clock()
obn = random.randint(0, 2)
obn2 = random.randint(0, 2)
obn3 = random.randint(0, 2)
gx=0
ox=800
ox2=1200
ox3=800
value = 0
game_over= False
ty= 395
score = 0
speed=10
def draw():
    global value
    global gx,ty
    global trex_rect
    ground_surf = pygame.image.load('ground2.png').convert_alpha()
    ground_rect = ground_surf.get_rect(midbottom=(gx, 400))
    
    trex_surf = [pygame.image.load('trex1.png').convert_alpha(), pygame.image.load('trex3.png').convert_alpha(),
                    pygame.image.load('trex4.png').convert_alpha()]
    image = trex_surf[value]
    
    trex_rect = image.get_rect(midbottom=(80, ty))
    trex_rect.width = 35
    trex_rect.height = 50
    image = pygame.transform.rotozoom(image, 0, 0.5)
    # pygame.draw.rect(screen, (0,255,0), trex_rect)
    screen.blit(image, trex_rect)
    gx -= 10
    if gx <= -300:
        gx=0

    screen.blit(ground_surf, ground_rect)


def obstacle():
    global ox,ox2
    global obn,obn2
    global i
    global obstacle_rect,obstacle_rect2
    obstacle_surf = [pygame.image.load('obstacle1.png').convert_alpha(),pygame.image.load('obstacle2.png').convert_alpha(),
                     pygame.image.load('obstacle3.png').convert_alpha()]
    obstacle_surf[0] = pygame.transform.rotozoom(obstacle_surf[0],0,0.5)
    obstacle_surf[1] = pygame.transform.rotozoom(obstacle_surf[1],0,0.5)
    obstacle_surf[2] = pygame.transform.rotozoom(obstacle_surf[2],0,0.5)
    obstac= obstacle_surf[obn]
    obstac2= obstacle_surf[obn2]
    obstac3= obstacle_surf[obn3]
   
    obstacle_rect = obstacle_surf[obn].get_rect(midbottom=(ox, 395))
    obstacle_rect2 = obstacle_surf[obn2].get_rect(midbottom=(ox2, 395))
    # pygame.draw.rect(screen, (255,0,0), obstacle_rect)
    # pygame.draw.rect(screen, (255,0,0), obstacle_rect2)
    ox -= 20
    ox2 -= 20
    screen.blit(obstac, obstacle_rect)
    screen.blit(obstac2,obstacle_rect2)
        
    if ox<=0 and game_over== False:
        ox= 800
        obn= random.randint(0,2)
    if ox2<=0 and game_over== False:
        ox2= 800
        obn2= random.randint(0,2)

def Score():    
    global score
    font = pygame.font.Font(None, 26)
    score_surf = font.render(f'Score: {score}', True, (100, 0, 0))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    print(score)
    score += 1


def key_event():
    global game_over,speed,gx,ox,ox2,ox3,value,score
    global trex_rect,ty,obstacle_rect,obstacle_rect2
    keys = pygame.key.get_pressed()
    if game_over== False:
       
        if keys[pygame.K_SPACE] and trex_rect.bottom >= 395:
            while ty > 345:
                ty -= 5
        elif trex_rect.bottom < 395:
            ty+= 10
    else:
        if keys[pygame.K_SPACE]:
            gx=0
            ox=800
            ox2=1200
            ox3=800
            value = 0
            game_over= False
            ty= 395
            score = 0
            speed=10
            
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
    if game_over== False:
        trex_surf = [pygame.image.load('4.png').convert_alpha(), pygame.image.load('3.png').convert_alpha(),
                        pygame.image.load('2.png').convert_alpha()]
        image = trex_surf[value]
        screen.fill((225, 225, 225))
        draw()
        Score()
        obstacle()
        key_event()
        if value < 2:
            value += 1
            image= []
        else:
            value = 0
        if trex_rect.colliderect(obstacle_rect) or trex_rect.colliderect(obstacle_rect2):
            game_over= True
        if score % 100 == 0:
            speed += 3
        clock.tick(speed)
    else:
        game_over_surf = pygame.image.load('gameOver.png').convert_alpha()
        game_over_rect = game_over_surf.get_rect(center=(400, 200))
        screen.fill((225, 225, 225))
        font = pygame.font.Font(None, 30)
        score_surf = font.render(f'Final Score: {score}', True, (100, 0, 0))
        restart_surf = font.render('Press SPACE to Restart', True, (100, 0, 0))
        score_rect = score_surf.get_rect(center=(400, 250))
        restart_rect = restart_surf.get_rect(center=(400, 280))
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(restart_surf, restart_rect)

        key_event()
    pygame.display.flip()