#Why we use pandas
# it contains mulitple data structure and data manipulation tools that is used for data cleaning. Furthermore, it 
# is designed to work with hetrogeneous data.

#  Content Covered in this file  #
#  1. Series 
#  2. DataFrame


# Importing pandas package
import pandas as pd

# 1. Series (one dimensional array-like object) (you can think of it as a fixed-length dict)
data=[1,2,3,4,5]
index=['one','two','three','four','five']
series=pd.Series(data,index)
print(series)
print(series.index)
print(series['two'])
series['three']=33
print(series['three'])
print(series[series>1])
print(series*2)
print(3 in series)
# we also pass dic in series
dic={"one":111,"two":222,"three":333}
series2=pd.Series(dic)
print(series2)
