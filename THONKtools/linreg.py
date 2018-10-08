def linreg(xarr,yarr,markeraus='-',grenz=True,markergrenz='--',color='orange',labelaus='Lineare Regression',labelgrenz=None,unumpy=False,first=0,last=-1,xnum=100,xfitrestrictl=None,xfitrestrictr=None,yfitrestrictl=None,yfitrestrictr=None,subplot=None):
    def fitfunc(x,a,b):
        return a*x+b
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    if unumpy == True:
        from uncertainties import unumpy as unp
        xfit=np.linspace(unp.nominal_values(xarr)[first],unp.nominal_values(xarr)[last],xnum)
        popt,pcov=curve_fit(fitfunc,unp.nominal_values(xarr)[xfitrestrictl:xfitrestrictr],unp.nominal_values(yarr)[yfitrestrictl:yfitrestrictr])
    else:
        xfit=np.linspace(xarr[first],xarr[last],xnum)
        popt,pcov=curve_fit(fitfunc,xarr[xfitrestrictl:xfitrestrictr],yarr[yfitrestrictl:yfitrestrictr])
    a,b=popt
    fit=a*xfit+b
    c=np.sqrt(np.diag(pcov))[0]
    d=np.sqrt(np.diag(pcov))[1]
    dfit1=(a+c)*(xfit)+(b-d)
    dfit2=(a-c)*(xfit)+(b+d)
    if subplot==None:
        plt.plot(xfit,fit,markeraus,color=color,label=labelaus)
    else:
        subplot.plot(xfit,fit,markeraus,color=color,label=labelaus)
    if grenz==True:
        if subplot==None:
            plt.plot(xfit,dfit1,markergrenz,color=color,label=labelgrenz)
            plt.plot(xfit,dfit2,markergrenz,color=color,label=labelgrenz)
        else:
            subplot.plot(xfit,dfit1,markergrenz,color=color,label=labelgrenz)
            subplot.plot(xfit,dfit2,markergrenz,color=color,label=labelgrenz)
    return a,b,c,d=[a,b,c,d]
