import cmath
from random import randint

pi = 3.1415926
e = 2.718281


def f2bin(f):
    if not cmath.isfinite(f):
        return repr(f)
    sign = '-' * (copysign(1.0, f) < 0)
    frac, fint = modf(fabs(f))
    n, d = frac.as_integer_ratio()
    assert d & (d - 1) == 0
    return f'{sign}{floor(fint):b}.{n:0{d.bit_length()-1}b}'


def fbin2dec(n):
    n1 = int(str(n)[:str(n).find('.')], 2)
    n2 = 0
    ind = 1
    for i in str(n)[str(n).find('.')+1:]:
        n2 += int(i) * (0.5 ** ind)
        ind += 1
    return n1 + n2


def ceil(x):
    return int(x)+1


def floor(x):
    return int(x)


def degrees(x):
    return x * 180 / pi


def radians(x):
    return x * pi / 180


def fabs(x):
    return x if x > 0 else -x


def fmod(x, y):
    return x % y


def modf(x):
    return (float('0.'+str(x)[str(x).find('.')+1:]), float(str(x)[:str(x).find('.')])) \
        if '.' in str(x) else (float(x), 0.0)


def hypot(x, y):
    return sqrt(x**2 + y**2)


def sqrt(x, y=2):
    return x ** (1/y)


def atan2(x, y):
    return radians(cmath.atan(x/y))


def frexp(x):
    a = f2bin(float(x))
    if (a[0] + a[1]) == '0.':
        a = a.replace('0.', '')
        a = a[::-1]
        a = '0.' + a
    else:
        a = a[::-1]
        if not (a[0] + a[1]) == '0.':
            a = a.replace('.', '')
            a = '0.' + a
    return fbin2dec(a), len(a[a.find('.')+1:])


def ldexp(x, y):
    return x * (2 ** y)


def copysign(x, y):
    return (-1 if '-' in str(y) else 1) * fabs(x)


def rand(_min, _max):
    return randint(_min, _max)
