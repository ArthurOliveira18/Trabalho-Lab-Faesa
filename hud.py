from matriz import matrizMaisSeguidores, menosSeguidores, mostrarTabela


# Loop principal do menu
while True:
    print("\n--- BEM-VINDO AO SISTEMA ---")
    print("1. Cadastrar novos dados a matriz")
    print("2. Listagem da matriz")
    print("3. Editar os dados da matriz")
    print("3. Relatório/pesquisa")
    print("0. Sair")

    escolha = input("Digite sua opção: ")

    match escolha:
        case "1":
            # Criei uma váriavel pra salvar os valores de cada resultado da matriz
            dadosGanhos = matrizMaisSeguidores()
            dadosPerdidos = menosSeguidores()

        case "2":
            mostrarTabela(dadosGanhos, dadosPerdidos)

        case "3":
            print("teste 3")

        case "4":
            print("Teste 4")

        case "0":
            print("Obrigado por usar o sistema. Saindo...")
            break  # Quebra o loop 'while True'

        case _:
            # O 'case _' (underscore) é o caso padrão (default)
            # Ele captura qualquer outra entrada que não "casou"
            print("Opção inválida! Por favor, tente novamente.")
