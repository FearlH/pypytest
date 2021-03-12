import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

font={"family":"fangsong"}
matplotlib.rc("font",**font)
df=pd.read_csv("D:\\233\\donwload\\iris.data")

y=df.iloc[0:100,4].values#切片 先行后列
y=np.where(y=="Iris-setosa",1,-1)

print(np.sum(y==1))#统计个数


x=df.iloc[0:100,[0,2]].values#单行单列numpy数组

plt.scatter(x[0:49,0],x[0:49,1],color="r",marker="o",label="se")
plt.scatter(x[49:100,0],x[49:100,1],color="blue",marker="x",label="ve")
plt.xlabel("花瓣长度")
plt.ylabel("萼片长度")
plt.show()