tempo = input("Informe o valor dos segundos: ")
segundosInt = int(tempo)


horas = segundosInt//3600
minutos = (segundosInt-(horas*3600))//60
segundos = segundosInt - (minutos*60) - (horas*3600)

print("convertendo os segundos informados em Hora, minuto e segundos: ", horas,":",minutos,":", segundos)