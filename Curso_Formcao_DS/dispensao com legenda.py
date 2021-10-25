import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\co2.csv')
x = base.conc
y = base.uptake

unicos = list(set(base.Treatment))


for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label = unicos[i])
    
plt.legend(loc = 'lower right')    



