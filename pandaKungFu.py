
# Parallelization support #rvm 2018-04-21
# copyied from the (c)Internet, 
from joblib import Parallel, delayed
import multiprocessing
import re

def applyParallel(dfGrouped, func, *args):
    '''
    runs an pandas.DataFrame.groupby().apply(func) in parallel.
    Usage:
    applyParallel(pandas.DataFrame.groupby(), func) 
    
    (contact) Raoul
    '''
    retLst = Parallel(n_jobs=multiprocessing.cpu_count())(delayed(func)(group, args) for name, group in dfGrouped)
    return pd.concat(retLst)

def headdf(df, regex='.*', lines=5):
    '''
    returns a df.head filtered for the columns that match the regex
    (contact) Raoul
    '''
    return(df[[col for col in df.columns.tolist() if re.compile(regex).match(col)]].head(lines))

def registerHead2(pandas, headdf):
    '''
    registers headdf(DataFrame) as method of your pandas.DataFrame object.
    Usage:
    # Import packages as usual
    import pandas as pd
    from mofuutil import pandaKungFu
    # apply the registering
    pandaKungFu.registerHead2(pd, pandaKungFu.headdf)
    
    #now you use
    mydf = pd.DataFrame(...something to create a dataframe...)
    mydf.head2('.*?limp.*',3) # returns head(3) for all columns like 'Blimp', 'limphodus' etc.
    '''
    pandas.DataFrame.head2 = headdf
    print('You can now use DataFrame.head2(regex, lines) in pandas')
    