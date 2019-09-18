#Exercício 3
#Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
#Exemplo:
#Digite um número inteiro: 123
#6

numero = int(input("Digite um número inteiro: ") )
soma = 0
while(numero>0):
	digito = numero % 10
	numero = numero // 10
	soma = soma + digito
print(soma)