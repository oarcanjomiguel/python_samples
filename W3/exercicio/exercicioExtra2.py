#Exercício 2 - Desafio da videoaula
#Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
#O programa deve receber os parâmetros a, b, e c da equação ax^2 + bx + c, respectivamente, e imprimir o resultado na saída da seguinte maneira:
#Quando não houver raízes reais imprima:
#esta equação não possui raízes reais
#Quando houver apenas uma raiz real imprima:
#a raiz desta equação é X
#onde X é o valor da raiz
#Quando houver duas raízes reais imprima:
#as raízes da equação são X e Y
#onde X e Y são os valor das raízes.
#Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente, ou seja, X deve ser menor que Y.

import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4*a*c

if(delta < 0):
	print("esta equação não possui raízes reais")
else:
	x1 = (-1*b+math.sqrt(delta))/(2*a)
	if(delta == 0):
		print("a raiz desta equação é",x1)
	else:
		x2 = (-1*b-math.sqrt(delta))/(2*a)
		if(x2<x1):
			aux = x1
			x1 = x2
			x2 = aux
		print("as raízes da equação são", x1, "e", x2)