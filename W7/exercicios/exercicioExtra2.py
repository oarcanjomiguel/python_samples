#Exercício 2 - (Difícil) Soma das hipotenusas
#Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro
#positivo n e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

#Dica1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para 
#este exercício é fazer um laço de 1 até n testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. 
#Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

#Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.
#Exemplo:
# Para n = 25, as hipotenusas são:
# 5, 10, 13, 15, 17, 20, 25
# note que cada número deve ser somado apenas uma vez. Assim:
# soma_hipotenusas(25)
# deve devolver 105

import math
def eHipotenusa(hipotenusa):
        #ir de x-1 ate 1 com um dos catetos e verificar se o outro e inteiro:
        #if(catetoCalculado % 1 == 0):
        #       return True
        catetoCandidato = hipotenusa - 1
        while(catetoCandidato>=1):
                if( (math.sqrt(hipotenusa**2 - catetoCandidato**2) )%1==0 ):
                        return True
                catetoCandidato-=1
        return False

def soma_hipotenusas(n):
        soma = 0
        while(n>0):
                if(eHipotenusa(n)):
                        soma+=n
                n-=1
        return soma
