import pandas as pd 
import matplotlib.pyplot as plt

base = pd.read_csv('C:\\Users\\win10\\Desktop\\python_excel\\Formacao DC\\download\\FormaçãoCD2\\13.Prática em Python\\dados\\trees.csv')


plt.figure(1)

#girth com volume
plt.subplot(2, 2, 1)
plt.scatter(base.Girth, base.Volume)

#girth com height
plt.subplot(2, 2, 2)
plt.scatter(base.Girth, base.Volume)

#height com volume
plt.subplot(2, 2, 3)
plt.scatter(base.Girth, base.Volume)

#histograma do volume
plt.subplot(2, 2, 4)
plt.scatter(base.Girth, base.Volume)