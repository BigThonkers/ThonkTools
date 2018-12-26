def mean(arr):
	return sum(arr)/len(arr)

def wmean(arr,err):
	if err != None:
		return [sum(arr*err)/sum(err),1/sqrt(sum(err))]
	else:
		from uncertainties import ufloat
		return ufloat(sum(arr.n*arr.s)/sum(arr.s),1/sqrt(sum(arr.s)))
