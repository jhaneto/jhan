import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer


dataset = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\Credit.csv')

X = dataset.iloc[:,8:10].values

labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:,0])

onehotencoder = make_column_transformer((OneHotEncoder(categories='auto',
                                                     sparse=False),
                                                     [1]), remainder="passthrough")

X = onehotencoder.fit_transform(X)