import pygame
import math
from Enemy import Enemy

class Game:
    def __init__(self):
        self.width = 600
        self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = {
            'white': (255, 255, 255),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
            'red': (255, 0, 0)
        }
        self.direction = 0 - math.pi
        self.center = (200, 150)
        self.radius = 160
        self.speed = math.pi/60

        self.enemy = Enemy(self.win)

        pygame.display.set_caption('sdgf')

    def run(self):
        run = True

        def check_keys():
            pk = pygame.key.get_pressed()

            if pk[pygame.K_LEFT]:
                self.center = (self.center[0] - 1, self.center[1])

            if pk[pygame.K_RIGHT]:
                self.center = (self.center[0] + 1, self.center[1])

            if pk[pygame.K_DOWN]:
                self.center = (self.center[0], self.center[1]+1)

            if pk[pygame.K_UP]:
                self.center = (self.center[0], self.center[1]-1)

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_ESCAPE:
                        run = False

            pygame.time.delay(100)

            # seier tiirleb
            self.direction = self.direction + self.speed
            # kontrollib vajautatud nuppe
            check_keys()

            # ekraan puhtaks
            self.win.fill((0,0,0))


            # koll rändab
            self.enemy.move()
            self.enemy.draw()

            # pygame.draw.rect(self.win, (100, 50, 200), (x, y, w, h))
            pygame.draw.circle(self.win, self.color['blue'], self.center, self.radius, 1)
            # siin arvutatakse joone otsakoordinaadid
            x_pos = math.cos(self.direction) * self.radius + self.center[0]
            y_pos = math.sin(self.direction) * self.radius/2 + self.center[1]
            end_pos = (x_pos, y_pos)
            pygame.draw.aaline(self.win, self.color['red'], self.center, end_pos)

            pygame.display.flip()

        pygame.quit()



game = Game()
game.run()

print('aken sulgus')


#
#
