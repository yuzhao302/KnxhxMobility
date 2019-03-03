#
import numpy as np
import pandas as pd
import re
import sys
import random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

from datetime import datetime, date

clf3 = joblib.load('/KNOXHEX/model.pkl')

# In[2]:


# clf3 = joblib.load('model.pkl')


# In[59]:

# print(predictVac(['2019-03-03'],[12],[2]))
print([100,200,340,500])