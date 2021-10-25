import pandas as pd 


base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\insect.csv')

agrupado = base.groupby(['spray'])['count']. sum()

agrupado.plot.bar(color = 'gray')

agrupado.plot.pie(legend = True)