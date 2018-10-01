import numpy as np

def qeq(a, b, c):
    """
    Solve quadratic equation.
    """
    d = np.sqrt(b**2 - 4 * a * c)
    return ((-b + d) / (2 * a)), ((-b - d)/ (2 * a))

def qeq2(a, b, c):
    """
    Solve quadratic equation with less error.
    """
    d = np.sqrt(b**2 - 4 * a * c)
    alpha = (-b - np.sign(b) * d) / (2 * a)
    beta = c / (a * alpha)
    return alpha, beta
