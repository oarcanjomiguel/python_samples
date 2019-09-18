#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve 
#o maior número primo menor ou igual ao número passado à função
#Exemplos de execução no shell do Python:
#>>> maior_primo(100)
#97
#>>> maior_primo(7)
#7
#Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o 
#número é primo ou não; se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.
def e_primo(x):
	numero = x
	primo = True
	while(x>2 and primo):
		x-=1
		if(numero%x == 0):
			primo = False
	return primo
	
def maior_primo(x):
	i=3
	maior = i
	while(i<=x):
		if(e_primo(i)):
			maior = i
		i+=1
	return maior
