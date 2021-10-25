import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\trees.csv')

plt.scatter(base.Girth, base.Volume, color = 'blue', facecolors = 'none', marker = '*')
plt.title('Arvores')
plt.xlabel('Volume')
plt.ylabel('Circunferencia')


plt.plot(base.Girth, base.Volume)

sns.regplot(base.Girth, base.Volume, data = base)


sns.regplot(base.Girth, base.Volume, data = base, x_jitter = 0.3,fit_reg = False)
