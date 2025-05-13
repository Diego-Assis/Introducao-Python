import math
distancia = [1, 10, 100, 500, 1000]
frequencia = 2.4*pow(10,9)
Ptx = 30
Gtx = 2
Grx = 2

def FSPL(distancia, frequencia):
    fspl = 20*(math.log10(distancia)) + (20*math.log10(frequencia)) - 147.55
    return fspl

def Prx(Ptx, Gtx, Grx, distancia, frequencia):
    Prx = Ptx + Gtx + Grx - FSPL(distancia, frequencia)
    return Prx



for i in range(len(distancia)):
    print("Para a distancia: ", distancia[i], ", o valor de FSPL é: ", FSPL(distancia[i], frequencia), " e a potencia recebida é: ", Prx(Ptx, Gtx, Grx, distancia[i], frequencia))