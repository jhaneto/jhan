import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\Credit2.csv', sep = ";")

X = dataset.iloc[:,1:10].values
y = dataset.iloc[:,10].values


labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:,0])

onehotencoder = make_column_transformer((OneHotEncoder(categories='auto', sparse=False),[1]), remainder = 'passthrough')
X = onehotencoder.fit_transform(X)

X = X[:,1:]

labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test  = sc.transform(X_test) 

classifier = Sequential()
classifier.add(Dense(units= 6, kernel_initializer = 'uniform', activation = 'relu', input_dim= 12))
classifier.add(Dense(units= 6, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units= 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.fit(X_train, y_train, batch_size=10, epochs = 100)

y_pred = classifier.predict(X_test)

y_pred = (y_pred > 0.5)


cm = confusion_matrix(y_test, y_pred)
