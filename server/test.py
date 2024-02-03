import pandas as pd
import numpy as np
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split

df=pd.read_csv('s_diabetes.csv')
cdf=df.copy()

X=cdf.drop(columns='Outcome',axis=1)
y=cdf['Outcome']

sc=StandardScaler()
X_std = sc.fit_transform(X)
X_train,X_test,y_train,y_test=train_test_split(X_std,y,test_size=0.2,stratify=y,random_state=2)

classifier=svm.SVC(kernel='linear')

classifier.fit(X_train,y_train)

def predict(data):
    n = np.asarray(data)
    input_data = n.reshape(1, -1)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        std_data = sc.transform(input_data)
        prediction=classifier.predict(std_data)
        return 0 if prediction[0]==0 else 1