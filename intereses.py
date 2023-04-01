#Interes compuesto al 5%

import math


C=int(input("Digite el valor de C: "))
n= 0
D= 2*C

while(C<D):
    C = C+0.05*C
    n= n+1
    print("i="+str(n))
    print("Suma="+str(D))


print("La suma es: " + str(n))