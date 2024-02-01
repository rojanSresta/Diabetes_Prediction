
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

df=pd.read_csv('s_diabetes.csv')

df.shape


df.head(40)




df.info()




cdf=df.copy()




cdf.describe()




cdf.isna().sum()




cdf.columns




cdf.duplicated().sum()




# plt.figure(figsize=(15,5))
# ax=sns.countplot(x='Outcome',data=cdf)
# for bars in ax.containers:
#     ax.bar_label(bars)
# plt.show()




#observing outliers
# plt.figure(figsize=(10,10))
# for i,col in enumerate(['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']):
#     plt.subplot(3,3,i+1)
#     sns.boxplot(x=col,data=cdf)
# plt.show()




# sns.pairplot(cdf,hue='Outcome')
# plt.figure(figsize=(10,20))
# plt.show()




# plt.figure(figsize=(10,10))
# for i,col in enumerate(['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']):
#     plt.subplot(3,3,i+1)
#     sns.histplot(x=col,data=cdf,kde=True)
# plt.show()




# plt.figure(figsize=(20,20))
# sns.heatmap(cdf.corr(numeric_only=True),annot=True) 


X=cdf.drop(columns='Outcome',axis=1)




y=cdf['Outcome']




X




y




sc=StandardScaler()




sc.fit(X)




sd = sc.transform(X)




sd




X=sd
y=cdf['Outcome']




X




from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,stratify=y,random_state=2)




print(X.shape,X_train.shape,X_test.shape)




#training the model
from sklearn import svm
classifier=svm.SVC(kernel='linear')




#training the support vector machine classifer #machine laerning model
classifier.fit(X_train,y_train)




from sklearn.metrics import accuracy_score




#model evaluation
#acuuracy for training data
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,y_train)
training_data_accuracy




X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,y_test)
test_data_accuracy




from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(max_depth=2,n_estimators=200)
rclf = rf.fit(X_train,y_train)
y_pred = rclf.predict(X_test)
accuracy_score(y_pred,y_test)




from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(max_depth=3)
clf = tree.fit(X_train,y_train)
y_pred = clf.predict(X_test)
accuracy_score(y_pred,y_test)
print(y_pred[130])




from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
knnclf = neigh.fit(X_train,y_train)
y_pred = knnclf.predict(X_test)
accuracy_score(y_pred,y_test)


# making the prediction system



from sklearn.preprocessing import StandardScaler

input_data = (2,121,70,32,95,39.1,0.886,23)

# changing it into numpy array
n = np.asarray(input_data)

# reshape
input_data_reshape = n.reshape(1, -1)

# standardize the input data
std_data = sc.transform(input_data_reshape)
print(std_data)
prediction=classifier.predict(std_data)
print(prediction)
if(prediction[0]==0):
    print("the person is not diabetic")
else:
    print("the person is diabetic")
    





















