#Exercício 1 - Primos
#Escreva a função n_primos que recebe como argumento um número inteiro maior ou 
#igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
#Exemplo:
#>>>n_primos(2)
#1
#>>>n_primos(4)
#2
#>>>n_primos(121)
#30
def ePrimo(n):
    fator = 3
    if(n == 2):
        return True
    
    while(fator<=n/2 and (n%fator!=0)):
        fator+=1
    if n%fator == 0:
          return False
    else:
          return True
        
        
def n_primos(numero):
        primos = 0
        while(numero>1):
                if(ePrimo(numero)):
                        primos+=1
                numero-=1
        return primos

#print(n_primos(int(input("Digite um numero inteiro maior que 2: "))))