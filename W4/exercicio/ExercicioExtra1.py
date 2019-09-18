#Exercício 1
#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo".
#Caso contrário, imprima "não primo".
#Exemplos:
#Digite um número inteiro: 13
#primo
#Digite um número inteiro: 12
#não primo

numero = int(input("Digite um número inteiro: "))
i=2
primo=True
while(primo and i<numero):
	if(numero%i == 0):
		primo = False
		print("não primo")
	i+=1
if(primo):
	print("primo")
