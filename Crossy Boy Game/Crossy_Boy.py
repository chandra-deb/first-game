import pygame #importing pygame library
TITLE = 'Crossy Boy' #screen title
WIDTH = 800 #screen size
HEIGHT = 700 #screen size
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)
BLUE_COLOR = (0,0,255)
clock = pygame.time.Clock() #this clock is for selecting frames per second (FPS)
pygame.font.init()
font = pygame.font.SysFont('comicsans',60)


class Game:
    tick_rate = 60 #refresh 60 frames per second

    def __init__(self,background_image,title,width,height):
        self.title = title
        self.width = width
        self.height = height
        
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((width,height))
        self.screen.fill(WHITE_COLOR)
        image = pygame.image.load(background_image)
        self.background_image = pygame.transform.scale(image,(width,height))
  
        
    def run_game_loop(self,level_speed):
        is_game_over = False
        direction = 0
        did_win = False

        player_character = PlayerCharacter('player.png',375,650,50,50)
        enemy_1 = EnemyCharacter('enemy 0.png',20,550,50,50)
        enemy_1.SPEED *= level_speed
        enemy_2 = EnemyCharacter('enemy 0.png',self.width - 40,400,50,50)
        enemy_2.SPEED *= level_speed
        enemy_3 = EnemyCharacter('enemy 1.png',20,200,50,50)
        enemy_3.SPEED *= level_speed
        treasure = GameObject('treasure.png',375,50,50,50)

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)
            self.screen.fill(WHITE_COLOR)
            self.screen.blit(self.background_image,(0,0))
            player_character.move(direction,self.height)
            player_character.draw(self.screen)
            treasure.draw(self.screen)
            if player_character.collision_detector(enemy_1) or player_character.collision_detector(enemy_2) or player_character.collision_detector(enemy_3):
                is_game_over = True
                did_win = False
                text = font.render('You lose :(',True,BLACK_COLOR)
                self.screen.blit(text,(300,250))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.collision_detector(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You win :)',True,BLACK_COLOR)
                self.screen.blit(text,(300,250))
                pygame.display.update()
                clock.tick(1)
                break
            enemy_1.move(self.width)
            enemy_1.draw(self.screen)
            pygame.display.update()

            if level_speed > 2:
                enemy_2.move(self.width)
                enemy_2.draw(self.screen)
            if level_speed > 4:
                enemy_3.move(self.width)
                enemy_3.draw(self.screen)
                
            pygame.display.update()
            clock.tick(self.tick_rate)
        if did_win == True:
            self.run_game_loop(level_speed + 0.5)
        else:
            return
# generic behavior for every object
class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # Scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))
        
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self,background):
        background.blit(self.image,(self.x_pos,self.y_pos))


class PlayerCharacter(GameObject):

    SPEED = 5
    
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path, x, y, width, height)

    def move(self,direction,max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50

    def collision_detector(self,other_body):
        if self.y_pos > other_body.y_pos + other_body.height - 10:
            return False
        elif self.y_pos + self.height - 10 < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        return True
            
            

class EnemyCharacter(GameObject):

    SPEED = 4
    
    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path, x, y, width, height)

    def move(self,max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 20:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED
        
    
pygame.init()

new_game = Game('background.png',TITLE,WIDTH,HEIGHT)
new_game.run_game_loop(1)
#objects.draw('player.png')
#initialize all pygame library function

##player_image = 
## player_image = 

##game_over = False
##while not game_over:
##    for event in pygame.event.get():
##        if event == pygame.QUIT():
##            game_over = True
##        print(event)

 # pygame.draw.rect(screen,black_color,[350,350,100,100])
           # pygame.draw.circle(screen,blue_color,(400,200),80)
            #screen.blit(player_image,(375,375))
##            
pygame.quit()
quit()


