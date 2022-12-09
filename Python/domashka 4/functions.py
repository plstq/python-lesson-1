import sympy
from random import randint as rnd 

def create_polinom(k: int, simple: bool = True) -> str:
    polinom = ''
    for i in range(k, -1, -1):
        polinom += f'{rnd(0,2)}*x**{i}+'
        if i == 0:
            polinom += f'{rnd(0,100)}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)

def create_pol_file(polinom: str, filename: str = 'new'):
    with open (f'domashka 4/{filename}.txt', 'w') as f: #не знаю что у Вас написано в sem4, поэтому у меня не работает код :(
        f.write(polinom)