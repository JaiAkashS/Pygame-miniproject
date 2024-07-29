import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player=pygame.image.load('C:\\Users\\Tharun\\Documents\\CodingStuff\\Pygame Miniproject\\mando100.png')
playerrect=player.get_rect()
playerrect.x=350
pos=[1280,600]
speed=[-20,0]
score=0
obstacles = []
obstacle = pygame.image.load('C:\\Users\\Tharun\\Documents\\CodingStuff\\Pygame Miniproject\\obstacle.png')
pygame.font.init()
font = pygame.font.Font(None, 36)
def create_obstacle():
    obstacle = pygame.image.load('C:\\Users\\Tharun\\Documents\\CodingStuff\\Pygame Miniproject\\obstacle.png')
    obstacle_rect = obstacle.get_rect()
    obstacle_rect.right = 1280
    obstacle_rect.bottom = 600
    return obstacle_rect
# Constants for jump
gravity = 0.5
jump_strength = -10
vertical_speed = 0
for _ in range(3):
    obstacles.append(create_obstacle())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerrect.y += -10
            if event.key == pygame.K_LEFT:
                playerrect.x += -10
            if event.key == pygame.K_RIGHT:
                playerrect.x += 10
            if event.key == pygame.K_DOWN:
                playerrect.y += 10
        
        else:
            pass

    score+=1
    print(score)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    text_rect = score_text.get_rect()
    text_rect.topleft = (10, 10)

    # Apply gravity to the vertical speed
    
    if playerrect.bottom >= 600:
        playerrect.bottom = 600
        vertical_speed = 0

    screen.fill("purple")
    screen.blit(player,playerrect)
    pygame.draw.rect(screen, (255,255,255), [0, 600, 1300, 600], 1000)  
    screen.blit(score_text, text_rect)

   
    pygame.display.flip()
    clock.tick(60)
pygame.quit()