import pandas as pd

# O parâmetro encoding indica que os dados estão em português
# Mais detalhes em https://docs.python.org/3/library/codecs.html#standard-encodings
base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\Credito.csv', sep = ';', encoding = 'cp860')

# Criação da variável X que presenta os atributos previsores
X = base.iloc[:, 0:19].values

# Criação da variável y que contém as respostas
y = base.iloc[:, 19].values

# Transformação dos atributos categóricos no formato string para números
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])
X[:, 2] = labelencoder.fit_transform(X[:, 2])
X[:, 3] = labelencoder.fit_transform(X[:, 3])
X[:, 5] = labelencoder.fit_transform(X[:, 5])
X[:, 6] = labelencoder.fit_transform(X[:, 6])
X[:, 8] = labelencoder.fit_transform(X[:, 8])
X[:, 9] = labelencoder.fit_transform(X[:, 9])
X[:, 11] = labelencoder.fit_transform(X[:, 11])
X[:, 13] = labelencoder.fit_transform(X[:, 13])
X[:, 14] = labelencoder.fit_transform(X[:, 14])
X[:, 16] = labelencoder.fit_transform(X[:, 16])
X[:, 18] = labelencoder.fit_transform(X[:, 18])

# Divisão da base em treino e teste (70% para treinamento e 30% para teste)
from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, 
                                                                  test_size=0.3,
                                                                  random_state=0)

from sklearn.neighbors import KNeighborsClassifier #classificador
knn = KNeighborsClassifier()
knn.fit(X_treinamento, y_treinamento)
#y_teste = labelencoder.fit_transform( y_teste)
#resultado_knn = knn.predict(y_teste)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                     metric_params=None, n_jobs=None, n_neighbors=5, p=2,
                     weights='uniform')

#Calculando a matriz de confusão
resultado_knn = knn.predict(X_teste)
print (pd.crosstab(y_teste,resultado_knn, rownames=['Real'], colnames=['Predito'], margins=True))

from sklearn.metrics import accuracy_score #acuracia

# Acurácia
resultado_knn = labelencoder.fit_transform( resultado_knn)
acuracia = accuracy_score(y_teste, resultado_knn)
erro = 1 - acuracia
print('Acurácia: %f' % acuracia)
print('Erro: %f' % erro)
# Conseguimos uma taxa de erro de 32%

# Precision
from sklearn.metrics import precision_score #precision
precision = precision_score(y_teste, resultado_knn)
print('Precision: %f' % precision)
