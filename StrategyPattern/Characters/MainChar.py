from Characters import Character
from typing import Type
from Jumps import Strategy

class Create(Character.Character):
    def __init__(self, strategy_jump: Type[Strategy.Istrategy], speed, health):
        super().__init__(strategy_jump, speed, health)

    def jump(self):
        super().jump()