import pygame

# Tower Defense Game


pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width/2, screen.get_height/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill('purple')

    pygame.draw.circle(screen, 'red', player_pos, 40)

    key = pygame.key.get_pressed()
    if keys[pygame.K_w]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()