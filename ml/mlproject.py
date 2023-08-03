import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score


def split_train_test(data, test_ratio):
    # ye value isliye le gyi h kyuki permutation wale function me kbhi na kbhi sare data points aa jaege (test data me ) toh overfitting ke chance jyada h , seeding se nhi  hoga
    np.random.seed(42)
    # Jo length rhega data ka uski random permutation me uski indices ko shuffle krdega
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data)*test_ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


def print_scores(scores):
    print("Scores :", scores)
    print("Mean:", scores.mean())
    print("Std:", scores.std())


housing = pd.read_csv("Data.csv")

print(housing.info())
print("\n")

print(housing['CHAS'].value_counts())
print("\n")
print(housing.describe())
print("\n")
housing.hist(bins=50, figsize=(20, 15))
plt.show()
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
print(f"Rows in train set:{len(train_set)} \nRows in test set:{len(test_set)}")

print("\n")
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['CHAS']):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]


print(strat_train_set.info())
print("\n")

print(strat_test_set['CHAS'].value_counts())

print("\n")

housing = strat_train_set.copy()
corr_matrix = housing.corr()
print(corr_matrix['MEDV'].sort_values(ascending=False))
print("\n")
attribute = ["MEDV", "RM", "LSTAT", "ZN "]
print(scatter_matrix(housing[attribute], figsize=(12, 8)))
# outliers hta skte h isse corr matrix se
housing.plot(kind="scatter", x="RM", y="MEDV", alpha=0.8)
housing['TAXRM'] = housing['TAX']/housing['RM']

print(housing.head())
print(corr_matrix['MEDV'].sort_values(ascending=False))
print("\n")
housing.plot(kind="scatter", x="TAXRM", y="MEDV", alpha=0.8)
housing = strat_train_set.drop("MEDV", axis=1)  # droping the label
housing_labels = strat_train_set["MEDV"].copy()
imputer = SimpleImputer(strategy="median")
imputer.fit(housing)
print(imputer.statistics_)
print("\n")
X = imputer.transform(housing)
housing_tr = pd.DataFrame(X, columns=housing.columns)
my_pipeline = Pipeline([  # u can add many
    ('imputer', SimpleImputer(strategy="median")),
    ('std_scaler', StandardScaler())
])
# ye ek numpy array h,predictor array lega input me
housing_num_tr = my_pipeline.fit_transform(housing)

model = RandomForestRegressor()
model.fit(housing_num_tr, housing_labels)
some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[:5]
prepared_data = my_pipeline.transform(some_data)
print(model.predict(prepared_data))
list(some_labels)
housing_predictions = model.predict(housing_num_tr)
mse = mean_squared_error(housing_labels, housing_predictions)
rmse = np.sqrt(mse)
scores = cross_val_score(
    model, housing_num_tr, housing_labels, scoring="neg_mean_squared_error", cv=10)
rmse_scores = np.sqrt(-scores)
print_scores(rmse_scores)
