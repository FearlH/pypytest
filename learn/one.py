import numpy as np
class Preception(object):
    def __init__(self,eta=0.01,n_iter=10):
        self.eta=eta
        self.n_iter=n_iter
    def fit(self,X,y):
        self.w_=np.zeros(1+X.shape[1])#权值等于X输入的列上面的个数+1
        self.errors_=[]

        for _ in range(self.n_iter):
            errors=0
            for xi,target in zip(X,y):
                update=self.eta*(target - self.predict(xi))
                self.w_[1:]+=update*xi
                self.w_[0]+=update
                errors+=int(update!=0.0)
            self.errors_.append(errors)

    
    def net_input(self,J):
        return np.dot(J,self.w_[1:])+self.w_[0]
    def predict(self,J):
        return np.where(net_input(self,J)>=0.0,1,-1)
