
import numpy as np
import pandas as pd
import re
import sys
import random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

from datetime import datetime, date


# In[2]:


clf3 = joblib.load('.\model.pkl')


# In[59]:


def getweek(date):
    dayOfWeek = []
    for i in range(len(date)):
        split = re.split('-| :',date[i])
        week = datetime(int(split[0]),int(split[1]),int(split[2])).weekday()
        dayOfWeek.append(week)
    return dayOfWeek


# In[60]:


#date0=['2019-03-03', '2018-03-03']


# In[61]:


#print(getweek(date0))


# In[68]:


def predictVac(date, time, garageNo):
    x_test = pd.DataFrame({'dayOfWeek':getweek(date), 'time':time, 'garageNo':garageNo})
    return clf3.predict(x_test).astype(int)


# In[69]:


#print(predictVac(['2019-03-03', '2018-03-03'],[12,2],[3,2]))

ans = predictVac([sys.argv[1], sys.argv[1], sys.argv[1], sys.argv[1]], [int(sys.argv[2]),int(sys.argv[2]),int(sys.argv[2]),int(sys.argv[2])], [0,1,2,3])

print([int(ans[0][0]), int(ans[1][0]), int(ans[2][0]), int(ans[3][0])])

