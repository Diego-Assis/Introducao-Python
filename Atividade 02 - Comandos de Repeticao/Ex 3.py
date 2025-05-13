palavra = input("Informe o nome da cidade:")
tamanho = len(palavra)

for i in range(tamanho-1, -1, -1):
    print(palavra[i], end="")