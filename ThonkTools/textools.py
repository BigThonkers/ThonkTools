"""This here was my attempt at doing this with Pandas. Seemed too complex to me, though.

def csvtex(fname,caption,index=None):
    import pandas as pd
    data=pd.read_csv(fname,delimiter='\t',index_col=None)
    print('\\begin{{table}}[h]\n\centering\n\caption{{{0}}}\vspace{{11pt}}\n\\begin{{tabular}}{{{1}}}\n\\toprule\n{2} '.format(caption,len(data.columns)*'c',('\\textrm{{{1}}}/\\textrm{{}} & '.format(x) for x in list(data.columns.values))))
    print('\midrule')
    print(data.iat[0,0],'&',data.iat[1,0],'\n\hline')
    print('\\bottomrule\n\end{{tabular}}\n\label{{Tab:{0}}}\n\end{{table}}'.format(tabnum))"""

'''
Takes a csv file and outputs it as LaTeX code for use in a LaTeX table.

Filename must be input as a string, and can be of any file type. 

Currently, the only option for style other than None is "nutrition".
The nutrition style will output a LaTeX table in standard scientific table style, which resembles a nutrition table.
If no style is set, only the values with tabs replaced by ampersands and new lines replaced with slashes will be output.
Default is None.

The caption and label are only useful for styles and will apply the caption and label to the output table code.
These can easily be located and modified later on, though.
Defaults are "CAPTION" and "Tab:X" in order to stand out and be a reminder that these should be changed.

The index option is a planned feature to introduce index columns.
Default is and will remain None.

line_break toggles whether new lines should be started after slashes.
Default is on.

dec_comma toggles whether commas or dots should be used for decimals.
Default is off, meaning dots are output.

Example:
    Let us assume a csv file including a total of six values evenly split across two rows:
    
    ~/Documents/file.txt reads:
    a   b   c
    d   e   f

    The simplest scenario usage here would be:

    import ThonkTools as TT
    
    TT.csvtex("~/Documents/file.txt")

    output reads:
    a & b & c \\
    d & e & f


TODO: 
Index column option
'''


def csvtex(filename: str, style=None, caption="CAPTION", label="Tab:X", index=None, line_break=True, dec_comma=False):
    if line_break == False:
        with open(filename) as data:
            data = data.read().replace(',', '.').replace('\n', ' \\\\ ').replace('\t', ' & ')[:-4]
    elif line_break == True:
        with open(filename) as data:
            data = data.read().replace(',', '.').replace('\n', ' \\\\\n').replace('\t', ' & ')[:-4]
    if dec_comma == True:
        data = data.replace('.', ',')
    if style == "nutrition":
        linelength = list(zip(data, data[1:])).index(('\\', '\\'))
        columncount = ['c' for x in data[:linelength] if x == '&'] + ['c']
        print("\\begin{table}[h]\n\\caption{"
              + caption +
              "}\\vspace{11pt}\n\\begin{tabular}{"
              + ''.join(columncount) +
              "}\n\\toprule\n", "\\textrm\{XXXX\}/\\textrm\{XX\}" * len(columncount) +
              "\\\\\n\\midrule\n"
              + data +
              "\n\\bottomrule\n\\end{tabular}\n\\label{"
              + label +
              "}\n\\end{table}")
        return
    else:
        print(data)
        return


'''
Tool to convert lists, arrays, and uarrays to LaTeX code. Very few options now, and chaining these isn't really easy.
'''


def arrtex(array, row=True, column=False):
    if row == True and column == False:
        conv = str(array)
        if '+' in conv:
            out = conv.replace(' ', ' & ').strip('[]').replace('+/-', ' \\pm ')
        else:
            out = conv.replace(' ', ' & ').strip('[]')
        return print(out)
    elif row == False or column == True:
        conv = str(array)
        if '+' in conv:
            out = conv.replace(' ', ' \\\\ ').strip('[]').replace('+/-', ' \\pm ')
        else:
            out = conv.replace(' ', ' \\\\ ').strip('[]')
        return print(out)
