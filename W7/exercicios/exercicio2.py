#Exercício 2
#Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
#Por exemplo:
#digite a largura: 10
#digite a altura: 3
# ##########
# #        #
# ##########
#digite a largura: 2
#digite a altura: 2
# ##
# ##

def desenhaLinha(tamanho,caracter):
        linha = ""
        posicao = tamanho
        while(posicao>0):
                if(posicao == tamanho) or (posicao == 1):
                        linha = linha + "#"
                else:
                        linha = linha + caracter
                posicao-=1
        print(linha)
altura = 0
largura = 0
while(altura < 1 or largura < 1):
        largura = int(input("Digite uma largura positiva: "))
        altura = int(input("Digite uma altura positiva: "))
        if(altura < 1 or largura < 1):
                print("parâmetros inválidos!")
alturaDigitada = altura
while(altura>0):
        if(altura == alturaDigitada) or (altura == 1):
                desenhaLinha(largura,"#")
        else:
                desenhaLinha(largura," ")
        altura-=1