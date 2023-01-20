from typing import Type
from Jumps import Strategy

class Character():
    def __init__(self, strategy_jump: Type[Strategy.Istrategy], speed, health):
        self.strategy_jump = strategy_jump
        self.speed = speed
        self.health = health

    def jump(self):
        self.strategy_jump.execute()

    def setStrategy(self, strategy_jump: Type[Strategy.Istrategy]):
        self.strategy_jump = strategy_jump