import pandas as pd

valores = np.random.uniform(0, 10, 20).reshape(5, 4).round(1)
valores

nomes = ['Alice', 'Bruno', 'Carol', 'David', 'Emily']
testes = ['P1', 'P2', 'P3', 'P4']

provas = pd.DataFrame(valores, columns = testes, index = nomes)
provas

provas.transpose()

dicionario = {'Alice': np.random.uniform(5, 10, 4).round(1),
              'Bruno': np.random.uniform(0, 7, 4).round(1),
              'Carol': np.random.uniform(3, 7, 4).round(1),
              'David': np.random.uniform(0, 10, 4).round(1),
              'Emily': np.random.uniform(1, 10, 4).round(1),
              'Fabio': np.random.uniform(1, 10, 4).round(1),
              'Gloria': np.random.uniform(1, 10, 4).round(1)}

provas = pd.DataFrame(dicionario)

provas.index = ['P1', 'P2', 'P3', 'P4']

provas

provas = provas.transpose()

