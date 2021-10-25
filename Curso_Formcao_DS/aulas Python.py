lista  = []
lista = range(10)
  
for y in lista:
       print(lista[y])
       
       
       
class Pessoa:
   def __init__(self, nome, idade):
              self.nome = nome
              self.idade = idade
              
   def getNome(self):    
      return self.nome 
  
   def getIdade(self):      
      return self.idade 
  
   def setNome(self, nome):
       self.nome = nome
       
   def setIdade(self, idade):
       self.idade = idade

p = Pessoa("",0)
input('Escreva o Nome:')
p.setNome()
print(p.getNome())     


pares = [num for num in range(101) if (num % 2 ==0)]
print(pares)

    def pot(x):
     return x**2

print(pot(2))

#função lambda 

pot1 = lambda x: x**2
print(pot1(10))

def fat(x):
    if(x == 0):
     return 1
    return (x * fat(x - 1))

print(fat(5))    

fat_ = lambda n: n * fat(n - 1) if n > 1 else 1

print(fat_(5))

#funcao MAP
lista = [1,2,3,4]
m = map(lambda x : x ** 2, lista)

for i in m:
     print(i)
# funcao reduce

import  functools
print(functools.reduce(lambda x,y: x+y, [1,2,3,4]))   

#funcao filter

f = filter(lambda x: x%2 == 0, range(10))
for i in f:
       print(i)
       
#fibonacci

def fib(n):
   if(n == 1 or n == 2):
      return 1
   return fib(n - 1)+ fib(n - 2)
print(fib(5))       

def potbase(base, exp):
   if(exp == 0):
       return 1
   return base * potbase(base, exp - 1)

print(potbase(10, 2))


