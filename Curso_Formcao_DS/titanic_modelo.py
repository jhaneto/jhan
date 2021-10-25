#importação da bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
#Carregar o Dataset do arquivo csv no pandas
df_treino = pd.read_csv("C:\\Users\\win10\\Desktop\\python_excel\\train_titanic.csv")
#Visualisar Dados
df_treino.head()
#Visualisar quantidade de colunas e linhas
df_treino.shape
#Visulisar os tipos de campos 
df_treino.dtypes
#Calculo de total de mulheres que sobreviveram 
mulheres = df_treino.loc[df_treino.Sex == 'female']['Survived']
taxa_mulheres = sum(mulheres)/len(mulheres)
#mostrar o resultado de mulheres sobreviventes
print("% de mulheres que sobreviveram: ", taxa_mulheres)
#Metodo len mostra a quantidade
len(mulheres)
#Metodo sum mostra a soma 
sum(mulheres)
#Calculo de total de homens que sobreviveram 
homens = df_treino.loc[df_treino.Sex == 'male']['Survived']
taxa_homens = sum(homens)/len(homens)
#mostrar o resultado de homens sobreviventes
print("% de Homens que sobreviveram: ", taxa_homens)
#Metodo len mostra a quantidade
len(homens)
#Metodo sum mostra a soma 
sum(homens)
#Mostra os vamores de mulheres e homens 
df_treino['Sex'].value_counts()
#Mostra num grafico o total de passageiros pelo genero
fig, ax = plt.subplots(figsize =(10,6))
sns.countplot(x = "Sex", data = df_treino)
plt.title('Total de Passageiros por Sexo')
#Mostra num grafico o total de passageiros pelo genero que sobreviveram
plt.figure(figsize = (10,6))
sns.countplot(data = df_treino, x = 'Sex', hue = 'Survived', palette = 'viridis')
plt.title('Genero')
plt.show()
#Mostra um histograma pela idade dos passageiros
df_treino['Age'].hist(bins = 30);
df_treino['Pclass'].hist(by = df_treino['Survived'])
#Calcula as o numero de crianças menores de 10 anos que sobreviveram
criancas = df_treino.loc[df_treino.Age <= 10]['Survived']
criancas
#Mostra a correlação dos campos 
corelacao = df_treino.corr()
#mostra um grafico de correlações dos campos 
sns.heatmap(df_treino.corr(), vmax = 1.0, annot = True)
#Transforma o campo generos em fator binario(0,1)
df_treino['Sex'] = df_treino["Sex"].map({'male': 0, 'female': 1})
#Mostra os campos 
df_treino.head()

#Verificar valores nulos
df_treino.isnull().sum()
#Mostra a descrição de cada campo do DataSet
df_treino.describe()
#Apaga os valores nulos da coluna Anos(Age)
df_treino = df_treino.dropna(subset = ["Age"])
#Preencher os dados NaN por valores sem dropar os campos vazios
#values = {'Age': df.Age.mode()[0], 'Cabin': 'SC', 'Embarked': df.Embarked.mode()[0]}
#values
# Atribuido os novos valores
#df.fillna(value=values, inplace=True)
#Remover os espaços em branco no começo ou fim 
#df.Name.str.rstrip().head()
#Transformar os nomes em maiusculo(upper()) o minusculo(lower())
#df.Name.str.upper().head()
#Função para tirar parentese das palavras
#def remove_parenteses(item):
#  if '(' in item:
#    return item.replace('(','').replace(')','')
#  else:
#    return item
#df.Name.head(10).apply(remove_parenteses)

#Queremos ver os 5 primeiros passageiros que tem ‘Mr’ no nome.
#biblioteca de expressao regulares
#import re
#df.loc[df.Name.str.contains('Mr', flags=re.I, regex=True)].head()
df1 = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
#Use chunksize para dividir o processamento por quantidade de linhas.
#Passamos para o parâmetro chunksize o número de linhas a serem lidas por vez, dividindo o nosso conjunto em várias partes menores. O parâmetro nos retorna um objeto iterável de n-partes.
#df = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
#for d in pd.read_csv(df, chunksize=200):
#  print ("Chunk")
#  print(d.count())
#Classificando por faixa - etaria
import sys
df1['ageGroup']=pd.cut(
   df1['Age'],
   bins=[0, 13, 19, 61, sys.maxsize],
   labels=['<12', 'Teen', 'Adult', 'Older']
)
df1['Age', 'Sex', 'ageGroup']
df1.info()
# Convertendo os tipos de dados
df1.Sex = df1.Sex.astype('category')
df1['Sex']
de = df1['Sex' == 'male'] = 0 
de

df_treino.shape

#seleciona as  features para o nosso modelo
X = df_treino.drop(columns=["PassengerId", "Survived", "Name", "Ticket", "Embarked", "Cabin"])
y = df_treino["Survived"]

X.head()
y.head()

#Divindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#Verificando a forma dos dados 
X_train.shape, X_test.shape

y_train.shape, y_test.shape

#instanciado o objeto classificador
random_clf = RandomForestClassifier()

#Treinando o modelo
random_clf.fit(X_train, y_train)

resultado = random_clf.predict(X_test)

resultado

y_test
#Biblioteca de metricas para acuracia do treinamento
from sklearn import metrics
print(metrics.classification_report(y_test, resultado))
#Feature(caracteristicas) mais importantes para o modelo
random_clf.feature_importances_
#Mostra a importancia dos campos pro modelo 
feature_imp = pd.Series(random_clf.feature_importances_, index = X_train.columns).sort_values(ascending=False)
feature_imp
#Cria um grafico com a importancia dos campos pro modelo 
def visualiza_features_importantes(features_lista):
    %matplotlib inline
    plt.figure(figsize=(16,8))
    sns.barplot(x=features_lista, y=features_lista.index)
    
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.title('Visualizing Important Features')
    plt.show()
    
visualiza_features_importantes(feature_imp)

#selecionando uma arvore da floresta
tree0 = random_clf.estimators_[0]

from sklearn.tree import export_graphviz
import graphviz

dot_data = export_graphviz(
           tree0,
           max_depth=3,
           out_file = None,
           feature_names=X_train.columns,
           class_names=['0','1'],
           filled=True, rounded=True,
           proportion=True,
           node_ids=True,
           rotate=False,
           label='all',
           special_characters=True
    )
graph = graphviz.Source(dot_data)
graph

X_test

df_treino['Pclass'].unique()

teste = np.array([[2,1,28,0,0,7.2250]])

teste
resultado1 = random_clf.predict(teste)
resultado1