import numpy as np

n_album = 212
preco_pacote = 4
cromos_pacote = 4
preco_album = 10
sim_amigos = 2

def simulaAlbum():
        album = np.zeros(n_album)
        pacotes = 1
        
        while True:
             # Comprar pacote
             pacote = np.random.choice(np.arange(0, n_album), size = 4)
             pacotes += 1
             # Colar no Album
             for i in [0,1,2,3]:
                album[pacote[i]] += 1
                   
             if np.all(album >= 1):
                break
                
             custo = pacotes*preco_pacote + preco_album
        return custo

def simulaAlbum(num_amigos):
        album = np.zeros(n_album)
        pacotes = 1
       
        while True:
             # Comprar pacote
             pacote = np.random.choice(np.arange(0, n_album), size = 4)
             pacotes += 1
             # Colar no Album
             for i in [0,1,2,3]:
                album[pacote[i]] += 1
                   
             if np.all(album >= num_amigos):
                break
                
             custo = pacotes*preco_pacote + preco_album
        return custo/num_amigos

import timeit


S = 10000

resultados = []

inicio = timeit.default_timer()
for i in range(S):
        pessoa = simulaAlbum()
        resultados.append(pessoa)
        print(resultados)
        if i % 2 == 0:
            print(i)
            
            
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
            
todos = np.array(resultados) 
print(todos) 


sim = np.array(resultados).mean()
print(sim)
print(max(resultados))
print(min(resultados))
total = sim / 4
print(total)
 
import matplotlib.pyplot as plt

def grafico():
    plt.hist(todos, bins= 20, density = True, color = 'royalblue', edgecolor='black')
    plt.title('Distribuição Empirica do valor Gasto para Completar o Album')
    plt.show()


def probabilidade():
    prob1 = sum(np.array(todos)< 1500)/S
    prob2 = sum(np.array(todos) > np.array(todos).mean())/S 
    print(prob1)
    print(prob2)
    qts = np.quantile(todos, [0.025, 0.975])
    print(qts)


def graficosAmigos(simulacao):
    minimo_possivel = math.ceil(n_album/cromos_pacote)*preco_pacote
    plt.figure(figsize(18, 6))
    plt.bar(simulacao[0], simulacao[1], with = 0.5, color = 'royalblue')
    plt.xticks(simulacao[0])
    plt.axhline(y = minimo_possivel, linestyle = 'dashed', color = 'blue')
    plt.title('Custo médio aproximado para \n completar o album em função do tamanho\n do numero de amigos')
    ply.show()
    
    
    
grficosAmigos(sim_amigos)