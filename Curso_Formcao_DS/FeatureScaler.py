import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


dataset = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\Credit.csv')

dt = dataset.iloc[:,[1,4,7]].values

sc = StandardScaler()

x = sc.fit_transform(dt)

sc = MinMaxScaler()
y = sc.fit_transform(dt)

