import Strategy as Strategy

class Character():
    def __init__(self, strategy_jump: Strategy, speed, health):
        self.strategy_jump = strategy_jump
        self.speed = speed
        self.health = health

    def jump(self):
        Strategy.StrategyPattern.execute()

    def setStrategy(self, strategy_jump):
        self.strategy_jump = strategy_jump