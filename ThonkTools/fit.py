def fit(x, y, func=lambda x: x, p0=None, r=None, d=None):
    """
        fit takes data points calculates the curve fit and gives back
        the values with which the curve can be plotted
        Parameters:
        -----------
        x: x-value of the data points.
        y: y-value of the data points.
        func: the function type the curve_fit will be applied to.
        r: determines the size of steps in which the x-achse intervall is split.
        d: tuple which determines the start and end point of the x-achse intervall on which the
            will be drawn. If not given the curve will be drawn between the largest and the smalest
            given x-value.
        Returns:
        -----------
        xnew: x-value with which the fitted curve can be plotted.
        ynew: y-value with which the fitted curve can be plotted.
    """
    import numpy as np
    from scipy.optimize import curve_fit
    popt, pvoc = curve_fit(func, x, y, p0=p0)
    params = popt.copy()
    if d == None:
        if r == None:
            xnew = np.arange(min(x), max(x), np.abs((max(x) - min(x)) / 100))
        else:
            xnew = np.arange(min(x), max(x), r)
    else:
        if r == None:
            xnew = np.arange(min(d), max(d), np.abs((max(x) - min(x)) / 100))
        else:
            xnew = np.arange(min(d), max(d), r)
    ynew = func(xnew, *params)
    return xnew, ynew


def expfit(x, y, p0=None, r=None, d=None):
    import numpy as np
    return fit(x, y, func=lambda x, a, b, c: a * np.exp(b * x) + c, r=r, d=d, p0=p0)


def linfit(x, y, p0=None, r=None, d=None):
    return fit(x, y, func=lambda x, a, b,: a * x + b, r=r, d=d, p0=p0)


def grfit(x, y, p0=None, r=None, d=None):
    import numpy as np
    return fit(x, y, func=lambda x, s, b, k: s - (s - b) * np.exp(-k * x), r=r, d=d, p0=p0)


def logfit(x, y, p0=None, r=None, d=None):
    import numpy as np
    return fit(x, y, func=lambda x, L, k, x_0: L / (1 + np.exp(-k * (x - x0))), r=r, d=d, p0=p0)


def gausfit(x, y, p0=None, r=None, d=None):
    import numpy as np
    return fit(x, y, func=lambda x, mu, sigma, B, A: A * np.e ** ((-1 * (x - mu) ** 2) / (2 * sigma ** 2)) + B, r=r,
               d=d, p0=p0)


def poisfit(x, y, p0=None, r=None, d=None):
    import numpy as np
    from math import factorial
    return fit(x, y, func=lambda x, mu: 1 / (factorial(x)) * mu ** x * np.exp(-mu)q, r=r, d=d, p0=p0)


def fit_pm(x, y, func=lambda x: x):
    """
        fit_pm takes data points and makes an exponential curve fit. It returns
        the parameters with errors and the coefficient of determination
        Parameters:
        -----------
        x: x-value of the data points.
        y: y-value of the data points.
        func: Function to be fitted to.
        Returns:
        -----------
        list: Gives back a list with the parameters of an expotential function the
              corresponding errors and the coefficient of determination.
    """
    from scipy.optimize import curve_fit
    from uncertainties import unumpy as unp
    import numpy as np
    popt, pcov = curve_fit(func, x, y)
    params = popt.copy()
    errors = np.sqrt(np.diag(pcov))
    r = np.array(y) - func(np.array(x), *params)
    rss = np.sum(r ** 2)
    tss = np.sum((y - np.mean(y)) ** 2)
    R_2 = 1 - (rss / tss)
    return unp.uarray(params, errors), R_2


def expfit_pm(x, y):
    import numpy as np
    return fit_pm(x, y, func=lambda x, a, b, c: a * np.exp(b * x) + c)


def linfit_pm(x, y):
    return fit_pm(x, y, func=lambda x, a, b,: a * x + b)


def grfit_pm(x, y):
    import numpy as np
    return fit_pm(x, y, func=lambda x, s, b, k: s - (s - b) * np.exp(-k * x))


def logfit_pm(x, y):
    import numpy as np
    return fit_pm(x, y, func=lambda x, L, k, x_0: L / (1 + np.exp(-k * (x - x0))))


def gausfit_pm(x, y):
    import numpy as np
    return fit_pm(x, y, func=lambda x, mu, sigma, B, A: A * np.e ** ((-1 * (x - mu) ** 2) / (2 * sigma ** 2)) + B)

def poisfit_pm(x, y):
    import numpy as np
    from math import factorial
    return fit_pm(x, y, func=lambda x, mu: 1 / (factorial(x)) * mu ** x * np.exp(-mu)q)
