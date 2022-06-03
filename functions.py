import pandas as pd
import plotly.express as pl
import plotly.io as pio
import os
import glob

def getFile(file):
    '''
    Convenience function for FileReader
    Loads in a single file, adds a "year" value extracted from the filename

    Parameters
    -----------
    file: a filename to read

    Returns
    -----------
    A DF of the file, with column headers and added Year from filename
    '''
    ret = pd.read_csv(file,names = ['Name','Sex','Count'])
    print(file)
    ret['Year'] = int(file[11:15])
    ret['Rank'] = ret.groupby(['Year','Sex'])['Count'].rank(method='dense',ascending=False)
    return ret


def fileReader(source):
    '''
    Loops through all of the files in 
    both names and namesbystate files and 
    writes to pandas dataframe
    
    Parameters
    -----------
    source: either included folder names or namesbystagte

    Returns
    --------
    A dataframe of the concatenated files
    Two added columns are calculated: 
        A year variable, derived from the filename
        A year-sex rank variable from the count
    '''
    df = pd.concat([getFile(f) for f in glob.glob('./' + source + '/*.txt')], ignore_index = True)
    df.to_csv('./' + source +'.csv')
    return df   

def nameStartsWith(name,n):
    '''
    Creates a substring of the name 
    to allow selecting names that start
    with a letter or a series
  
    Parameters
    -----------  
    name: column containing the name
    n: number of letters to select

    Returns
    -----------
    the selected substring
    '''
    substr = name[:n]
    
    return substr

def NameEndsWith(name,n):
    '''
    Creates a substring of the name 
    to allow selecting names that end
    with a letter or a series
  
    Parameters
    -----------  
    name: column containing the name
    n: number of letters to select

    Returns
    -----------
    the selected substring
    '''
    substr = name[-n:]
    
    return substr


def NameSelector(df,names,minyear, maxyear, sex):
    '''
       Plotting convienience function: 
        Selects a single name-sex-time period combo. 
    
    Parameters
    -----------  
    df: pandas DF of name data
    names: List containing one or more names
    minyear: Minimum year to select (Earliest is 1883)
    maxyear: Maximum year to select (Latest is 2020)
    sex: M or F

    Returns
    -----------
    A single df of selected name-sex-time period combo
 
    '''
    namevector = df[
        (df['Name'].isin(names)) & 
        (df['Sex']==sex) & 
        (df['Year']>=minyear) & 
        (df['Year']<=maxyear)
        ].sort_values(by=['Name','Year'])

    return namevector

def nameGraph(df,names,minyear,maxyear,sex):
    '''
    Plot a set of names for a given time period
    
    Parameters
    ----------- 
    names: List containing one or more names
    minyear: Minimum year to select (Earliest is 1883)
    maxyear: Maximum year to select (Latest is 2020)
    sex: M or F

    Returns
    -----------
    The requested plot
    '''
    fig = pl.line(NameSelector(df,names,minyear,maxyear,sex), x="Year", y="Count", color='Name',template='plotly_dark')
    fig.show()



