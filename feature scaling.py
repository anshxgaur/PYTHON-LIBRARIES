
#feature scaling standarization / normalization 0-1 
#now we will proceed standarization to make the dataset normal to acces the dataset 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv(r"C:\Users\ansh1\OneDrive\Desktop\CODING\Social_Network_Ads.csv")
print(df.head())     

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Encode categorical variables before scaling
X = df.drop("Purchased", axis=1)
le = LabelEncoder()
X['Gender'] = le.fit_transform(X['Gender'])

x_train, x_test, y_train, y_test = train_test_split(X, df["Purchased"], test_size=0.30, random_state=0)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
x_train = pd.DataFrame(x_train, columns=X.columns)
x_test = pd.DataFrame(x_test, columns=X.columns)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].set_title("Before Scaling", fontsize=16)
sns.kdeplot(df['Age'], ax=axes[0])
sns.kdeplot(df['EstimatedSalary'], ax=axes[0])
sns.kdeplot(x_train.iloc[:, 2], ax=axes[1])

axes[1].set_title("After Scaling", fontsize=16)
sns.kdeplot(x_train['Age'], ax=axes[1])
sns.kdeplot(x_train['EstimatedSalary'], ax=axes[1])
plt.tight_layout()
plt.show()
