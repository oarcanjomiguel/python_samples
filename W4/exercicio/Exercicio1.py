#Exercício 1
#Escreva um programa que receba um número natural n n na entrada e imprima n! (fatorial) na saída.
#Exemplo:
#Digite o valor de n: 5
#120
#Dica: lembre-se que o fatorial de 0 vale 1!

n = int(input("Digite o valor de n: " ))
fatorial = 1
i = 1
while(i<=n):
	fatorial = i*fatorial
	i+=1
print(fatorial)