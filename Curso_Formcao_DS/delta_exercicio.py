
a,b,c = 1, 2, 1

 def deltas(x,y,z):
   delta = b**2 - 4*a*c

   if delta > 0:
    x1 = round((-b + delta**(1/2))/(2*a),3)
    x2 = round((-b - delta**(1/2))/(2*a),3)
    print('As raízes são {} e {}'.format(x1, x2))
   elif delta == 0:
    x =  round(-b /(2*a),3)
    print('A raíz é {}'.format(x))
   else:
    print("A equação não possui raizes reais")  

    
deltas(a,b,c)   

lista = ['Ricardo', 34]