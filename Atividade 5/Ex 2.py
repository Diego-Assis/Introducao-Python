paises = { "Brasil": 55, "Estados Unidos": 1, "Portugal": 351, "Bolívia": 591, "Equador": 593 }

print("O comprimento deste dicionario é: ", len(paises))

for key in paises:
    print(paises[key])


print(paises.items())

print(paises.keys())

print(paises.values())

del paises["Portugal"]

print("Codigo: ", paises.get('Brasil'))