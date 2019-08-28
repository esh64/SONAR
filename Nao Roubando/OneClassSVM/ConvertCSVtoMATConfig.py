import pandas as pd
import scipy.io
import os 

files=os.listdir('.')
for file in files:
    if '.csv' not in file:
        continue
    dict={}
    csv1=pd.read_csv(file, sep=';')
    dict['Unspecialized']=csv1.Unspecialized.values
    dict['Hierarchic']=csv1.Hierarchic.values
    dict['Competitive']=csv1.Competitive.values
    scipy.io.savemat(file[:-4], dict)
