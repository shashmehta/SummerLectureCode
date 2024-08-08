import pygame

#Init pygame and pygame screen
pygame.init
screen = pygame.display.set_mode((1000,500), pygame.RESIZABLE)
pygame.display.set_caption("Robot Controller")

#Set up the black color
BLACK = (0,0,0)
BLUE = (2,130,242)

#Set up the run variable for the main WHILE loop. When run is false the game will stop.
Run = True


#Position for the circle/robot to draw
x = 400
y = 200

#Pygame Loop
while Run:
    
    #Reset the screen
    screen.fill(BLACK)
    
    #Draw the circle
    pygame.draw.circle(screen, BLUE, (x,y), 25)
    
    keys = pygame.key.get_pressed()
    
    #Moves circle and motor based off keypress
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += 5
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= 5
    
    #Stop the motors and update the display
    pygame.display.update()
    
    
    #Quits the game
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Run = False
        if event.type == pygame.QUIT:
            Run = False
                
pygame.quit