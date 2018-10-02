
'''
Return periodic time as angular frequency.
'''
def omega(T):
	import numpy as np
	return 2*np.pi/T

'''
Calculate linear regression for polynomial a*x+b
'''
def a(x,y):
	n=len(x)
	return (sum(x**2)*sum(y)-sum(x)*sum(x*y))/(n*sum(x**2)-(sum(x))**2)

def b(x,y):
	n=len(x)
	return (n*sum(x*y)-sum(x)*sum(y))/(n*sum(x**2)-(sum(x))**2)

'''
Calculate uncertainties for the above functions
'''
def s(x,y):
	n=len(x)
	import numpy as np
	return np.sqrt((1/(n-2))*sum((y-a(x,y)-b(x,y)*x)**2))

def Da(x,y):
	n=len(x)
	import numpy as np
	return s(x,y)*np.sqrt(sum(x**2)/(n*sum(x**2)-(sum(x))**2))

def Db(x,y):
	n=len(x)
	import numpy as np
	return s(x,y)*np.sqrt(n/(n*sum(x**2)-(sum(x))**2))
	
'''
Calculate t. The smaller t, the better. Optimal values are t < 2.
'''
def t(x,y):
	import numpy as np
	return abs(x.n-y.n)/np.sqrt(x.s**2+y.s**2)
	
'''
Uncertainty for time for certain devices. Apparently.
'''
def s_t(t,n):
	import numpy as np
	return (sum(t)/len(t))/np.sqrt(n)
	
'''
Import lots of stuff.
'''
def impfunc():
	from uncertainties import ufloat
	from uncertainties import unumpy as unp
	import numpy as np
	import matplotlib.pyplot as plt
	from scipy.optimize import curve_fit
	import pandas as pd
	return