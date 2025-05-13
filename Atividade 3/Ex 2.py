def estaDentro(x,y,z):
    if (x <= y) and ( y<= z):
        return True
    else:
        return False
    
x = input("Informe o valor de x: ")
y = input("Informe o valor de y: ")
z = input("Informe o valor de z: ")

if estaDentro(x, y, z):
    print("Verdadeiro")
else:
    print("Falso")