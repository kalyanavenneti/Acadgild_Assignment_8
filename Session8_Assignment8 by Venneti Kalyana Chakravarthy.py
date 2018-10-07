
# coding: utf-8

# In[9]:


#Question 1: How-to-count-distance-to-the-previous-zero For each value, count the difference of the distance from 
#the previous zero (or the start of the Series, whichever is closer) and if there are no previous zeros, print the position
#Consider a DataFrame df where there is an integer column {'X':[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]}
#The values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new column 'Y'. 
#import pandas as pd
#df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

import pandas as pd
df=pd.DataFrame({'X':[7,2,0,3,4,2,5,0,3,4]})
df_series=df['X']
x=[(df_series.tolist() [i::-1]+[0]).index(0) for i in range(len(df_series.tolist()))]
df['Y']=x

print("Output \n")
print("Dataframe input column values are \n",df['X'].tolist(),"\n")
print("The Counter position for available zero in dataframe column is \n",x,"\n")
print("Output DataFrame \n")
df


# In[14]:


#Question 2: Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers

import pandas as pd
import numpy as np

Datedata=pd.date_range(start='2015-01-01', end='2015-12-31', freq='B')
randomNum=np.random.rand(len(Datedata))
s=pd.Series(randomNum, index=Datedata)

print("Output: \n")
print("Few observations of series object are \n",s.head(), "\n")
print("Index of series object are \n", s.index)


# In[17]:


# Question 3: Find the sum of the values in s for every Wednesday

s[Datedata.weekday_name=='Wednesday'].head()
print("Output: \n")
print("Sum of values for Wednesday in s:") 
s[Datedata.weekday_name=='Wednesday'].sum()


# In[21]:


# Question 4: Average For each calendar month
print("Output: \n")
s.resample('M', convention='end').mean()


# In[25]:


# Question 5: For each group of four consecutive calendar months in s, find the date on which the highest value occurred

print("Output: \n")
print("Duration of consecutive 4 months, till that highest value recorded: \n")
print(s.groupby(pd.Grouper(freq='4M')).idxmax(), "\n")
print("Maximum value for the recorded date: \n")
print(s[s.groupby(pd.Grouper(freq='4M')).idxmax()])

