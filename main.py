import pygame
pygame.init()


win=pygame.display.set_mode((900,500))
pygame.display.set_caption("Game")

yellow_image=pygame.image.load("./Assets/spaceship_yellow.png")
red_image=pygame.image.load("./Assets/spaceship_red.png")

yellow_small=pygame.transform.scale(yellow_image,(50,30))
yellow_player=pygame.transform.rotate(yellow_small,270)

red_small=pygame.transform.scale(red_image,(50,30))
red_player=pygame.transform.rotate(red_small,90)

yellow =pygame.Rect(200,200,50,30)
red =pygame.Rect(700,200,50,30)

FPS =60 
clock=pygame.time.Clock()

run=True
VAL=5
while run :

    clock.tick(FPS)

    win.fill((255,255,255))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

    k_press=pygame.key.get_pressed()
    if k_press[pygame.K_LEFT]:
        red.x-=5
    if k_press[pygame.K_RIGHT]:
        red.x+=5
    if k_press[pygame.K_UP]:
        red.y-=5
    if k_press[pygame.K_DOWN]:
        red.y+=5
    
    if k_press[pygame.K_a]:
        yellow.x-=5
    if k_press[pygame.K_d]:
        yellow.x+=5
    if k_press[pygame.K_w]:
        yellow.y-=5
    if k_press[pygame.K_s]:
        yellow.y+=5


    win.blit(yellow_player,(yellow.x,yellow.y))
    win.blit(red_player,(red.x,red.y))

    # win.blit(yellow_player,(x,y))
    # win.blit(red_player,(x,y))

    

    pygame.display.update()

pygame.quit()



# next tasks :
# drow black border 
# add condition to k_press
