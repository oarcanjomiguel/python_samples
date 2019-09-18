# Exercício 2
# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:
# Exemplo:
# Entrada de Dados:
# Digite a primeira nota: 4
# Digite a segunda nota: 5
# Digite a terceira nota: 6
# Digite a quarta nota: 7
# Saída de Dados:
# A média aritmética é 5.5

primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))
terceiraNota = float(input("Digite a terceira nota: "))
quartaNota = float(input("Digite a quarta nota: "))

mediaAritmetica = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4

print("A média aritmética é", mediaAritmetica)