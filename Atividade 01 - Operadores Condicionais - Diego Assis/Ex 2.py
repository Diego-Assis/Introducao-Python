salario = input("Informe o salario do colaborador: ")
salarioFloat = float(salario)

if salarioFloat <= 280.0:
    print("O salario antes do reajuste era: ", salarioFloat)
    print("O salario foi aumentado em 20%")
    print("O valor do aumento é de: ", salarioFloat*0.20)
    print(salarioFloat*1.2)
elif salarioFloat >= 280.0 and salarioFloat < 700.0:
    print("O salario antes do reajuste era: ", salarioFloat)
    print("O salario foi aumentado em 15%")
    print("O valor do aumento é de: ", salarioFloat*0.15)
    print(salarioFloat*1.15)
elif salarioFloat >= 700.0 and salarioFloat < 1500.0:
    print("O salario antes do reajuste era: ", salarioFloat)
    print("O salario foi aumentado em 1%")
    print("O valor do aumento é de: ", salarioFloat*0.01)
    print(salarioFloat*1.01) 
elif salarioFloat > 1500.0:
    print("O salario foi aumentado em 5%")
    print("O salario antes do reajuste era: ", salarioFloat)
    print("O valor do aumento é de: ", salarioFloat*0.05)
    print("O novo salario é: ", salarioFloat*1.05)