import pandas as pd
import pandas_profiling
import plotly.express as px
import numpy as np

#Solicitações do CEO

df = pd.read_csv("C:\\Users\\win10\\Desktop\\python_excel\\kc_house_data.csv")

#1. Qual a data do imóvel mais antigo no portfólio?
df['date'] = pd.to_datetime(df['date'])
df[['id', 'yr_built']].sort_values('yr_built')
#R: A data mais antiga é 1900

#2. Quantos imóveis possuem o número máximo de andares (3.5)?
df[df['floors'] == 3.5].shape
# 8 imóveis possuem 3.5 andares

#3. Criar uma classificação para os imóveis, separando-os em baixo e alto padrã o de acordo com o preço
#acima de 540.000 = alto padrão
#Abaixo de 540.00 = baixo padrão

#Sem estutura de controle

df1 = pd.read_csv("C:\\Users\\win10\\Desktop\\python_excel\\kc_house_data.csv")

pandas_profiling.ProfileReport(df1)

df1['padrao'] =  'baixo'

df1.loc[df['price'] >= 540000, 'padrao'] = 'alto'
df1[['id', 'price' , 'padrao']]
df1[df1['padrao']=='alto']
df1.groupby(by='padrao').size()
df1.groupby(by='padrao')['price'].mean()
df1.groupby(['padrao']).agg({'price': np.mean, 'id': np.size})
df1.isnull().sum()
df1.padrao.mode()
#Utilizando estruturas de controle

# for i in range(len(df)):
#     if (df1.loc[i,'price'] >= 540000):
#         df1.loc[i, 'padrao'] = 'alto_padrao'
#     else:
#         df1.loc[i, 'padrao'] = 'baixo_padrao'

#4. Fazer um relatório ordenado pelo preço e contendo as seguintes informações:
#Id do imóvel
#Data que o imóvel ficou disponível para compra
#O número de quartos
#O tamanho total do terreno
#O preço
#A classificação do imóvel (alto e baixo padrão)

df1[['price','id', 'date', 'bedrooms', 'sqft_lot', 'padrao']].sort_values('price', ascending = False).head()

#5. Criar um mapa indicando onde as casas estão localizadas geograficamente
data_map = df1[['id', 'lat', 'long', 'price', 'condition']]
mapa = px.scatter_mapbox(data_map, lat = 'lat', lon = 'long', hover_name = 'id', hover_data = ['price'] ,
                  height = 300 , zoom = 10, color = 'condition', size = 'price')
mapa.update_layout (mapbox_style = 'open-street-map')
mapa.update_layout(height = 600, margin = {'r':0,'t':0,'l':0,'b':0} )

#Perguntas do CEO
df2 = pd.read_csv("C:\\Users\\win10\\Desktop\\python_excel\\kc_house_data.csv")

df2.info()
df2.index
df2.mean()
df2.median()
a = df2.columns
a.tolist()
df2.groupby(by='padrao').size()
#Aplicando uma função que substitui a por b
#df2.apply(lambda x: x.replace('a', 'b'))

df2[df2['floors'] == 3.5]

#1. Crie um anova coluna chamada: "house_age" ==
#Se o valor da coluna "date" for maior que 2014-01-01 => 'new_house
#Se o valor da coluna "date" for menor que 2014-01-01 => 'old_house


df2['date'] = pd.to_datetime(df2['date'])

#sem condicional

df2['house_age'] = 'new_house'
df2.loc[df2['date'] < '2014-01-01', 'house_age'] = 'old_house'


#df2.query('house_age == new_house').head()
#df2.query('date < "2014-01-01"').head(10)
#df2.select_dtypes(include=['object'])
#df2.select_dtypes(include=['float'])
#df.groupby(by='Sex').size()
#df.groupby(by='Sex')['Age'].mean()

#Um outro exemplo um pouco mais complexo. Agora vamos ver qual foi a 
#média de idade e a quantidade de passageiros que sobreviveram 
#e que não sobreviveram por sexo.

#df.groupby(['Sex','Survived']).agg({'Age': np.mean, 'PassengerId': np.size})
#Podemos visualizar esses valores com o método isnull().sum(), 
#que retorna a soma dos valores nulos encontrados por coluna.

#df.isnull().sum()
#Vamos preencher os valores faltantes da coluna ‘Age’
# e da coluna ‘Embarked’ com a moda (valor que mais 
#se repete em cada uma dessas colunas). Para coluna ‘Cabin’, vamos substituir todos os valores faltantes pela sigla SC (Sem Cabine).

#values = {'Age': df.Age.mode()[0], 'Cabin': 'SC', 'Embarked': df.Embarked.mode()[0]}

# Atribuido os novos valores
#df.fillna(value=values, inplace=True)
#df.isnull().sum()

d = df2.loc[(df2['house_age'] == 'old_house')]
d['house_age']

#com condicionar 
# for i in range(len(df)):
#     if (df2.loc[i, 'date'] > 2014-01-01):
#         df2.loc[i, 'house_age'] = 'casa_nova'
#     else:
#         df2.loc[i, 'house_age'] = 'casa_velha'

#2. Crie uma nova coluna chamada: "dormitory_type"
#Se o valor da coluna "bedrooms" for igual à 1 => 'studio'
#Se o valor da coluna "bedrooms" for igual à 2 => 'apartament'
#Se o valor da coluna "bedrooms" for maior que 2 => 'house'

