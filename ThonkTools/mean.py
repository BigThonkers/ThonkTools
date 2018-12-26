def mean(arr):
	return sum(arr)/len(arr)

def wmean(arr,err):
	if err != None:
		return [sum(arr*err)/sum(err),1/sqrt(sum(err))]
	else:
		from uncertainties import ufloat
		return ufloat(sum(arr.n*arr.s)/sum(arr.s),1/sqrt(sum(arr.s)))

def meandev(arr,uncertainties=False):
    if uncertainties==True:
        arr=arr.nominal_values()
    m=mean(arr)
    return sqrt((1/(len(arr)-1))*sum((arr-m)**2))/sqrt(len(arr))

def nmean(arr,uncertainties=False):
    from uncertainties import ufloat
    if uncertainties==True:
        arr=arr.nominal_values()
    return ufloat(mean(arr),meandev(arr))
