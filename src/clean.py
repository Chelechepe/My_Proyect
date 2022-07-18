import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

def check (dict_, key, string_):
    """" this function replace words for hey words in a list"""
    for i in dict_[key]:
        if i in string_:
            return key

def activityclean(string):
    #lowercase for functions and Title for Classes
    """Cleans the strings of text and converts it to useful simplifications"""
    string = str(string).lower().strip()
    if string != string:
        return np.nan
    elif "swimming" in string or"bathing" in string or "floating" in string or "splashing" in string or "jumped into the water" in string or "playing" in string:
        return "swimming"
    elif "diving" in string or "snorkel" in string:
        return "diving"
    elif "fishing" in string:
        return "fishing"
    elif "surf" in string or "body boarding" in string or "body-boarding" in string or "boogie boarding" in string or "paddleskiing" in string:
        return "surf"
    elif "standing" in string:
        return "standing"
    elif "kayaking" in string or "ship" in string or "sail" in string or "boat" in string or "canoeing" in stricng or "board" in string or "rowing" in string or "fell into the water" in string:
        return "boating"
    elif "disaster" in string:
        return "sea disaster"
    elif "wading" in string or "walking" in string or "treading water" in string:
        return "walking"
    else:
        return np.nan

def replace (df,column,source,output):
    """" this function will replace an unwanted word in a column 
    and will imput the desired nomenclature"""
    s = source
    o = output
    c = column
    df[c] = df[c].replace([s],[o])
    pass

def dropna_colum (df,column):
    """"this function will dropna in a specific column
    and return the dataframe displaying random 5 lines"""
    df = df.dropna(subset=["Column"])
    return df.sample(5)

def columnnullcount (df):
    """this function returns a list of all the columns 
    and the count of null values """
    return df.isnull().sum()

def checking ():
    print('this workssss')