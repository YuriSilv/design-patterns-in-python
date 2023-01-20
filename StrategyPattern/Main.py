from Characters import MainChar
from Jumps import DoubleJump, SimpleJump

SimpleChar = MainChar.Create(SimpleJump.Jump(), 10, 10)
SimpleChar.jump()

SpecialChar = MainChar.Create(DoubleJump.Jump(), 50, 50)
SpecialChar.jump()