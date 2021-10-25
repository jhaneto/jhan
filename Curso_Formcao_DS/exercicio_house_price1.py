import pandas as pd
import numpy as np


#Importando Data Set
data = pd.read_csv("C:\\Users\\win10\\Desktop\\python_excel\\kc_house_data.csv")

data.head()
#1. Quantas casas estão disponíveis para compra?
#Quantidade de dados da tabela
data.shape
## Ao todo são 21613 casas disponíveis para compra

#2. Quantos atributos as casas possuem? 
data.shape
# Ao todo são 21 atributos (21 colunas)

#3. Quais são os atributos das casas?
# mostra o nome das colunas
a = data.columns
a.tolist()

#Ordenar pelo campo preço
#4. Qual a casa mais cara ( casa com o maior valor de venda )?
data.sort_values('price')
#Ordenar pelo maior valor no campo preço
data[['id', 'price']].sort_values('price', ascending = False)
#R: A casa mais cara custa 7700000 e possui o ID 6762700020

#5. Qual a casa com o maior número de quartos?
data[['id', 'bedrooms']].sort_values('bedrooms', ascending=False)
#A casa com mais quartos é a de ID 2402100895

#6. Qual a soma total de quartos do conjunto de dados?
data[['bedrooms']].sum()
# A soma total é de 72854 quartos

#7. Quantas casas possuem 2 banheiros?
(data[['bathrooms']] == 2).sum()
#Um total de 1930 casas possuem 2 banheiros

#8. Qual o preço médio de todas as casas no conjunto de dados?
data[['price']].mean()
# O preço médio é de 540088.14

#9. Qual o preço médio de casas com 2 banheiros?
a = data.loc[(data['price'] > 0) & (data['bathrooms'] == 2),:]
a['price'].mean()
#R: O preço médio de casos com 2 banheiros é de 457889.71

#10. Qual o preço mínimo entre as casas com 3 quartos?
a = data.loc[(data['price'] > 0) & (data['bedrooms'] == 3), : ]
a['price'].min()
#R: O prelo mínimo é de 82000

#11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
(data['sqft_living'] > 300).sum()
# 21612 casas possuem mais de 300 m²

#12. Quantas casas tem mais de 2 andares?
(data['floors'] > 2).sum()
#R: 782 Casas possuem mais de 2 andares

#13. Quantas casas tem vista para o mar?
data['waterfront'].sum()
#R: 163 casas possuem vista para o mar

#14. Das casas com vista para o mar, quantas tem 3 quartos?
a = data.loc[(data['waterfront'] > 0) & (data['bedrooms'] == 3)]
a['waterfront'].sum()
#R: das 163 casas com vista para o mar, 64 possuem 3 quartos

#15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
a = data.loc[(data['sqft_living'] > 300) & (data['bathrooms'] > 2)]
a['bathrooms'].shape
#Quantidade  (11242,)