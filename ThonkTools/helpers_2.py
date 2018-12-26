# -*- coding: utf-8 -*-
"""
Functions to help with Physics Lab. Some of them Require numpy.
@author: erik_
"""

%pylab inline

def LRoG(list:xx, list:yy)-> list:
    """Linear Regression, unweighted"""
    n = len(xx)
    x = np.array(xx)
    y = np.array(yy)
    x2 = x**2
    y2 = y**2
    xy = y * x
    xsum = sum(x)
    ysum = sum(y)
    x2sum = sum(x2)
    y2sum = sum(y2)
    xysum = sum(xy)
    a = (x2sum * ysum - xsum * xysum) / (n * x2sum - xsum**2)
    b = (n * xysum - xsum * ysum) / (n * x2sum - xsum**2)
    xyab = (y - (a + (b * x)))**2
    ssum = sum(xyab)
    s = sqrt(np.abs((1 / (n - 2)) * ssum))
    ub = s * sqrt(np.abs((n) / (n * x2sum - (xsum**2))))
    ua = s * sqrt(np.abs((x2sum / (n * x2sum - xsum**2))))
    return a,b,ua,ub

def LRmG(list:x, list:y, list:u)-> list:
    """Linear Regression, weighted.
    
    """
    try:
        u[0]
        if (len(x)!=len(y)):
            raise LenError
        if (len(x)!=len(u)):
            raise LenError
        x = array(x)
        y = array(y)
        u = array(u)
        g = []
        for i in range(len(y)):
            g.append(1/u[i]**2)
            
        a = (sum(g*(x**2))*sum(g*y)-sum(g*x)*sum(g*x*y))/(sum(g)*sum(g*(x**2))-(sum(g*x)**2))
             
        b = (sum(g)*sum(g*x*y)-sum(g*x)*sum(g*y))/(sum(g)*sum(g*x**2)-sum(g*x)**2)
        
        ua = sqrt(sum(g*x**2)/(sum(g)*sum(g*x**2)-sum(g*x)**2))
        
        ub = sqrt(sum(g)/(sum(g)*sum(g*x**2)-sum(g*x)**2))
        
        return a,b,ua,ub
        
    except TypeError:
        return LRmG(x,y,ones(len(y))*u)
    

def meanDeviation(list:x):
    """Computes the mean deviation of a given list."""
    m = mean(x)
    return sqrt((1/(len(x)-1))*sum((x-m)**2))/sqrt(len(x))

def gewMitt(list:x, list:ux):
    """returns the weighted mean. Input are two lists of equal lengh:
            the Values and the uncertainties """
    if len(x)!=len(ux):
        print("u fucked x, ux up")
    g = []
    for i in range(len(ux)):
        g.append(1/(ux[i]**2))
    g = np.array(g)
    x = np.array(x)
    xg = sum(g*x)/sum(g)
    uxg = 1/sqrt(sum(g))
    return xg, uxg

def vertrag(x,ux,y):
    """determines, whether your value is compatible with a given value"""
    return abs(x-y)/ux

def vergl(x,ux,y, uy):
    """determines, whether two values are compativle"""
    return abs(x-y)/sqrt(ux**2 +uy**2)

def line(x,a,b):
    """helper to plot a line"""
    return (a) + multiply((b),(x))

def drawLine(x,list:a):
    """helper to plot a line from a list"""
    return line(x,a[0],a[1])

def lineinfo(list:a,e=5,r=5):
    """returns the params of a Lineplot (listform)"""
    print("{0}\t{1}\t{2}\t{3}".format(round(a[0],e), round(a[1], e), round(a[2],r),round(a[3],r)))

def iround(a):
    """rounds physically"""
    for i in range(10):
        intern = round(a,i)
        intern2 = round(a,i+1)
        if (1<=(abs(intern2)*10**(i))<=2):
            return round(a,(i+1))
        if (abs(intern)*10**(i)) >= 2:
            return round(a,i)
