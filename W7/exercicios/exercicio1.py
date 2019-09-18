#Exercício 1
#Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura
#e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo
# informado com caracteres '#' na saída.
#Por exemplo:
#digite a largura: 10
#digite a altura: 3
# ##########
# ##########
# ##########
#digite a largura: 2
#digite a altura: 2
# ##
# ##

def desenhaLinha(x):
        linha=""
        while(x>0):
                linha = linha + "#"
                x-=1
        print(linha)

largura = int(input("largura: "))
altura = int(input("altura: "))
while(altura>0):
        desenhaLinha(largura)
        altura-=1