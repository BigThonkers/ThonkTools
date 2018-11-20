"""This here was my attempt at doing this with Pandas. Seemed to complex to me, though.

def csvtex(fname,caption,index=None):
    import pandas as pd
    data=pd.read_csv(fname,delimiter='\t',index_col=None)
    print('\\begin{{table}}[h]\n\centering\n\caption{{{0}}}\vspace{{11pt}}\n\\begin{{tabular}}{{{1}}}\n\\toprule\n{2} '.format(caption,len(data.columns)*'c',('\\textrm{{{1}}}/\\textrm{{}} & '.format(x) for x in list(data.columns.values))))
    print('\midrule')
    print(data.iat[0,0],'&',data.iat[1,0],'\n\hline')
    print('\\bottomrule\n\end{{tabular}}\n\label{{Tab:{0}}}\n\end{{table}}'.format(tabnum))"""


'''
TODO: 
Formatting (as above)
Index column option
'''

def csvtex(filename,style=None,index=None,line_break=True,dec_comma=False):
    if line_break==False:
        with open (filename) as data:
            data=data.read().replace(',','.').replace('\n',' \\\\ ').replace('   ',' & ')[:-4]
    elif line_break==True:
        with open (filename) as data:
            data=data.read().replace(',','.').replace('\n',' \\\\\n').replace('   ',' & ')[:-4]
    if dec_comma==True:
        data=data.replace('.',',')
    print(data)
    return

'''
This function will convert arrays to LaTeX tables. Same options as above.
'''

def arrtex(filename):
    return







