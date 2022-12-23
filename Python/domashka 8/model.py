import sympy

def execute_expr(expr: str) -> str: 
    """Принимает на вход строку-пример. Возвращает результат примера"""
    return str(eval(expr))

def solve_eq(expr: str) -> str:
    
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    try:
        x = sympy.Symbol('x')
        res = sympy.solve(expr, x)
        res = list(map(str, res))
        return " || ".join(res)
    except ValueError:
        return 'Incorrect input'

def simpify_pol(expr: str) -> str:
    """Упрощает выделенный многочлен"""
    return str(sympy.simplify(expr))
