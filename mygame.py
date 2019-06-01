import pygame

class Game:
    def __init__(self):
        self.width = 600
        self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('sdgf')

    def run(self):
        run = True

        def check_keys(mx, my, mspeed):
            pk = pygame.key.get_pressed()
            if pk[pygame.K_LEFT]:
                mx = mx - mspeed
            if pk[pygame.K_RIGHT]:
                mx = mx + mspeed
            if pk[pygame.K_UP]:
                my = my - mspeed
            if pk[pygame.K_DOWN]:
                my = my + mspeed
            return (mx, my)

        x = 20
        y = 40
        w = 60
        h = 80
        speed = 5

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.time.delay(10)


            (x, y) = check_keys(x, y, speed)

            self.win.fill((0,0,0))
            pygame.draw.rect(self.win, (100, 50, 200), (x, y, w, h))

            pygame.display.flip()

        pygame.quit()



game = Game()
game.run()

print('aken sulgus')


#
#
