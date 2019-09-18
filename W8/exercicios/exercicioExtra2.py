#Exercício 2 - Invertendo sequência
#Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números in    teiros e 
#imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.
#Exemplo:
#Digite um número: 1
#Digite um número: 7
#Digite um número: 4
#Digite um número: 0
#4
#7
#1

lista = []
elemento = 1
while(elemento != 0):
    elemento = int(input("Digite um número: "))
    if(elemento != 0):
        lista.append(elemento)
#print(lista)
for i in range(len(lista)):
    print(lista[len(lista)-i-1])