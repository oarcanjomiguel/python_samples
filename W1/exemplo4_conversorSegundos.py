segundos = int(input("Numero de segundos: "))

dias = (segundos // 3600) // 24
horas = (segundos // 3600) - dias * 24
minutos = (segundos % 3600) // 60
segundosRestantes = (segundos % 3600) %60


print(dias, " dias, ", horas, " horas, ", minutos, " minutos, ", segundosRestantes, " segundos.")