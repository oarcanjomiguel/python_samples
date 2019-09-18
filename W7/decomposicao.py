#457136254
#654923
def ePrimo(n):
    fator = 2
    if(n == 2):
        return True
    
    while(fator<=n/2 and (n%fator!=0)):
        fator+=1
    if n%fator == 0:
          return False
    else:
          return True

def main():
    i=2
    numero = int(input("Digite um numero positivo: "))
    #numeroDigitado = numero
    while(numero>1):
        multiplicidade = 0
        #achou um fator primo, tenta dividir
        while(numero%i == 0):
            #eh divisivel, verifica a multiplicidade
            multiplicidade+=1
            numero = numero / i
        if(multiplicidade > 0):
            print("Fator:", i, "multiplicidade:",multiplicidade)
        i+=1

main()
