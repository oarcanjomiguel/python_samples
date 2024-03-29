#Exercício 1 - Distância entre dois pontos
#Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, 
#às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, 
#às coordenadas x e y de um outro ponto no mesmo plano.
#Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
#longe
#na saída. Caso o contrário, quando a distância for menor que 10, imprima
#perto
import math

x1 = int(input("Digite a coordenada x do ponto 1: "))
y1 = int(input("Digite a coordenada y do ponto 1: "))
x2 = int(input("Digite a coordenada x do ponto 2: "))
y2 = int(input("Digite a coordenada y do ponto 2: "))

if (x1 >= x2):
	deltaX = x1 - x2
else:
	deltaX = x2 - x1

if(y1 >= y2):
	deltaY = y1 - y2
else:
	deltaY = y2 - y1

distancia = math.sqrt(deltaX**2 + deltaY**2)

if(distancia >= 10.0):
	print("longe")
else:
	print("perto")
print(distancia)
