import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\trees.csv')

h =  np.histogram(base.iloc[:,1], bins= 2)

plt.hist(base.iloc[:,1], bins = 6)
plt.title('Arvores')
plt.ylabel('Frequencia')
plt.xlabel('Altura')