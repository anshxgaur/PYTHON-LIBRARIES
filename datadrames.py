#create a dataframe in which gender and marks will be given and you have to enter atleast 5 entries
import pandas as pd
data = { 'marks':[10,20,30,40,50],'gender':['f','m','f','f','m']}
df = pd.DataFrame(data)
print(df)
        
# in order to find the mean of this data:
df = pd.DataFrame(data)
mean_val = df['marks'].mean()
median_val = df['marks'].median()
mode_val = df['gender'].mode()
print(mean_val)
print(median_val)
print(mode_val)

# change of dataframe:

import pandas as pd
import numpy as np
data = { 'marks':[10,20,30,40,np.nan],'gender':['f','m','f','f','m']}
df = pd.DataFrame(data)
print(df)
df['marks']
