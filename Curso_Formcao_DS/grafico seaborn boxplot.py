import pandas as pd
import seaborn as sns


base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\trees.csv')

sns.boxplot(base.Volume).set_title('Arvores')

sns.boxplot(data = base)