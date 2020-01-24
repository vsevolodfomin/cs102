import pygame
from pygame.locals import *
import   math
from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int=10, speed: int=10) -> None:
        super().__init__(life)
        self.speed = speed
        self.cell_size = cell_size

        self.life = life

        self.screen_size =  self.life.rows * cell_size, self.life.cols * cell_size
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        # Copy from previous assignment
        for x in range(0, self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.cell_size))
        for y in range(0, self.cell_size, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.cell_size, y))

    def draw_grid(self) -> None:
        # Copy from previous assignment
        for i in range(self.cell_size):
            for j in range(self.cell_size):
                if self.screen[i][j] == 0:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                    pygame.Rect(x, y, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                                    pygame.Rect(x, y, self.cell_size, self.cell_size))

    def run(self) -> None:
        # Copy from previous assignment
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.create_grid(True)

        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if pause == False:
                            pause = True
                        else:
                            pause = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        row = math.floor(x/self.cell_size)
                        col = math.floor(y/self.cell_size)
                        self.life.curr_generation[col][row] = 1 if self.life.curr_generation[col][row] == 0 else 0
                        self.draw_grid()


            if not self.life.is_changing and self.life.randomize == True:
                running = False

            if not pause:
                self.draw_lines()

            self.life.step()
            if self.life.generations > self.life.max_generations:
                break
            self.draw_grid()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()