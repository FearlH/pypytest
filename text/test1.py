import numpy as np
class  Prediction(Object):
    def __init__(self,l_rate=0.01,n_iter=10):
        self.l_rate=l_rate
        self.n_iter=n_iter
    def fit(self,X,y):
        self.w_=np.zeros(X.shape[0]+1)
        self.errors=[]
        for  n in range(self.n_iter):
            error=0
            for Xi,target in zip(X,y):
                update=(target-self.predict(Xi,y))
                self.w_[1:]+=update*self.l_rate*Xi
                self.w_[0]=update*self.l_rate
                error+=int(update!=0)
            self.errors.append(error)
        return self
                


    def predict(self,Xi,y):
        return np.where(self.input(Xi)>=0.0,1,-1)

    def input(self,Xi):
        return np.dot(Xi*self.w_[1:])+self.w_[0]
        

        