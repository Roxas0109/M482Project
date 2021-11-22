import numpy as np

def p1(n):
    return int(1+(np.floor(n * 17*np.power(np.pi, 6)) % 31))

def p2(n):
    return int(1+(np.floor(n * 17*np.power(np.e, 6)) % 31))

def p3(n):
    return int(1+(np.floor(n * 17*np.power(np.e, 8)) % 31))

def p4(n):
    return int(1+(np.floor(n * 11*np.power(np.e, 8)) % 31))

def p5(n):
    return int(1+(np.floor(n * 101*np.power(np.e, 2)) % 31))

def p6(n):
    return int(1+(np.floor(n * 101*np.power(np.e, 8)) % 31))
