

from random import randint, uniform
import re


def gera_lancamentos():
    lancamentos = []

    for i in range(0, 100):  
        random = (randint(1, 6))
        lancamentos.append(str(random))
    return lancamentos

print(gera_lancamentos())