from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler,Normalizer
import numpy as np
X_train = np.array([[1.,-1.,2.],[2.,0.,0.],[0.,1.,-1.]])
X_scaled = preprocessing.scale(X_train)
print(X_scaled)
X_scaled.mean(axis=0)
X_scaled.std(axis=0)
MM_X = MinMaxScaler().fit_transform(X_train)
print(MM_X)
X = [
    [4,4,2,2],
    [1,3,9,3],
    [5,7,5,1]
] 
transformer = Normalizer().fit(X)
transformer.transform(X)