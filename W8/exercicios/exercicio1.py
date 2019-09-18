#Exercício 1 - Removendo elementos repetidos
#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros,
#verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista
#correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
#Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
#Exemplo:
#>>>lista = [2, 4, 2, 2, 3, 3, 1]
#>>>remove_repetidos(lista)
#[1, 2, 3, 4]
#>>>remove_repetidos([1, 2, 3, 3, 3, 4])
#[1, 2, 3, 4]

def remove_repetidos(lista):
        lista.sort()
        listaRepetidos  = []
        listaNova = []
        for i in range(len(lista)-1):
                if(lista[i] == lista[i+1]):
                        listaRepetidos.append(i)
        for i in range(len(lista)):
                if(not (i in listaRepetidos)):
                        listaNova.append(lista[i])
        return listaNova
