from sklearn import datasets
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.utils import np_utils
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import confusion_matrix

base = datasets.load_iris()

previsoes = base.data
classe = base.target

classe_dummy = np_utils.to_categorical(classe)

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsoes,
                                                                  classe_dummy,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

modelo = Sequential()
modelo.add(Dense(units = 5, input_dim = 4))
modelo.add(Dense(units = 4))
modelo.add(Dense(units = 3, activation = 'softmax'))

modelo.summary()

from keras.utils.vis_utils import plot_model

modelo.compile(optimizer = 'adam', loss = 'categorical_crossentropy', 
               metrics = ['accuracy'])
modelo.fit(X_treinamento, y_treinamento, epochs = 1000, 
           validation_data = (X_teste, y_teste))

previsoes = modelo.predict(X_teste)
previsoes = (previsoes > 0.5)



y_teste_matriz = [np.argmax(t) for t in y_teste]
y_previsoes_matriz = [np.argmax(t) for t in previsoes]

confusao = confusion_matrix(y_teste_matriz, y_previsoes_matriz)
