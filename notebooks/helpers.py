import os
import pandas as pd
import numpy as np
import re
            
# Helpers to clean up resulting left merge
def drop_y(df):
    # list comprehension of the cols that end with '_y'
    to_drop = [x for x in df if x.endswith('_y')]
    df.drop(to_drop, axis=1, inplace=True)
    
def rename_x(df):
    for col in df:
        if col.endswith('_x'):
            df.rename(columns={col:col.rstrip('_x')}, inplace=True)
            
def team_remove (row):
    return re.sub("[\(\[].*?[\)\]]", "", row['Player'])[:-1]