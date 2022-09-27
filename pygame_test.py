import pygame



# init
pygame.init()

window_width = 500
window_height = 500

window = pygame.display.set_mode((window_width, window_height))


x = 250
y = 250


object_width = 30
object_height = 30

speed = 0.3


isRun = True
while isRun:
    
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > 0:
        x -= (1 * speed)

    if keys[pygame.K_d] and x < window_width - object_width:
        x += (1 * speed)

    if keys[pygame.K_w] and y > 0:
        y -= (1 * speed)

    if keys[pygame.K_s] and y < window_height - object_height:
        y += (1 * speed)

    # update asset

    window.fill((255, 255, 255)) # color white
    pygame.draw.rect(window, (255, 0, 0), (x, y, object_width, object_height))

    # render to display

    pygame.display.update()



pygame.quit()