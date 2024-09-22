import numpy as np
import pandas as pd
from numpy.random import randn
labels = ['w','x','y','z']
List = [10,20,30,40]
array = np.array([10,20,30,40])
Dict = {'w':10,'x':20,'y':30,'z':40}
print(pd.Series(data = List))
print(pd.Series(data = List,index = labels))
print(pd.Series(List,labels))
print(pd.Series(array,labels))
print(pd.Series(Dict))
Sports = pd.Series([1,2,3,4],index = ['Cricket','Football','Basketball','Golf'])
print(Sports)
np.random.seed(1)
dataframe = pd.DataFrame(randn(10,5),index = 'A B C D E F G H I J'.split(),columns = 'Score1 Score2 Score3 Score4 Score5'.split())
print(dataframe)
print(dataframe['Score3'])
print(dataframe[['Score2','Score1']])
print(type(dataframe['Score1']))
#Adding a new column to the dataframe
dataframe['Score6'] = dataframe['Score1']+dataframe['Score2']
print(dataframe)
#Removing columns from Dataframe
print(dataframe.drop('Score6',axis = 1)) #use axis = 0 for dropping rows and axis = 1 for dropping columns
#Selecting rows
print(dataframe.loc['F'])
#Select based on index position
print(dataframe.iloc[2])
#Conditional selection
dt1 = dataframe>0.5
print(dt1)
dt2 = dataframe[dataframe>0.5]
print(dt2)
#Dealing with missing data
df = pd.DataFrame({'Cricket':[1,2,np.nan,4,6,7,2,np.nan],
                          'Basketball':[5,np.nan,np.nan,5,7,2,4,5],
                          'Tennis':[1,2,3,4,5,6,7,8]})
#print(dataframe)
dt1 = df.dropna()
print(dt1)
dt2 = df.fillna(value = 0)
print(dt2)
#Groupby method
dat = {'CustID':['1001','1001','1002','1002','1003','1003'],
       'CustName': ['UIPat', 'DatRob', 'Goog', 'Chrysler', 'Ford', 'GM'],
       'Profitinlakhs':[2005,3245,1245,8765,5463,3547]}
group_by_df = pd.DataFrame(dat)
print(group_by_df)
CustID_grouped = group_by_df.groupby('CustID').mean('Profitinlakhs')
print(CustID_grouped)
#Combinig dataframes together - merging, joining and concatenating
dafa1 = pd.DataFrame({'CustID':['101','102','103','104'],
                      'Sales':[13456,45321,54385,53212],
                      'Priority':['CAT0','CAT1','CAT2','CAT3'],
                      'Prime': ['yes', 'no', 'no', 'yes']},
                     index = [0,1,2,3])
#print(dafa1)
dafa2 = pd.DataFrame({'CustID': ['101', '103', '104', '105'],
                        'Sales': [13456, 54385, 53212, 4534],
                        'Payback': ['CAT4', 'CAT5', 'CAT6', 'CAT7'],
                        'Imp': ['yes', 'no', 'no', 'no']},
                         index=[4, 5, 6, 7])
#print(dafa2)
dafa3 = pd.DataFrame({'CustID': ['101', '104', '105', '106'],
                        'Sales': [13456, 53212, 4534, 3241],
                        'Pol': ['CAT8', 'CAT9', 'CAT10', 'CAT11'],
                        'Level': ['yes', 'no', 'no', 'yes']},
                        index=[8, 9, 10, 11])
#print(dafa3)
con = pd.concat([dafa1,dafa2,dafa3],axis=1)
#print(con)
mer = pd.merge(dafa1,dafa2,how ='inner',on = 'CustID')
#print(mer)
daf3 = pd.DataFrame({'Q1':['101','102','103'],
                     'Q2':['201','202','203']},
                    index = ['IO','I1','I2'])
daf4 = pd.DataFrame({'Q3':['301','302','303'],
                     'Q4': ['401','402','403']},
                    index = ['IO','I2','I3'])
daf5 = daf3.join(daf4)
print(daf5)