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

# Criação do classificador Random Forest
from sklearn.ensemble import RandomForestClassifier
floresta = RandomForestClassifier(n_estimators = 100)
floresta.fit(X_treinamento, y_treinamento)

# Previsões
previsoes = floresta.predict(X_teste)

from sklearn.metrics import confusion_matrix, accuracy_score

print (pd.crosstab(y_teste,previsoes, rownames=['Real'], colnames=['Predito'], margins=True))
print(confusion_matrix(y_teste, previsoes))
matriz = confusion_matrix(y_teste, previsoes)

acuracia = accuracy_score(y_teste, previsoes)
erro = 1 - acuracia
print('Acurácia: %f' % acuracia)
print('Erro: %f' % erro)

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

# Conseguimos uma taxa de erro de 22%
from sklearn.metrics import precision_score #precision
y_teste = labelencoder.fit_transform(y_teste)
precision = precision_score(y_teste, previsoes)
print('Precision: %f' % precision)

# Recall
from sklearn.metrics import recall_score #recall
recall = recall_score(y_teste, previsoes)
print('Recall: %f' % recall)

# F1-Score
from sklearn.metrics import f1_score #f1-score
f1 = f1_score(y_teste, previsoes)
print('F1-Score: %f' % f1)
