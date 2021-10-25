import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\trees.csv')

sns.distplot(base.Volume, bins = 10, axlabel = 'Volume').set_title('Arvores')

base2 = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\chicken.csv')

agrupado = base2.groupby(['feed'])['weight'].sum()

teste = base2.loc[base2['feed'] == 'horsebean']

plt.figure()
plt.subplot(3,2,1)
sns.distplot(base2.loc[base2['feed'] == 'horsebean'].weight).set_title('horsebean')

plt.subplot(3,2,2)
sns.distplot(base2.loc[base2['feed'] == 'casein'].weight).set_title('casien')

plt.subplot(3,2,3)
sns.distplot(base2.loc[base2['feed'] == 'linseed'].weight).set_title('linseed')

plt.subplot(3,2,4)
sns.distplot(base2.loc[base2['feed'] == 'meanmeal'].weight).set_title('meanmeal')

plt.subplot(3,2,5)
sns.distplot(base2.loc[base2['feed'] == 'soybean'].weight).set_title('soybean')

plt.subplot(3,2,6)
sns.distplot(base2.loc[base2['feed'] == 'sunflower'].weight).set_title('sunflower')
plt.tight_layout()