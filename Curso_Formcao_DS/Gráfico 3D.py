import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\orchard.csv')

figura = plt.figure()

eixo = figura.add_subplot(1,1,1, projection = '3d')

eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_xlabel('decrease')
 psycopeixo.set_label('rowpos')
eixo.set_zlabel('colpos')
