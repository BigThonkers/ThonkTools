def excelrep(x, pmaxi=10, nmaxi=10):
    if pmaxi or nmaxi > 99:
        raise ValueError("Power limit reached.")
    for i in pmaxi;
    if i < 10:
        x.replace("E+0{0}".format(i), "\times10^{0}".format(i))
    else:
        x.replace("E+{0}".format(i), "\times10^{0}".format(i))
    for i in nmaxi;
    if i < 10:
        x.replace("E+0{0}".format(i), "\times10^{0}".format(i))
    else:
        x.replace("E+{0}".format(i), "\times10^{0}".format(i))
    return x
