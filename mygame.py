import pygame
import math

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

        pygame.display.set_caption('sdgf')

    def run(self):
        run = True

        def check_keys(mdir, mspeed):
            pk = pygame.key.get_pressed()
            if pk[pygame.K_LEFT]:
                mdir = mdir - mspeed
            if pk[pygame.K_RIGHT]:
                mdir = mdir + mspeed
            # if pk[pygame.K_UP]:
            #     my = my - mspeed
            # if pk[pygame.K_DOWN]:
            #     my = my + mspeed
            return mdir

        direction = 0 - math.pi
        center = (150, 150)
        radius = 100
        # x = 20
        # y = 40
        # w = 60
        # h = 80
        speed = math.pi/60

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.time.delay(10)

            direction = check_keys(direction, speed)

            self.win.fill((0,0,0))
            # pygame.draw.rect(self.win, (100, 50, 200), (x, y, w, h))
            pygame.draw.circle(self.win, self.color['blue'], center, radius, 10)
            x_pos = math.cos(direction) * 100 + 150
            y_pos = math.sin(direction) * 50 + 150
            end_pos = (x_pos, y_pos)
            pygame.draw.aaline(self.win, self.color['red'], center, end_pos)

            pygame.display.flip()

        pygame.quit()



game = Game()
game.run()

print('aken sulgus')


#
#
