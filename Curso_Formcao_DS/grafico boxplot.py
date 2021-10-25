import pandas as pd 
import matplotlib.pyplot as plt

base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\trees.csv')



plt.boxplot(base.Volume, vert = False, showfliers= False, notch = True,
            patch_artist=True)
plt.title('Arvores')
plt.xlabel('Volume')


#colorir

plt.boxplot(base)

plt.boxplot(base.Volume, vert = False)
plt.boxplot(base.Girth, vert = False)
plt.boxplot(base.Height, vert = False)

