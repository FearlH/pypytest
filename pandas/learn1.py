import pandas as pd
import numpy as np
data={"name":["name1","name2","name3"],"age":[1,2,3]}
pd.DataFrame(data)
s=pd.Series([0,1,2,np.nan,1])#单列表
print(s)

dates=pd.date_range("20200101",periods=6)#生成6天
print(dates)


df=pd.DataFrame(np.arange(24).reshape((4,6)),index=["a","b","c","d"],columns=dates)#给定行和列
print(df)
print(pd.DataFrame(np.arange(12).reshape(3,4)))#不给定就按照123
print(df.index)
print(df.columns)
print(df.values)
print(df.describe)
C=df.T#转置

df.sort_index(axis=0,ascending=False)#对于0维度排序，然后Flase表示倒叙
#按照行或者列的标签标签排序
print(df)
df.sort_values(by="2020-01-01",ascending=False)#按照某个列排序

df1=pd.DataFrame(np.arange(15).reshape(3,5),columns=["a","b","c","d","e"])
dates=pd.date_range("20200101",periods=4)
print(dates)
df2=pd.DataFrame(np.arange(12).reshape(3,4),index=["a","b","c"],columns=dates)
print(df1)
print(df2)
print(df1["a"])

print(df1[0:2])
print(df2["2020-01-01":"2020-01-03"])
print(df2["a":"b"])#只能对于行切片



#loc 根据标签选择
print(df2.loc["a"])#根据标签选择
print(df1.loc[1])#可以按照行选择

print(df1.loc[:,["a","c"]])#跟切片比较像
print(df1.loc[:,"a":"c"])
print(df1.loc[0:2,:])#这个里面的切片都是闭合的


#iloc 根据位置来选择

print(df1.iloc[2])
print(df1.iloc[0:2])#真的切片了
print(df1.iloc[:,0:2])

print(df1.iloc[[1,2],0:2])


#组合筛选


#条件筛选

print(df1["a"]>8)
c=df1["a"]>8
print(df1[c])
print(df1[df1["a"]>8])

df1.iloc[2,2]=1000
print(df1)

df1[df.a>4]=0#改变df1
df1.a[df.a>4]=0#改变df1的a
df1.b[df.a>4]=0

df1["g"]=np.nan
print(df1)
print(df1.shape[1])
df1["e"]=np.arange(df1.shape[0])#有多少行
print(df1)


#数据丢失了

df1.iloc[1,2]=np.nan
df1.iloc[2,4]=np.nan

T=np.array([0,0,0])
G=T[np.newaxis,:]

print(df1)
df1.loc[:,"g"]=pd.Series([0,0,0,0,0])

print(df1.dropna(axis=0,how="any"))#丢弃行或者列
#how={"any","all"}#any就是只要有一个nan就丢弃，all就是都是nan丢弃
print(df1)

df.fillna(value=0)#把value填写进入nan里面
print(df1.isna())
print(df1.isnull())
print(np.any(df1.isna()))


#导入导出

#read_csv  read_excel  to_csv  to_excel

A=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learing-databases/iris/iris.data",header=None)

A=pd.read_csv("D:\\233\\donwload\\iris.data")
A.tail()








