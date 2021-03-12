import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
class Preception:
    '''
    eta 学习率
    n_iter 迭代次数
    '''
    def __init__(self,eta=0.01,n_iter=10):#定义参数
        self.eta=eta
        self.n_iter=n_iter
        print(self.n_iter,n_iter)
    def fit(self,X,Y):
        self.X=X
        self.Y=Y
        self.theta_s=np.zeros(X.shape[1]+1)
        self.errors=[]
        for i in range(self.n_iter):
            error=0
            for Xi,Yi in zip(self.X,self.Y):#第一轮预测里面求error
                target=self.predict(Xi)
                update=self.eta*(Yi-target)
                self.theta_s[1:]+=update*Xi
                self.theta_s[0]+=update
                error+=int(update!=0.0)
            self.errors.append(error)
        return  self



    def get_input(self,Xi):
        return np.dot(Xi,self.theta_s[1:])
    def predict(self,Xi):
        return np.where(self.get_input(Xi)>=0.0,1,-1)

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

plt.figure()
ppn=Preception(eta=0.1,n_iter=10)

ppn.fit(x,y)
plt.plot(range(1,len(ppn.errors)+1),ppn.errors,marker="o")
plt.xlabel("次数")
plt.ylabel("error")
plt.show()


