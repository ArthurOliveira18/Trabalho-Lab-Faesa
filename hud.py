# Importe a nova função aqui
# Adicione gerarRelatorio no final do import
from matriz import (
    matrizMaisSeguidores,
    menosSeguidores,
    mostrarTabela,
    atualizarDados,
    gerarRelatorio,
)

# Inicializa as variáveis vazias antes do loop para evitar erro de "NameError"
dadosGanhos = []
dadosPerdidos = []

# Loop principal do menu
while True:
    print("\n--- BEM-VINDO AO SISTEMA ---")
    print("1. Cadastrar novos dados a matriz")
    print("2. Listagem da matriz")
    print("3. Editar os dados da matriz")
    print("4. Relatório/pesquisa")  # Corrigi a numeração que estava repetida
    print("0. Sair")

    escolha = input("Digite sua opção: ")

    match escolha:
        case "1":
            # Criei uma váriavel pra salvar os valores de cada resultado da matriz
            dadosGanhos = matrizMaisSeguidores()
            dadosPerdidos = menosSeguidores()

        case "2":
            # Só chama se tiver dados
            mostrarTabela(dadosGanhos, dadosPerdidos)

        case "3":
            # Chama a nova função passando as matrizes atuais
            atualizarDados(dadosGanhos, dadosPerdidos)

        case "4":
            # Chama a função de relatório passando as listas preenchidas
            gerarRelatorio(dadosGanhos, dadosPerdidos)

        case "0":
            print("Obrigado por usar o sistema. Saindo...")
            break  # Quebra o loop 'while True'

        case _:
            # O 'case _' (underscore) é o caso padrão (default)
            print("Opção inválida! Por favor, tente novamente.")
