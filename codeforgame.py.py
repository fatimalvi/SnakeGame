import pygame
import sys  # system
import os
import random


class Hebi():
    def __init__(self):
        self.length = 1
        self.position = [(screen_height/2, screen_width/2)]  # middle
        self.direction = left  # initial
        self.score = 0

    def resetgame(self):
        FileDir = os.path.dirname(os.path.abspath(__file__))
        end_screen = os.path.join(FileDir, "e2.jpg")
        end = pygame.image.load(end_screen)
        surface.fill((255, 255, 255))
        surface.blit(end, [70, 0])
        pygame.display.flip()
        end_music = os.path.join(FileDir, "omae.mp3")
        pygame.mixer.music.load(end_music)
        pygame.mixer.music.play(-1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()

    def head(self):
        return self.position[0]

    def keymovemnet(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.turning(down)
                elif event.key == pygame.K_RIGHT:
                    self.turning(right)
                elif event.key == pygame.K_UP:
                    self.turning(up)
                elif event.key == pygame.K_LEFT:
                    self.turning(left)

    def drawhebi(self, surface):
        for section in self.position:  # x y width height
            r = pygame.Rect((section[0], section[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, ((34, 67, 89)), r,
                             4)  # where colour area fill

    def turning(self, coordinate):
        if self.length > 1 and (coordinate[0]*-1, coordinate[1]*-1) == self.direction:
            return
        else:
            self.direction = coordinate

    def movement(self):
        current = self.head()
        x, y = self.direction
        new = (((current[0]+(x*gridsize)) % screen_width),
               (current[1]+(y*gridsize)) % screen_height)
        if len(self.position) > 2 and new in self.position[2:]:
            self.resetgame()
        else:
            self.position.insert(0, new)
            if len(self.position) > self.length:
                self.position.pop()


class foodforhebi():
    def __init__(self):
        self.position = (0, 0)
        self.color = ((0, 255, 0))
        self.random_food()

    def random_food(self):
        self.position = (random.randint(0, grid_width-1)*gridsize,
                         random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect(
            (self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, ((255, 255, 255)), r)


def basecolour(surface):
    surface.fill((156, 218, 255))


# the variables

screen_width = 480
screen_height = 480  # dimensions
gridsize = 30
grid_width = int(screen_width/gridsize)
grid_height = int(screen_height/gridsize)
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)


def main():
    pygame.init()  # initialization
    global surface
    surface = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    FileDir = os.path.dirname(os.path.abspath(__file__))

    #caption and icon
    pygame.display.set_caption("Hebi the snake game")
    icon_image = os.path.join(FileDir, "hebi.jpg")
    s_icon = pygame.image.load(icon_image)
    pygame.display.set_icon(s_icon)  # for the icon

    # start image
    cover_image = os.path.join(FileDir, "c2.jpg")
    cover = pygame.image.load(cover_image)
    surface.fill((255, 255, 255))
    surface.blit(cover, [70, 0])
    pygame.display.flip()

    # bm music
    bm_music = os.path.join(FileDir, "mario.mp3")
    pygame.mixer.music.load(bm_music)
    pygame.mixer.music.play(-1)
    surface.fill((255, 255, 255))
    surface.blit(cover, [70, 0])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    hebi = Hebi()
                    food = foodforhebi()
                    basecolour(surface)
                    score_record = pygame.font.SysFont("monospace", 18)

                    while True:
                        clock.tick(10)
                        hebi.keymovemnet()
                        basecolour(surface)
                        hebi.movement()
                        if hebi.head() == food.position:
                            hebi.length += 1
                            hebi.score += 1
                            food.random_food()
                        hebi.drawhebi(surface)
                        food.draw(surface)
                        surface.blit(surface, (0, 0))
                        text = score_record.render(
                            "Food eaten {0}".format(hebi.score), False, (0, 0, 0))
                        surface.blit(text, (5, 10))

                        pygame.display.update()


main()
