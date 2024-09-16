import pygame
import random
pygame.init()

#defining colors
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# creating window 
screen_witdh = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_witdh, screen_height))
# game title
pygame.display.set_caption("Snake Game")

# creating specific variables
quit_game = False
game_over = False
snake_x = 450
snake_y = 300
snake_size = 15
velocity_x = 0
velocity_y = 0
food_x = random.randint(20, screen_witdh-50)
food_y = random.randint(20, screen_height-50)
score = 0
# init_velocity = 3
if score <= 100:
    init_velocity = 5
elif score <= 200:
    init_velocity = 10
elif score <= 300:
    init_velocity = 15
elif score <= 400:
    init_velocity = 20
elif score <= 500:
    init_velocity = 25
fps = 60
snk_list = []
snk_length = 1

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size] )
    
    
    
#creating a game loop
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
                
            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0
                
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0
                
            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0
           
    snake_x += velocity_x
    snake_y += velocity_y  
    
    if abs(snake_x - food_x) < 10  and abs(snake_y - food_y) < 10:
        score += 1 
        food_x = random.randint(20, screen_witdh-50)
        food_y = random.randint(20, screen_height-50) 
        snk_length += 5
                
    gameWindow.fill(black)
    text_screen("Score: "+ str(score * 10), red, 5, 5)
    # text_screen("Press up or down key to start", red, 310, 250)
    pygame.draw.rect(gameWindow,green, [food_x, food_y, snake_size, snake_size] )
    
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    
    if len(snk_list) > snk_length:
        del snk_list[0]
    
    # pygame.draw.rect(gameWindow,red, [snake_x, snake_y, snake_size, snake_size] )
    plot_snake(gameWindow, red, snk_list, snake_size)
    
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
