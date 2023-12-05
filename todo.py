import json
from functions import register, register_t, login
from main import User, Todo

f = False

e = int(input('Exit(0) / Enter todo (1): '))
if e == 1:
    f = register_t()
else:
    f = f