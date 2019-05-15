def omega(T):
    '''Return periodic time as angular frequency.'''
    import numpy as np
    return 2 * np.pi / T


def t(x, y):
    '''Calculate t. The smaller t, the better. Optimal values are t < 2.'''
    import numpy as np
    return abs(x.n - y.n) / np.sqrt(x.s ** 2 + y.s ** 2)


def s_t(t, n):
    '''Uncertainty for time for certain devices. Apparently.'''
    import numpy as np
    return (sum(t) / len(t)) / np.sqrt(n)


def wmean(x, ux):
    '''Weighted mean. Stolen from Erik's helpers_2.py'''
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
        of your uncertainties uarray"""

    values = []
    errors = []
    for i in range(len(x)):
        values.append(x[i].nominal_value)
        errors.append(x[i].std_dev)
    values = np.asarray(values)
    errors = np.asarray(errors)
    return values, errors


def txttoarr(fname, offset=0, *kwargs):
    '''What used to be me csvreader, but Erik changed to disregard empty items.'''
    import numpy as np
    with open(fname, 'r') as myfile:
        data = myfile.read().replace(',', '.').replace('\n', ',').replace('  ', ',').replace("\t", ",")
    datarray = data.split(',')
    output = []
    for item in datarray:
        if item != '':
            output.append((item))
    internal = []
    for item in output[offset:]:
        internal.append(float(item))
    output = np.array(internal)
    x = output[0::2]
    y = output[1::2]
    return [x, y]


def findpositive(x, y):
    '''Finds all positive values of y and gives you only the corresponding x and y values as lists.'''
    i = 0
    x_ = []
    y_ = []
    while y[i] >= 0:
        x_.append(x[i])
        y_.append(y[i])
        i += 1
    return x_, y_


def findnegative(x, y):
    '''Finds all negative values of y and gives you only the corresponding x and y values as lists.'''
    i = 0
    x_ = []
    y_ = []
    while y[i] < 0:
        x_.append(x[i])
        y_.append(y[i])
        i += 1
    return x_, y_
