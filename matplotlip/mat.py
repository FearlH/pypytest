import matplotlib.pyplot as plt#一般导入这个
import numpy as np
import pandas as pd
import matplotlib
font={"family":"fangsong","weight":"bold","size":12}
matplotlib.rc("font",**font)
x=np.linspace(-1,1,50)#生成等差数列
y=2*x+1
y2=2*x*x+1
plt.figure()#打头后面的数据就都在这个figure里面了
plt.plot(x,y)
plt.xticks(ticks=np.linspace(-1,1,10),labels=["刻度{}".format(i) for i in range(10)])#ticks 刻度
plt.show()


plt.figure(num=3,figsize=[10,10])
plt.plot(x,y2,color="red")
plt.plot(x,y,color="blue",linewidth="1.0",linestyle="--")
plt.show()#只需要一个show
#保存图形 

plt.figure(figsize=(20,40),dpi=100)
