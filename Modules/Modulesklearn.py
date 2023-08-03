import numpy as np
from sklearn import linear_model, datasets
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

"""
# diabetes data set

diabetes = datasets.load_diabetes()

# ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']

# print(diabetes.data)

diabetes_X_train = diabetes.data
diabetes_y_train = diabetes.target

diabetes_X_test = diabetes_X_train[:]
diabetes_y_test = diabetes_y_train[:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_predicted = model.predict(diabetes_X_test)  # 1st regression
# diabetes_y_predicted2 = model.predict()

for i, j in zip(diabetes_y_test, diabetes_y_predicted):
    print(f"{i} ,  {j:.2f}")

print("Mean Squared Error is :", mean_squared_error(diabetes_y_test, diabetes_y_predicted))

# plt.scatter(diabetes_X_test, diabetes_y_test)
# plt.plot(diabetes_X_test, diabetes_y_predicted)

# plt.show()

print("Weights : ", model.coef_)
print("Intercept :", model.intercept_)
"""

"""
# iris peals dataset 
# Iris- Setosa, Iris-Versicolour, Iris-Virginica

dataset = datasets.load_iris()

iris_X_train = dataset.data
iris_y_train = dataset.target

iris_X_test = iris_X_train[-40:]
iris_y_test = iris_y_train[-40:]

model = KNeighborsClassifier()

model.fit(iris_X_train, iris_y_train)

predictions = model.predict(iris_X_test)

labels = {0: "Iris- Setosa", 1: "Iris-Versicolour", 2:"Iris-Virginica"}
for i, j in zip(iris_y_test, predictions):
    print(labels[i],"  ", labels[j])
    
"""

"""
# Dry bean dataset

import pandas as pd

# df = pd.read_excel("Dry_Bean_Dataset.xlsx")
# df.to_csv("Dry_Bean_Dataset.csv")

df = pd.read_csv("Dry_Bean_Dataset.csv")

X_train = (df.drop(columns=["Class", "S.No"])).values

scaler = MinMaxScaler(feature_range=(0,1))
X_train = scaler.fit_transform(X_train)
raw_y_train = df['Class'].values

y_train = []
classes = {1: "Seker", 2: "Barbunya", 3: "Bombay", 4:"Cali", 5: "Dermason", 6: "Horoz", 7: "Sira"}
classes = {v: k-1 for k,v in classes.items()}

for item in raw_y_train:
    y_train.append(classes[(item).title()])

scaler2 = MinMaxScaler(feature_range=(0,1))
y_train = scaler2.fit_transform(y_train)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)

X_test = X_train
y_test = y_train

y_predicted = model.predict(X_test)
y_predicted = np.array([round(item) for item in y_predicted])

classes = {v: k for k,v in classes.items()}

count = 0
for test, predicted in zip(y_test, y_predicted):
    if test == predicted:
        count+=1
    
print("Accuracy : ", round((count/len(y_test))*100), "%")
"""
