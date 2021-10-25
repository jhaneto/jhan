from math import sqrt
print("---------------------Valore de Delta-------------------------")
a1 = input("Digite o valor de A:")
b1 = input("Digite o valor de B:")
c1 = input("Digite o valor de C:")




def funcDelta(a,b,c): 
   delta = b**2 - 4*a*c
   raiz_delta = sqrt(delta)
   x1 = (-b + raiz_delta)/2*a
   x2 = (-b - raiz_delta)/2*a
   
   return print("X1: {0} e X2: {1}".format(x1,x2)  )



if(a1 == ''  or b1 == '' or c1 == ''):
  print("Não pode conter valor nulo")
else:
  x = float(a1)
  y = float(b1)
  z = float(c1)
  funcDelta(x,y,z)


lista =range(10)

def pares(x):
    if(x % 2 == 0):
     return  print("par :",x)
    return  print("impar :",x)

pares(3)


listaOrd = [70,22,1, 9, 76, 0, 3, 1,93]

def selection_sort(lista):
    
    for i in range(len(lista)):    
        menor = i
        for j in range(i+1,len(lista)):
           
           if lista[j] < lista[menor]:
               menor = j
        if lista[i] != lista[menor]:       
         aux = lista[i]
         lista[i] = lista[menor]
         lista[menor] = aux   
         
    print(lista)
   
selection_sort(listaOrd)   


listas = sorted(listaOrd)
print(listas)

if 100 in listaOrd:
    print("22 na lista")


del listas[2]

print(listas)