#sem estrutura de controle

df2['dormitory_type'] = 'house'

df2.loc[df['bedrooms'] == 1, 'dormitory_type'] = 'studio'
df2.loc[df['bedrooms'] == 2, 'dormitory_type'] = 'apartament'

df2['dormitory_type'].unique()

#com estrutura de controle

# for i in range(len(df)):
#     if (df2.loc[i, 'bedrooms'] == 1):
#         df2.loc[i, 'dormitory_type'] = 'studio'
        
#     elif (df2.loc[i, 'bedrooms'] == 2):
#          df2.loc[i, 'dormitory_type'] = 'apartament'
            
#     else:
#         df2.loc[i, 'dormitory_type'] = 'house'

# df2['dormitory_type'].unique()
#  array(['house', 'apartament', 'studio'], dtype=object)

#3. Crie uma nova coluna chamada: "condition_type"
#Se o valor da coluna "condition" for menor ou igual à 2 => 'bad'
#Se o valor da coluna "condition" for igual à 3 ou 4 => 'regular'
#Se o valor da coluna "condition" for igual à 5 => 'good'

#sem estrutura de controle
df2['condition_type'] = 'bad'
df2.loc[(df2['condition'] == 3) | (df2['condition'] == 4), 'condition_type'] = 'regular'
df2.loc[df2['condition'] == 5, 'condition_type'] = 'good'       
df2['condition_type'].unique()
#array(['regular', 'good', 'bad'], dtype=object)

#4. Modifique o TIPO da coluna "condition" para STRING
df2['condition'] = df2['condition'].astype(str)

#5. Delete as colunas "sqft_living15" e "sqft_lot15"
df2 = df2.drop(['sqft_living15', 'sqft_lot15'], axis = 1)
#(21613, 20)

#6. Modifique o TIPO da coluna "yr_build" para DATE
df2['yr_built'] = pd.to_datetime(df2['date'])

#7. Modifique o TIPO da coluna "yr_renovated" para DATE
df2['yr_renovated'] = pd.to_datetime(df2['date'])

#8. Qual a data mais antiga de construção de um imóvel?
df2[['yr_built', 'id']].sort_values('yr_built', ascending = True)
#Outra forma 
#df2['yr_built'].min()

#9. Qual a data mais antiga de renovação de um imóvel?
df2[['yr_renovated', 'id']].sort_values('yr_renovated')
#outra forma
# df2['yr_renovated'].min()

#10. Quantos imóveis tem 2 andares?
df2[df2['floors'] == 2].shape
# R: 8241 imoveis (8241, 20)

#11. Quantos imóveis estão com a condição igual à "regular"?
df2[df2['condition_type'] == 'regular'].shape
# R: 19710 (19710, 20)

#12. Quantos imóveis estão com a condição igual a "bad" e possuem "vista para água"?
df2[(df2['condition_type'] ==  'bad') & (df2['waterfront'] == 1)].shape
#R: 2 (2, 20)

#13. Quantos imóveis estão com a condição igual a "good" e são "new_house"?
df2[(df2['condition_type'] == 'good') & (df2['house_age'] == 'new_house')].shape
#R: 1701

#14. Qual o valor do imóvel mais caro do tipo "studio"?
df2[(df2['dormitory_type'] == 'studio')].sort_values('price', ascending = False)
#1247000  (199 rows × 22 columns)

#15. Quantos imóveis do tipo "apartament" foram reformados em 2015?
df2[(df2['house_age'] == 'new_house') & (df2['yr_renovated'] == 2015)]

#16. Qual o maior número de quartos que um imóvel do tipo "house" possui?
df2[(df2['dormitory_type'] == 'house')].sort_values('bedrooms', ascending = False)
# r: 33

#17. Quandos imóveis "new_house" foram reformados no ano de 2014?
df2[(df2['house_age'] == 'new_house') & (df2['yr_renovated'] == 2014)]
#R: 91 imóveis

#18. Selecione as colunas: "id = 0", "date = 1", "price = 2", "floors" = 7, "zipcode = 16" pelo método:
#Direto pelo nome das colunas
#Pelos índices
#Pelos índices das linhas e o nome das colunas
#Índices booleanos

#nome das colunas
#df2[['id', 'date', 'price', 'floors', 'zipcode']]

    #índices
#df2.iloc[:, [0,1,2,7,16]]

    #indices das linhas e nome das colunas
#df2.loc[:,['id', 'date', 'price', 'floors', 'zipcode']]
    
   #indices boleanos
col = [True, True, True, False, False, False, False, True, False, False, False, False,
       False, False, False, False, True, False, False, False, False, False]
df2.loc[:, col]

#19. Salve um arquivo .csv com somente as colunas do item 10
a = df2[['id', 'zipcode', 'floors', 'price']]
a.to_csv("C:\\Users\\win10\\Desktop\\python_excel\\novo_home_price.csv", index = False)

#20. Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"
data_map = df2[['lat', 'long', 'id', 'price', 'condition']]
mapa = px.scatter_mapbox(data_map, lat = 'lat', lon = 'long', hover_data = ['price'],
                         hover_name = 'id', size = 'price', color_discrete_sequence = ['green'], height = 300 , zoom = 10)
mapa.update_layout(mapbox_style = 'open-street-map')
mapa.update_layout(height = 600, margin = {'r':0,'t':0,'l':0,'b':0} )
mapa.show()


