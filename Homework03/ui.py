import abc

from abc import abstractmethod

from life import GameOfLife


class UI(abc.ABC):

    def __init__(self, life: GameOfLife) -> None:
        self.life = life

    @abstractmethod
    def run(self) -> None:
        pass