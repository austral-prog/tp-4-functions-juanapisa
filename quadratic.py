# Replace the "ANSWER HERE" for your answer
from idlelib.replace import replace

def roots(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
    raiz1 = str(r1)
    raiz2 = str(r2)
    discriminante = b ** 2 - 4 * a * c
    if discriminante > 0:
        return f"({r1}, {r2})"
    elif raiz1 == raiz2:
        return f"({r1})"
    else:
        return f"( )"

def value_y(a, b, c, x):
    formula = a * x ** 2 + b * x + c
    return formula

def to_string(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0 and b == 0:
        return f"f(x) = {c}"
    elif b == 0 and c == 0:
        return f"f(x) = {a} * X^2"
    elif c == 0 and a == 0:
        return f"f(x) = {b} * X"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a < 0 or b < 0 or c < 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    if a > 0 and b > 0:
        return f"f'(x) = {a*2} * X + {b}"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {a * 2} * X"
    elif b < 0:
        return f"f'(x) = {a*2} * X + {b}"




