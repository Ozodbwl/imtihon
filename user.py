import json
from functions import register, login
from main import User, Todo
f = False

e = int(input('Sign up(0) / Sign in (1): '))
if e == 0:
    f = register()
else:
    f = login()
