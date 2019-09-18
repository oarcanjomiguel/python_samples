#Exercício 5 - Verificando ordenação
#Receba 3 números inteiros na entrada e imprima
#crescente
#se eles forem dados em ordem crescente. Caso contrário, imprima
#não está em ordem crescente

primeiroNumero = int(input("Digite o primeiro numero: ") )
segundoNumero = int(input("Digite o segundo numero: ") )
terceiroNumero = int(input("Digite o terceiro numero: ") )
if((primeiroNumero <= segundoNumero) and (segundoNumero <= terceiroNumero) ):
	print("crescente")
else:
	print("não está em ordem crescente")