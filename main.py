import pygame
import random
pygame.init()

#defining colors
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# creating window 
screen_witdh = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_witdh, screen_height))
# game title
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size] )
        
def welcome():
    quit_game = False
    while not quit_game:
        gameWindow.fill(black)
        text_screen("Welcome to My First Game", white, 320, 270)
        text_screen("Press Space to Play", white, 360, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        
        pygame.display.update()
        clock.tick(60)
    
#creating a game loop
def gameloop(): 
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
    init_velocity = 4
    fps = 60
    snk_list = []
    snk_length = 1
    
    with open("highscore.txt", "r") as file:
        highscore = file.read()
    
    while not quit_game:
        if game_over:
            gameWindow.fill(black)
            with open("highscore.txt", "w") as file:
                file.write(str(highscore))
            
            text_screen("Game Over! Press Enter/Return to continue", red, 250, 300)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            
        else:   
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
                    
                    #cheat code (Q)
                    if event.key == pygame.K_q:
                        score += 20
                
            snake_x += velocity_x
            snake_y += velocity_y  
            
            if abs(snake_x - food_x) < 10  and abs(snake_y - food_y) < 10:
                score += 10 
                food_x = random.randint(20, screen_witdh-50)
                food_y = random.randint(20, screen_height-50) 
                snk_length += 5
                
                if score > int(highscore):
                    highscore = score
                        
            gameWindow.fill(black)
            text_screen("Score: "+ str(score) + "   Highscore: "+str(highscore), green, 5, 5)
            pygame.draw.rect(gameWindow,green, [food_x, food_y, snake_size, snake_size] )
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list) > snk_length:
                del snk_list[0]
                
            if head in snk_list[:-1]:
                game_over = True
                
            if snake_x < 0 or snake_x > screen_witdh or snake_y < 0 or snake_y > screen_height:
                game_over = True
   
            plot_snake(gameWindow, red, snk_list, snake_size)
            
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
    
if __name__ == '__main__':
    welcome()