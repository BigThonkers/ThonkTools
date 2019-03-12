def excelrep(x, pmaxi=10, nmaxi=10, cdot=False):
    """
    Excel tractor
    Convert Excel's notation to LaTeX.

    :param x: Excel output as string
    :param pmaxi: Max positive value
    :param nmaxi: Max negative value
    :param cdot: Whether to use \times or \cdot
    :return: "10^{1}"
    """
    if pmaxi or nmaxi > 99:
        raise ValueError("Power limit reached.")
    if cdot == False:
        for i in pmaxi:
            if i < 10:
                x.replace("E+0{0}".format(i), "\times10^{0}".format(i))
            else:
                x.replace("E+{0}".format(i), "\times10^{0}".format(i))
        for i in nmaxi:
            if i < 10:
                x.replace("E+0{0}".format(i), "\times10^{0}".format(i))
            else:
                x.replace("E+{0}".format(i), "\times10^{0}".format(i))
    else:
        for i in pmaxi:
            if i < 10:
                x.replace("E+0{0}".format(i), "\cdot10^{0}".format(i))
            else:
                x.replace("E+{0}".format(i), "\cdot10^{0}".format(i))
        for i in nmaxi:
            if i < 10:
                x.replace("E+0{0}".format(i), "\cdot10^{0}".format(i))
            else:
                x.replace("E+{0}".format(i), "\cdot10^{0}".format(i))
    return x
