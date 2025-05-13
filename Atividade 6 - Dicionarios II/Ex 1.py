agendaContatos = { }
nome = input("Digite o nome do contato: ")
telefone = input("Digite otelefone do contato: ")
i=0
while i != 6:
    if i==0:
        print('Escolha uma opção para prosseguir:', end="" +
        '1-Criar um novo contato.', end="" +
        '2-Pesquisar um contato.', end="" +
        '3-Imprimir (mostrar) os contatos.', end="" +
        '4-Editar contato.', end="" +
        '5-Apagar contato.', end="" +
       '6-Sair', end="")
    if i==1:
        agendaContatos[nome]=telefone #Cria um novo contato
    if i==2:
        nomeBuscar = input("Digite o nome do contato para busca: ")
        agendaContatos.get(nomeBuscar)
    if i==3:
        agendaContatos.items()
    if i==4:
        nomeEditar = input("Digite o nome do contato para editar: ")
        telefoneNovo = input("Digite o novo número do contato: ")
        agendaContatos[nome]=telefoneNovo
    if i==5:
        nomeExcluir = input("Digite o nome do contato para excluir: ")
        del agendaContatos[nomeExcluir]

print("Finalizado.")