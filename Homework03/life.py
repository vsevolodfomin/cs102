import pathlib
import random

from typing import List, Optional, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool=True,
        max_generations: Optional[float]=float('inf')
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool=False) -> Grid:
        # Copy from previous assignment
        grid = [[0] * self.cols for j in range(self.rows)]

        if randomize == False:
            return grid
        else:
            row = 0
            for i in grid:
                col = 0
                for j in grid:
                    grid[row][col] = random.randint(0, 1)
                    col += 1
                row += 1
            return grid
        return grid 

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        grid = self.curr_generation
        list_of_neighbours = []
        row, col = cell
        for j in range(-1, 2):
            for i in range(-1, 2):
                if (0 <= row+j < self.rows) and (0 <= col+i < self.cols) and (i+j != i*j):
                    list_of_neighbours.append(grid[row+j][col+i])
        return list_of_neighbours

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        grid = self.curr_generation
        new_grid = []
        for row in range(len(grid)):
            new_grid.append([])
            for col in range(len(grid[row])):
                neighbours = self.get_neighbours((row, col)).count(1)
                if (grid[row][col] == 0) and (neighbours == 3):
                    new_grid[row].append(1)
                elif (grid[row][col] == 1) and (2 <= neighbours <= 3):
                    new_grid[row].append(1)
                else:
                    new_grid[row].append(0)
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.generations += 1
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        max_generations = self.max_generations
        if max_generations > self.generations:
            return False
        else:
            return True

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        previous_grid = self.prev_generation
        current_grid = self.curr_generation

        row = 0
        for i in previous_grid:
            col = 0
            for j in i:
                if j != current_grid[row][col]:
                    return True
                col += 1
            row += 1
        return False
            

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        grid = []

        with open(filename, 'r') as file:
            for i in file:
                grid.append(i[:-1])

        new_grid = list(map(list, grid))

        last_grid = []
        for i in new_grid:
            last_grid.append(list(map(int, i)))


        game_return = GameOfLife([len(last_grid[0]), len(last_grid)])
        game_return.curr_generation = last_grid

        return game_return

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        grid = self.curr_generation
        with open(filename, 'w') as file:
            for i in grid:
                for j in grid:
                        file.writelines()
  
