'''
Return periodic time as angular frequency.
'''


def omega(T):
    import numpy as np
    return 2 * np.pi / T


'''
Calculate linear regression for polynomial a*x+b
'''


def b(x, y):
    n = len(x)
    return (sum(x ** 2) * sum(y) - sum(x) * sum(x * y)) / (n * sum(x ** 2) - (sum(x)) ** 2)


def a(x, y):
    n = len(x)
    return (n * sum(x * y) - sum(x) * sum(y)) / (n * sum(x ** 2) - (sum(x)) ** 2)


'''
Calculate uncertainties for the above functions
'''


def s(x, y):
    n = len(x)
    import numpy as np
    return np.sqrt((1 / (n - 2) * sum((y - b(x, y) - a(x, y) * x) ** 2)))


def Db(x, y):
    n = len(x)
    import numpy as np
    return s(x, y) * np.sqrt(sum(x ** 2) / (n * sum(x ** 2) - (sum(x)) ** 2))


def Da(x, y):
    n = len(x)
    import numpy as np
    return s(x, y) * np.sqrt(n / (n * sum(x ** 2) - (sum(x)) ** 2))


'''
Calculate t. The smaller t, the better. Optimal values are t < 2.
'''


def t(x, y):
    import numpy as np
    return abs(x.n - y.n) / np.sqrt(x.s ** 2 + y.s ** 2)


'''
Uncertainty for time for certain devices. Apparently.
'''


def s_t(t, n):
    import numpy as np
    return (sum(t) / len(t)) / np.sqrt(n)


'''
Weighted mean. Stolen from Erik's helpers_2.py
'''


def wmean(x, ux):
    if len(x) != len(ux):
        raise ValueError("Nominal value and uncertainties must be of same length.")
    else:
        g = []
        for i in range(len(ux)):
            g.append(1 / (ux[i] ** 2))
        g = np.array(g)
        x = np.array(x)
        xg = sum(g * x) / sum(g)
        uxg = 1 / sqrt(sum(g))
        return xg, uxg


def uarraysplit(x):
    """takes an uncertainties uarray and returns the
    tuple (values, errors)
    -values: a numpy array that contains all the values
        of your uncertainties uarray
    -errors: a numpy array that contains all the errors
        of your uncertainties uarray
    """

    values = []
    errors = []
    for i in range(len(x)):
        values.append(x[i].nominal_value)
        errors.append(x[i].std_dev)
    values = np.asarray(values)
    errors = np.asarray(errors)
    return values, errors
