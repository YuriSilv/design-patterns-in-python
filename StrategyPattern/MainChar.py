import Character
import Strategy as Strategy

class MainChar(Character):
    def __init__(self, strategy_jump: Strategy, speed, health):
        super.__init__(strategy_jump, speed, health)

    def jump(self):
        Character.jump()