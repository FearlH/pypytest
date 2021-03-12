import numpy as np
import pandas as pd
#列是一样的
df1=pd.DataFrame(np.ones([3,4])*1,columns=["a","b","c","d"])
df2=pd.DataFrame(np.ones([3,4])*2,columns=["a","b","c","d"])
df3=pd.DataFrame(np.ones([3,4])*3,columns=["a","b","c","d"])
df4=pd.DataFrame(np.ones([3,4])*4,columns=["a","b","c","d"])
print(df1)
res=pd.concat([df1,df2],axis=0)#行上合并
print(res)#这样索引还是都是原来的索引
res1=pd.concat([df2,df3],axis=0,ignore_index=True)#在axis上面忽略原始的index
print(res1)


#join,["inner","outer"]
df3=pd.DataFrame(np.ones([3,4])*3,columns=["a","b","c","d"],index=[1,2,3])
df4=pd.DataFrame(np.ones([3,4])*4,columns=["b","c","d","e"],index=[2,3,4])
print(df3)
print(df4)

res3=pd.concat([df3,df4])#jin默认outer
print(res3)#没有的特征用none来替换

res3=pd.concat([df3,df4],join="inner",ignore_index=True)
print(res3)#合并一样的特征,没有的就删除

res4=pd.concat([df3,df4],axis=1)
print(res4)

#append

A=df1.append([df2,df3],ignore_index=True)
print(A)
A.append(pd.Series([1,2,3,4],index=['a',"b","c","e"]),ignore_index=True)

#merge


df1=pd.DataFrame({"Key0":["a","b","c","d"],
                "A":["A0","A1","A2","A3"],
                "B":["B0","B1","B2","B3"],
                "Key1":[1,2,3,4]
                },index=["a1","a2","a3","a4"])
df2=pd.DataFrame({"Key0":["a","e","c","d"],
                "C":["C0",'C1','C2','C3'],
                'D':['D0','D1','D2','D3'],
                "Key1":[1,2,9,4]},index=["b1","b2","b3","b4"])

print(df1,"\n",df2)

#merge

res=pd.merge(df1,df2,on=["Key0","Key1"])#在哪一个上面合并,公共的才可以
print(res)
#how={"left","right","inner","outer"}  按照前面一个，后面一个的Key来填充
res1=pd.merge(df1,df2,on=["Key0","Key1"],how="left",indicator="out")#按照df1的Key
print(res1)
#indicate表示数据从哪里来
print(df1)
res2=pd.merge(df1,df2,how="outer",left_index=True,right_index=True)
print(res2)





