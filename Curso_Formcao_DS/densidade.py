import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\trees.csv')

plt.hist(base.iloc[:,1], bins = 10)

sns.distplot(base.iloc[:,1], hist = True, kde=True, bins = 6, color = 'blue',
            hist_kws = {'edgecolor' : 'black'})