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
df['marks'] = df['marks'].fillna(df['marks'].mean())
print(df)
#   marks gender
#0   10.0      f
#1   20.0      m
#2   30.0      f
#3   40.0      f
#4    NaN      m
#   marks gender
#0   10.0      f
#1   20.0      m
#2   30.0      f
#3   40.0      f
#4   25.0      m

# filling gender values using mode function:
import pandas as pd
import numpy as np
data = { 'marks':[10,20,30,40,50],'gender':['f','m','f','f',np.nan]}
df = pd.DataFrame(data)
df['gender'] = df['gender'].fillna(df['gender'].mode()[0])

#    marks gender
# 0     10      f
# 1     20      m
# 2     30      f
# 3     40      f
# 4     50      f


# making box plot of the data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = { 
    'marks': [10, 20, 30, 40, 200]
}
df = pd.DataFrame(data)
# Box plot
plt.boxplot(df['marks'])
plt.title("Box Plot of Marks")
plt.ylabel("Marks")
plt.show()




