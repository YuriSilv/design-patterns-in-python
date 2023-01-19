import MainChar as MainChar
import Strategy as Strategy
import DoubleJump as DoubleJump

Principal = MainChar(Strategy.execute(), 10, 10)
Principal.setStrategy(DoubleJump())
Principal.jump()