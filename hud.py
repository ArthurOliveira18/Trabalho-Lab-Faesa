from matriz import (
    matrizMaisSeguidores,
    menosSeguidores,
    mostrarTabela,
    atualizarDados,
    gerarRelatorio,
)

dadosGanhos = []
dadosPerdidos = []

while True:
    print("\n--- BEM-VINDO AO SISTEMA ---")
    print("1. Cadastrar novos dados a matriz")
    print("2. Listagem da matriz")
    print("3. Editar os dados da matriz")
    print("4. Relatório/pesquisa")
    print("0. Sair")

    escolha = input("Digite sua opção: ")

    match escolha:
        case "1":
            dadosGanhos = matrizMaisSeguidores()
            dadosPerdidos = menosSeguidores()

        case "2":
            mostrarTabela(dadosGanhos, dadosPerdidos)

        case "3":
            atualizarDados(dadosGanhos, dadosPerdidos)

        case "4":
            gerarRelatorio(dadosGanhos, dadosPerdidos)

        case "0":
            print("Obrigado por usar o sistema. Saindo...")
            break

        case _:
            print("Opção inválida! Por favor, tente novamente.")
