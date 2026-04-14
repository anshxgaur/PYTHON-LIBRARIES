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


#consider a dataframe with 3 fields marks , subjects , grade appluy mean , median , mode on the appropriate data. and also find outlier if exists

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'marks': [30, 50, 60],
    'grade': ['a', 'b', 'b'],
    'subjects': ['hindi', 'english', 'french']
}
df = pd.DataFrame(data)

# Mean, Median, Mode
mean_marks = df['marks'].mean()
median_marks = df['marks'].median()
mode_marks = df['marks'].mode()[0]

mode_grade = df['grade'].mode()[0]
mode_subject = df['subjects'].mode()[0]

print("Mean (Marks):", mean_marks)
print("Median (Marks):", median_marks)
print("Mode (Marks):", mode_marks)
print("Mode (Grade):", mode_grade)
print("Mode (Subject):", mode_subject)

# Detecting Outliers using IQR
Q1 = df['marks'].quantile(0.25)
Q3 = df['marks'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['marks'] < lower_bound) | (df['marks'] > upper_bound)]
print("\nOutliers in Marks:")
print(outliers if not outliers.empty else "No outliers found")

# Visualization
plt.figure(figsize=(10,4))

# Boxplot for marks
plt.subplot(1,2,1)
plt.boxplot(df['marks'])
plt.title("Boxplot of Marks")

# Bar plot for grade distribution
plt.subplot(1,2,2)
df['grade'].value_counts().plot(kind='bar', title="Grade Distribution")

plt.tight_layout()
plt.show()



