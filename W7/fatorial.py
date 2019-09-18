def fatorial(numero):
    fat=1
    while(numero>1):
        fat = fat * numero
        numero -= 1
    return fat

def main():
    numero = 1
    while numero > 0:
        numero = int(input("Digite um número maior que 0: "))
        if(numero >=0):
            print("Fatorial de", numero, "=", fatorial(numero))
        else:
            print("Não existe fatorial de número negativo.")
        
main()
