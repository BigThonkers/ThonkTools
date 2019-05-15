def linreg(xarr, yarr, markeraus='-', grenz=True, markergrenz='--', color='orange', labelaus='Linear Regression',
           labelgrenz=None, unumpy=False, first=0, last=-1, xnum=2, xfitrestrictl=None, xfitrestrictr=None,
           yfitrestrictl=None, yfitrestrictr=None, subplot=None, method=None):
    '''Performs linear regression via curve_fit.

    Params:
    xarr and yarr are the input arrays. By default, these are parsed as lists.
    If unumpy is set to True, unp.nominal_values will be used.

    markeraus sets the marker used for the linear regression.

    grenz sets whether or not Grenzgeraden (I can't figure out the English term) should be used.

    markergrenz sets the marker used for the Grenzgeraden.

    color sets the color used by both the Grenzgeraden and the Ausgleichsgerade.

    labelaus and labelgrenz set the labels for the Ausgleichs- and Grenzgeraden.

    first and last set how much of the xarr should be used in the end.

    xnum sets the size of the array used for fitting.
    The default, 2, should suffice, since this is just a straight line.

    x/yfitrestrictl/r are restrictions for curve_fit.'''

    def fitfunc(x, a, b):
        return a * x + b

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    if unumpy == True:
        from uncertainties import unumpy as unp
        xfit = np.linspace(unp.nominal_values(xarr)[first], unp.nominal_values(xarr)[last], xnum)
        popt, pcov = curve_fit(fitfunc, unp.nominal_values(xarr)[xfitrestrictl:xfitrestrictr],
                               unp.nominal_values(yarr)[yfitrestrictl:yfitrestrictr], method=method)
    else:
        xfit = np.linspace(xarr[first], xarr[last], xnum)
        popt, pcov = curve_fit(fitfunc, xarr[xfitrestrictl:xfitrestrictr], yarr[yfitrestrictl:yfitrestrictr],
                               method=method)
    a, b = popt
    fit = a * xfit + b
    c = np.sqrt(np.diag(pcov))[0]
    d = np.sqrt(np.diag(pcov))[1]
    dfit1 = (a + c) * (xfit) + (b - d)
    dfit2 = (a - c) * (xfit) + (b + d)
    if subplot == None:
        plt.plot(xfit, fit, markeraus, color=color, label=labelaus)
    else:
        subplot.plot(xfit, fit, markeraus, color=color, label=labelaus)
    if grenz == True:
        if subplot == None:
            plt.plot(xfit, dfit1, markergrenz, color=color, label=labelgrenz)
            plt.plot(xfit, dfit2, markergrenz, color=color, label=labelgrenz)
        else:
            subplot.plot(xfit, dfit1, markergrenz, color=color, label=labelgrenz)
            subplot.plot(xfit, dfit2, markergrenz, color=color, label=labelgrenz)
    return


def b(x, y):
    '''Calculate linear regression for polynomial a*x+b'''
    n = len(x)
    return (sum(x ** 2) * sum(y) - sum(x) * sum(x * y)) / (n * sum(x ** 2) - (sum(x)) ** 2)


def a(x, y):
    n = len(x)
    return (n * sum(x * y) - sum(x) * sum(y)) / (n * sum(x ** 2) - (sum(x)) ** 2)


def s(x, y):
    '''Calculate uncertainties for linear regression of polynomial of a*x+b'''
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


def pltlinreg(x, y, xe, ye, label=None, color='darkorange', grenz=False):
    '''Plots the values with errorbars, linear regression, and outputs slope and intercept.
    I would add more parameters, but they're honestly mostly useless.'''
    import numpy as np
    import matplotlib.pyplot as plt
    plt.errorbar(x, y, xerr=xe, yerr=ye, fmt='x', label=r'{}'.format(label), color=color)
    linreg(x, y, method='lm', labelaus=r'Linear regression for {}'.format(label), color=color, grenz=grenz)
    print('Slope {}:'.format(label), a(x, y), '\pm', Da(x, y))
    print('Intercept {}:'.format(label), b(x, y), '\pm', Db(x, y))
    return
